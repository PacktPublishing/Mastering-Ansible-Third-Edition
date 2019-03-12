# Instructions

Tested on:
- CentOS 7.6
- Ansible 2.7.5

Below are the commands referenced in the book to install AWX and enable HTTPS support:

    git clone https://github.com/ansible/awx.git

    cd awx/installer

    sudo ansible-playbook -i inventory install.yml

    sudo yum install nginx

    openssl req -x509 -nodes -newkey rsa:4096 -keyout /etc/pki/tls/private/mastery.example.com.key -out /etc/pki/tls/certs/mastery.example.com.crt -days 3650 -subj "/C=GB/CN=mastery.example.com"

Change the default listening port in `nginx.conf`:

    server {
      listen 81 default_server;
      listen [::]:81 default_server;

Enable and start the service:

    sudo systemctl enable nginx.service
    sudo systemctl start nginx.service

Allow HTTPS through the firewall:

    sudo firewall-cmd --permanent --add-service=https
    sudo firewall-cmd --reload

