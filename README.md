# Installation

```
sudo apt-get install python-dev python-pip supervisor build-essential libffi-dev -y

sudo mkdir /var/log/core

sudo chmod 777 -Rf /var/log/core

sudo mkdir /usr/lib/<your_name>

sudo chown -R $USER: /usr/lib/<your_name>

sudo chmod 777 -Rf /usr/lib/<your_name>

git clone git clone <from your repo>

cd /usr/lib/<your_name>/Enterprise_txJSON-RPC/

sudo pip install --upgrade pip

pip install -r requirements.txt

sudo ln -s /usr/lib/<your_name>/Enterprise_txJSON-RPC/config/<your_name>.conf /etc/supervisor/conf.d

sudo /etc/init.d/supervisor restart
```
