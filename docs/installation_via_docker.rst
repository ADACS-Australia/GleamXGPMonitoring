Installation Via Docker
================

For Ubuntu / Debian systems, please go through the following guide on how to install Docker and the docker compose plugin:

https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository


Once docker is installed, download or clone the GleamXGPMonitoring repository from github:

https://github.com/ADACS-Australia/GleamXGPMonitoring

The repository contains a `docker-compose.yaml` that contains the setup information for the webapp.
Edit environment varialbes as needed for the deployment:

.. code-block::
    x-environment: &environment
    DB_NAME: "mwa_image_plane_db"
    DB_USERNAME: '<secret to be generated or chosen>'
    DB_PASSWORD: '<secret to be generated or chosen>'

    # Needed for the postgres container
    POSTGRES_PASSWORD: '<secret to be generated or chosen>'

    # Django variables
    DJANGO_SECRET_KEY: '<secret to be generated or chosen>'
    PYTHONUNBUFFERED: 1

    # Web hosting details
    WAN_IP: '<WAN IP of the host>'
    GLEAM_URL: "mwa-image-plane.duckdns.org"

.. _docker_compose_yaml:

For running the webapp, go into the GleamXGPMonitoring repo files and run the following command:

.. code-block::
    docker compose up -d
.. _run_docker:

which will download, build and run the webapp locally. 





