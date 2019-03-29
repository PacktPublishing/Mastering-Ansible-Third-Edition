# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

Edit this core Ansible file (this time by copying to a local `library/` directory first):

    mkdir library
    cp /usr/lib/python2.7/site-packages/ansible/modules/system/systemd.py library

Insert the following line as shown in the accompanying book:

    import rpdb; rpdb.set_trace(addr="0.0.0.0")

Edit the accompanying inventory to match your test host, then run the playbook:

    ansible-playbook -i mastery-debug rpdb.yaml -vv

Once the playbook is running, it will appear to hang. At this point you can telnet into the remote host on port 4444 and use rpdb as described in the book.

