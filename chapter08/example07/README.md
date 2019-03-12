# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

This example requires you to edit a core Ansible file - it might be worth making a backup before proceeding.

    sudo vim /usr/lib/python2.7/site-packages/ansible/inventory/manager.py

Add the following line just below `def parse_sources...`

    import pdb; pdb.set_trace()

Now run the playbook as we did before:

    ansible-playbook -i mastery-hosts objmethod.yaml

Try out the following commands in the interactive `pdb` session:

    where
    list
    p self._sources
    next
    step
    continue

