pip3 install virtualenv
virtualenv env
source env/bin/activate
pip3 install requests
pip3 install beautifulsoup4
pip3 freeze > requirements.txt
deactivate
