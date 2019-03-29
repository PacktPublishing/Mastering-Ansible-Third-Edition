# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

Run this command:

    ansible-vault create --vault-id @prompt secrets.yaml

Then insert the following data into the Vault:

    ---
    my_secret: is_safe

You can try and read the resulting file with:

    cat secrets.yaml


