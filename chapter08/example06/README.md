# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

Run this playbook using the command:

    ansible-playbook -i mastery-hosts objmethod.yaml

In the interactive debug session, run the following commands (full explanation of these commands is in the accompanying book):

    p task
    p task.args
    task_vars['derp']['missing'] = "the end"
    r

