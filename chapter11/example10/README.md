# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5
- Docker version 1.13.1

Download the Docker dynamic inventory file as shown:

    curl -O https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/docker.py

You can test it as shown in the book with these commands:

    ./docker.py --help
    ./docker.py --list --pretty | grep -C2 playbook-container


