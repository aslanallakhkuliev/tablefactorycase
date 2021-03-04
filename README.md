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

### Admin Panel:
/admin/

### API Structure

api/tables/
api/tables/create/',views.TableCreateApi.as_view()),
api/tables/<int:pk>/',views.TableViewByIdApi.as_view()),
api/tables/<int:pk>/update/',views.TableUpdateApi.as_view()),
api/tables/<int:pk>/delete/',views.TableDeleteApi.as_view()),

api/legs/
api/legs/create/
api/legs/<int:pk>/
api/legs/<int:pk>/update/
api/legs/<int:pk>/delete/

api/feet/
api/feet/create/
api/feet/<int:pk>/
api/feet/<int:pk>/update/
api/feet/<int:pk>/delete/

