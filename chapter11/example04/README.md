# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5
- OpenStack devstack release March 2019

For this example, download the OpenStack dynamic inventory provider and associated config template:

    curl -O https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/openstack_inventory.py
    
Next create an appropriate `clouds.yaml` file for your environment - for example:

```yaml
clouds:
  devstack:
    auth:
      auth_url: http://devstack.example.com/identity/v3
      username: admin
      password: password
      project_name: demo
      project_domain_name: "default"
      user_domain_name: "default"
  ansible:
    use_hostnames: True
    expand_hostvars: True
    fail_on_errors: True 
```

Test this dynamic inventory provider as described in the book:

    ./openstack_inventory.py --list

Then when you are happy it is working, run the playbook against this inventory:

    ansible-playbook -i openstack_inventory.py configure-server.yaml --private-key mastery-key

