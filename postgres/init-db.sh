#!/bin/bash
set -e

# Initialise the DB on only the first ever start-up 
# Have to do this per line otherwise postgres complains
psql -v ON_ERROR_STOP=1 -c "CREATE DATABASE $DB_NAME;"
psql -v ON_ERROR_STOP=1 -c "CREATE USER $DB_USERNAME WITH ENCRYPTED PASSWORD '$DB_PASSWORD';"
psql -v ON_ERROR_STOP=1 -c "ALTER ROLE $DB_USERNAME SET client_encoding TO 'utf8';"
psql -v ON_ERROR_STOP=1 -c "ALTER ROLE $DB_USERNAME SET default_transaction_isolation TO 'read committed';"
psql -v ON_ERROR_STOP=1 -c "ALTER ROLE $DB_USERNAME SET timezone TO 'UTC';"

# Apply superuser role to create the q3c extension
psql -v ON_ERROR_STOP=1 -c "ALTER ROLE $DB_USERNAME SUPERUSER;"