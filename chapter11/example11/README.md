# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5
- Docker version 1.13.1
- Ansible Container version 0.9.2

Perform the following commands to prepare your system for ansible-container:

    sudo pip uninstall docker-py
    sudo pip uninstall docker
    sudo pip install docker==2.7.0
    sudo sed -i "s/return os.path.join(os.sep, 'run', 'secrets')/return os.path.join(os.sep, 'docker', 'secrets')/g" /usr/lib/python2.7/site-packages/container/docker/engine.py 
    sudo pip install -U setuptools
    sudo pip install "ansible-container[docker,openshift]"

You can build the container as shown in the book:

    cd ansible
    ansible-container build

Then run the container when built:

    ansible-container run --detached
    docker ps --filter name=cowsay
    curl http://localhost:8081

