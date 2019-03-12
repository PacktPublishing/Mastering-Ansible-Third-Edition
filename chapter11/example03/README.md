# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5
- OpenStack devstack release March 2019

Run this playbook using the command (assumes prior setup of OpenStack - adjust the playbook according to your environment):

    ansible-playbook -i mastery-hosts boot-server.yaml --private-key mastery-key

Note that `mastery-key` should be the private SSH key created in and then downloaded from your OpenStack environment.
