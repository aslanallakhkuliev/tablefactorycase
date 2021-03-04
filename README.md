### Solution For The Table Factory Case

git clone https://github.com/aslanallakhkuliev/tablefactorycase.git

### How To Run The Project

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

**Only if has not been set before:**  
python3 manage.py createsuperuser

python3 manage.py runserver

### Initial Data

Initially, all the tables are empty.  
Feel free to add tables, legs and feet through the admin panel.

### Admin Panel

/admin/

### API Structure

/api/tables/  
/api/tables/create/  
/api/tables/<int:pk>/  
/api/tables/<int:pk>/update/  
/api/tables/<int:pk>/delete/

/api/legs/  
/api/legs/create/  
/api/legs/<int:pk>/  
/api/legs/<int:pk>/update/  
/api/legs/<int:pk>/delete/

/api/feet/  
/api/feet/create/  
/api/feet/<int:pk>/  
/api/feet/<int:pk>/update/  
/api/feet/<int:pk>/delete/

### Tesing

**Command:** pytest
