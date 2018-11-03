# Persona API
The Persona API is a fake RESTful API that delivers made up data on a few endpoints. The data sits within a zip file and needs to be decompressed only on deployment not when it sits in this repository. So you have to find a way to do that in an elegant manner.

### Setting up the container

###### BUILD CONTAINER:

    docker build -t persona-api:<version> .

###### RUN CONTAINER:

    docker run -p <local_port>:<docker_port> -it persona-api:<version>

IMPORTANT: The first port (local port) can be what ever I want the second port (docker port) must be the same as the PORT env in the docker file. If you want, you can change the docker port when starting the container like so:

    docker run -p <local_port>:<docker_port> -e PORT=<docker_port> -it persona-api:<version>


### Setting up the local enviroment for debugging using Pycharm

###### USING VIRTUALENV:

Create a virtual environment:

    virtualenv <env_name> --python=<path_to_python>

Create a virtual environment (inheriting systems package):

    virtualenv <env_name> --python=<path_to_python> --system-site-packages

Activate virtual environment:

    source <env_name>/bin/activate

Deactivate virtual environment:

    deactivate

###### USING VIRTUALENVWRAPPER:

Install virtualenvwrapper:

    pip install virtualenvwrapper

Setting virtualenvwrapper in bash_profile:

    # Setting virtualenvwrapper

    # set where virutal environments will live
    export WORKON_HOME=$HOME/environment/.virtualenvs
    # ensure all new environments are isolated from the site-packages directory
    export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
    # use the same directory for virtualenvs as virtualenvwrapper
    export PIP_VIRTUALENV_BASE=$WORKON_HOME
    # makes pip detect an active virtualenv and install to it
    export PIP_RESPECT_VIRTUALENV=true

    if [[ -r <path_to_virtualenvwrapper.sh> ]]; then
    source <path_to_virtualenvwrapper.sh>
    else
        echo "WARNING: Can't find virtualenvwrapper.sh"
    fi

Create a virtual environment:

    mkvirtualenv <env_name> --python=<path_to_python>

Create a virtual environment (inheriting systems package):

    mkvirtualenv <env_name> --python=<path_to_python> --system-site-packages

Activate virtual environment:

    workon <env_name>

Deactivate virtual environment:

    deactivate

IMPORTANT: If using PyCharm make sure to associate the virtual env to the project

###### INSTALL DEPENDENCIES:

Install all the project requirements:

    pip install -r requirements.txt

###### CONFIGURE PYCHARM DEBUGGING SERVER CONFIGURATION:
* go to edit configuration
* create a new python configuration (if you use the enterprise edition you may choose a flask configuration)
* set in the script panel the path to the main flask entrypoint (in this case run.py)
* set the following enviroment variables: HOST, PORT, DEBUG, SECRET_KEY, LOG_LEVEL
* set the proper python runtime (should be point to the virtualenv if used one)
* set the working directory (in this case the path to src folder)


