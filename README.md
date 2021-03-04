### The solution for the table factory case

git clone https://github.com/aslanallakhkuliev/tablefactorycase.git

### How to run the project

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

If required:
python3 manage.py createsuperuser

python3 manage.py runserver
