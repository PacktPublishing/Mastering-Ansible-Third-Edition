# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5
- Docker version 1.13.1

You can check if any related Docker containers are already in existence using the following commands:

    docker ps -a --filter ancestor=fedora-moo
    docker images --filter reference='fedora*'

Then run the playbook as follows to build and run the container:

    ansible-playbook -i mastery-hosts docker-interact.yaml 

Now run the two Docker queries again to see the running container:

    docker ps -a --filter ancestor=fedora-moo
    docker images --filter reference='fedora*'

Also check the container is running with:

    curl http://localhost:8080

