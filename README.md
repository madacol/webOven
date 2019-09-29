# Install

### Install distro Packages

    sudo apt install python3-pip python3-venv
    sudo apt install libatlas-base-dev supervisor   # (Optional) Required to import numpy on raspberry pi and to keep app running, respectively

### Clone repository

    git clone https://github.com/madacol/webOven.git
    cd webOven

### Create virtual environment

    python3 -m venv .venv
    source .venv/bin/activate

### Install python dependencies

    pip3 install -r dependencies.txt

# Running App

    FLASK_APP=app.py FLASK_ENV=development ./.venv/bin/flask run --host=0.0.0.0

# Config supervisor

### Check supervisor is running

    sudo systemctl status supervisor.service

### Add config file

    sudo cp supervisor-weboven.conf /etc/supervisor/conf.d/

### Load config file

    sudo supervisorctl update
    sudo supervisorctl status

### Restart app

Useful when app doesn't starts and needs further tweakings

    sudo supervisorctl restart weboven:
