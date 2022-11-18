Vagrant.configure("2") do |config|
  servers=[
      {
        :hostname => "control",
        :box => "bento/ubuntu-18.04",
        :ip => "192.168.56.90",
        :ssh_port => '9900'
      },
      {
        :hostname => "application",
        :box => "bento/ubuntu-18.04",
        :ip => "192.168.56.91",
        :ssh_port => '9908'
      },
      {
        :hostname => "backup",
        :box => "bento/ubuntu-18.04",
        :ip => "192.168.56.92",
        :ssh_port => '9909'
      },
    ]

  servers.each do |machine|
      config.vm.define machine[:hostname] do |node|
          node.vm.box = machine[:box]
          node.vm.hostname = machine[:hostname]
          node.vm.network :private_network, ip: machine[:ip]
          node.vm.network "forwarded_port", guest: 22, host: machine[:ssh_port], id: "ssh"
          node.vm.provider :virtualbox do |vb|
              vb.customize ["modifyvm", :id, "--memory", 2048]
              vb.customize ["modifyvm", :id, "--cpus", 1]
              vb.customize ["modifyvm", :id, "--vram", "128"]
          end  
      end
  end
end 