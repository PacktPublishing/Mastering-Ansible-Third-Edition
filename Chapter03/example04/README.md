# Instructions

Tested on:
- Windows Server 2016 Standard Edition build 14393
- CentOS 7.6

Installing Kerberos support on the Ansible host:

    sudo yum -y install python-devel krb5-devel krb5-libs krb5-workstation

Install the required Python support:

    sudo yum install python-pip gcc
    sudo pip install pywinrm[kerberos]

Edit `/etc/krb5.conf` as detailed in the book. Then test with (modify to suit your Active Directory domain):

    kinit Administrator@MASTERY.EXAMPLE.COM
    klist

Modify the enclosed inventory to suit your environment. Then test connectivity with:

    ansible -i windows-hosts -m win_ping all

