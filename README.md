sudo apt-get install python-dev python-pip supervisor build-essential libffi-dev -y

sudo mkdir /var/log/core

sudo chmod 777 -Rf /var/log/core

sudo mkdir /usr/local/cache_server

sudo chown -R $USER: /usr/local/cache_server

sudo chmod 777 -Rf /usr/local/cache_server

git clone git clone <from your repo>

cd /usr/local/cache_server/core_server/

sudo pip install --upgrade pip

pip install -r requirements.txt

sudo ln -s /usr/local/cache_server/core_server/config/cache_server.conf /etc/supervisor/conf.d

sudo /etc/init.d/supervisor restart
