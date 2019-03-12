# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

Create a password file for your new Vault using the command:

    echo "my long password" > password_file

Then run this command to create the vault:

    ansible-vault create --vault-id ./password_file more_secrets.yaml

Later try decrypting this with:

    ansible-vault decrypt --vault-id ./password_file more_secrets.yaml

Check the contents to ensure decryption was successful.
