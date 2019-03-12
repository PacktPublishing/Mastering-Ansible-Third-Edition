# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5
- Amazon EC2

To run this example, you will need an AWS account, and your credentials for this. Put your credentials where indicated into the playbook, then run it with the command:

    ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i mastery-hosts boot-ec2-server.yaml --private-key mastery-key.pem

Where mastery-key.pem is your private SSH key downloaded from the keypair you created in EC2.

