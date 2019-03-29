# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

Run these commands:

    curl -O https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py
    curl -O https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.ini
    sudo yum -y install python-boto

Once you have set your AWS credentials as described in the book run:

    chmod +x ec2.py
    ./ec2.py --list

If you have any virtual instances defined in EC2, run:

    ansible -i ec2.py all -m ping

