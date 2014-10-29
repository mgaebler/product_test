# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.require_version ">= 1.5.1"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/precise64"

  config.vm.provider "virtualbox" do |v, override|
    v.customize ["modifyvm", :id, "--cpus", "2"]
    v.customize ["modifyvm", :id, "--memory", "1024"]
  end

  config.vm.provider "vmware_fusion" do |v, override|
    v.vmx["numvcpus"] = "1"
    v.vmx["memsize"] = "1024"
    #v.gui = true
  end

  config.vm.define "trendsetter" do |machine|
    machine.vm.network :private_network, ip: "192.168.105.11"
  end

  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = 'ansible/vagrant.yml'
    ansible.inventory_path = 'ansible/vagrant'
    ansible.limit = 'vagrant'
    #ansible.verbose = 'v'
  end

  config.ssh.forward_agent = true
end
