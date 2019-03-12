# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

Run this playbook using the command:

    time ansible-playbook -i mastery-inventory.py inventory_test.yaml --limit backend,frontend,errors
