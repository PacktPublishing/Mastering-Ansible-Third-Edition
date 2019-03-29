# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5
- Cumulus VX 3.7.3

Adjust the inventory file to suit your setup, and then test with:

    ansible -i switch-inventory -m ping mastery-switch1

We can then query the switch using this playbook:

    ansible-playbook -i switch-inventory switch-query.yaml

Ports can then be configured using this playbook as discussed in the book:

    ansible-playbook -i switch-inventory switch-l2-configure.yaml
