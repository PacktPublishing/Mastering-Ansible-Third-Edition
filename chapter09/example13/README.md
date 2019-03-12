# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

Run these commands to prepare for the code tests:

    wget https://rpmfind.net/linux/centos/7.6.1810/os/x86_64/Packages/pytest-2.7.0-2.el7.noarch.rpm
    sudo rpm -Uvh pytest-2.7.0-2.el7.noarch.rpm
    wget http://springdale.math.ias.edu/data/puias/computational/7/x86_64//python-mock-1.0.1-5.sdl7.noarch.rpm
    sudo rpm -Uvh python-mock-1.0.1-5.sdl7.noarch.rpm 
    sudo yum install python-peak-util-symbols.noarch python2-packaging python2-pycodestyle
    sudo pip install setuptools

Run these commands to perform the code tests described in the book:

    cd ~/src
    git clone https://github.com/ansible/ansible.git
    cd ansible
    source ./hacking/env-setup
    py.test test/units/parsing
    test/runner/ansible-test integration -v ping
    test/runner/ansible-test integration -v posix/ci/
    make pep8

Mix tabs and spaces on a line of your choosing in a file such as: lib/ansible/modules/cloud/openstack/os_zone.py

    make pep8

