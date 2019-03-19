# Instructions

Tested on:
- Windows Server 2016 Standard Edition build 14393
- CentOS 7.6

Import your CA signed certificate into the Windows Certificate store:

    Import-Certificate -FilePath .\certnew.cer -CertStoreLocation Cert:\LocalMachine\My

Delete any previously created WinRM listeners:

    winrm delete winrm/config/Listener?Address=*+Transport=HTTPS

Create a new HTTPS listener referring to the new CA signed certificate:

    New-Item -Path WSMan:\Localhost\Listener -Transport HTTPS -Address * -CertificateThumbprint <thumbprint of certificate>

Place a copy of the Base64 encoded CA certificate for the above in `/etc/pki/ca-trust/source/anchors/` on the Ansible host. Then run:

    sudo update-ca-trust enable
    sudo update-ca-trust extract

Finally, update the enclosed inventory with the correct details for your Windows host and run the following command to test Ansible connectivity:

    ansible -i windows-hosts -m win_ping all
