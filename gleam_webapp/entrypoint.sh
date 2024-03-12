#!/bin/bash
set -e

# # If there's a DB file present, use that to seed it
# if [ -e *.dump]; then 


# fi

#  Check if table has extension installed or not -This means that DB has already been initialised
Q3C_CHECK="$( psql "postgres://$DB_USERNAME:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME" -XtAc "\dx" )"
echo "Extensions in the DB:" $RESULT

if  [[ $Q3C_CHECK == *q3c* ]]; then

    echo "Q3C extension already exists in the DB - Not migrating." 

else 
    echo "Q3C not in DB - Migrating using Django's manage.py"

    python3 manage.py migrate
    python3 manage.py migrate --run-syncdb

    psql "postgres://$DB_USERNAME:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME" -v ON_ERROR_STOP=1 -c "\
        CREATE EXTENSION q3c; \
        CREATE INDEX ON candidate_app_candidate (q3c_ang2ipix(ra_deg, dec_deg)); \
    "
fi 

# This runs the web app locally through Django
# python3 manage.py runserver 0.0.0.0:80 

# This runs the webapp using uwsgi and creates a socket that nginx uses
uwsgi --ini /gleam_webapp/gleam_webapp.uwsgi.ini