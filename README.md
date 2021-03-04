The solution for the table factory case.
How to run the project:

git clone https://github.com/<username>/<forked-repo>.git

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

If required:
python3 manage.py createsuperuser

python3 manage.py runserver
