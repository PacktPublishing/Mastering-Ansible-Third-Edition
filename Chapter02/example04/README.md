# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

Ensure `password.sh` is executable:

    chmod +x password.sh

Try encrypting the included vars file using the command:

    ansible-vault encrypt --vault-id ./password.sh a_vars_file.yaml

Check the contents:

    cat a_vars_file.yaml

