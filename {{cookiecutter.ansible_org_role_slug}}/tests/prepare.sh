#/bin/sh

yum -y makecache fast
yum -y install python epel-release make
yum -y makecache fast
yum -y install python2-pip.noarch
pip install --upgrade pip
pip install -r requirements.txt
