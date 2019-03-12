# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

This example requires you to edit a core Ansible file - it might be worth making a backup before proceeding. Also be sure to reverse any changes you made in the previous example before attempting this one.

    sudo vim /usr/lib/python2.7/site-packages/ansible/playbook/__init__.py

Add the following line just below the for loop for `get_all_plugin_loaders` as shown in the book:

    import pdb; pdb.set_trace()

Now run the playbook as we did before:

    ansible-playbook -i mastery-hosts objmethod.yaml

Test out the interactive debug session as described in the book.

Reverse all changes to the Ansible core files when complete.
