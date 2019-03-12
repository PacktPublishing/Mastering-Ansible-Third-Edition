# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5
- Microsoft Azure

To run this example, you will need an Azure account, and your credentials for this. Put your credentials where indicated into the playbook, then run it with the command:

    ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i mastery-hosts boot-azure-server.yaml

Note the setup commands you may need from the book before this will run, including:

    sudo pip install azure
    sudo pip install ansible[azure]
    az login
    az vm image list --offer fedora --all --output table
    az vm image show --urn tunnelbiz:fedora:fedora29:1.0.0
    az vm image accept-terms --urn tunnelbiz:fedora:fedora29:1.0.0
