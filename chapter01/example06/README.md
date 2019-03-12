# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

Run this playbook with the following commands:

    ansible-playbook -i mastery-hosts -c local mastery.yaml
    ansible-playbook -i mastery-hosts -c local --limit frontend mastery.yaml
