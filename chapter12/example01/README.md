# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

Note this is a theoretical example - it will need parameters changing if you have an F5 BIG-IP device to test with:

    sudo pip install f5-sdk
    ansible-playbook -i mastery-hosts reset-f5.yaml
