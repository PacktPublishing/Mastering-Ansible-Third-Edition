# Instructions

Tested on:
- Windows Server 2016 Standard Edition build 14393

Ensure the WinRM Python module is installed on your Ansible host:

    sudo yum install python2-winrm

or:

    sudo pip install "pywinrm>=0.3.0"

Edit the inventory to suit your environment (password, IP address of Windows host) and then run the following command to test connectivity:

    ansible -i windows-hosts -m win_ping all

