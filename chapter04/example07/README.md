# Instructions

Tested on:
- Windows Server 2016 Standard Edition build 14393
- CentOS 7.6

The enclosed playbook contains the file related code snippets from the Windows chapter. It should run provided you create a text file for Ansible to copy across at `~/src/mastery/mastery.txt`:

    ansible-playbook -i windows-hosts win_file.yaml
 
