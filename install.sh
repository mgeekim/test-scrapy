sudo apt install python3.6 python3-pip python3.6-venv

python3.6 -m venv venv
source ./venv/bin/activate

python3.6 -m pip install --upgrade pip
python3.6 -m pip install -r requirements.txt

cd projects
python3.6 -m scrapy crawl ruliweb