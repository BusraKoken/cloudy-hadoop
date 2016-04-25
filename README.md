# Ansible Hadoop in the Cloud

This Ansible playbook creats servers that will act as a cluster on Digitalocean, installs Hadoop on the cluster, performs a distributed map-reduce job on this cluster and destroys the cluster and deletes the servers on Digitalocean at the end.

## Installation

* install ansible [latest version] [ansible-install]. In case of markupsafe does not exist error, install markupsafe python library.

* git clone or zip download this project

* if you did not do it before, add your ssh key to your [digitalocean profile] [digitalocean-profile-link] 

* [generate an api token][digitalocean-api-token] on digitalocean.

* Edit playbooks/roles/create_cluster/vars/main.yml file to enter your ssh key fingerprint and digitalocean api token. You are ready to run the ansible playbook now.

*  in playbooks directory run this command to start deployment:
```sh
ansible-playbook deploy_cluster.yml 
```
* In case of dopy error: 
```sh
pip install 'dopy>=0.3.5,<=0.3.5'
```
and run again:
```sh
ansible-playbook deploy_cluster.yml 
```
* In this project a map reduce python script for word counting is uploaded to the cluster and run it for the count of monte cristo text file to count words. You can ssh to master droplet and see the results at /output/output file. 

* You can modify the playbook and run your own map-reduce job on the created hadoop cluster.

* After finisihing the map-reduce job you can destroy the servers that created on digital ocean by running the task: 
```sh
ansible-playbook destroy_cluster.yml 
```
* Enjoy.    

[ansible-install]: <http://docs.ansible.com/ansible/intro_installation.html>
[digitalocean-profile-link]: <https://cloud.digitalocean.com/settings/security>
[digitalocean-api-token]: <https://cloud.digitalocean.com/settings/api/tokens>
