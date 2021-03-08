# Solution For The Table Factory Case

## Clone The Project

git clone https://github.com/aslanallakhkuliev/tablefactorycase.git

cd tablefactorycase

## How To Run The Project

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

**Create admin user (if required):**  
python3 manage.py createsuperuser

**Import demo data (optional):**
python3 manage.py loaddata initial_data.json

**Start the server:**
python3 manage.py runserver

## User Info (Read-Only)

/tables/
/legs/
/feet/

## Admin Panel

/admin/

## API Structure

/api/tables/  
/api/legs/  
/api/feet/

## Testing

Start the server before running tests.

Open new terminal (or console) tab.

Activate virtual environment from the project folder:  
source venv/bin/activate

**Run Command:**
pytest

## Recent Changes

User-authentication for the API has been activated.

API is now using Model ViewSet.

User interface has been simplified similar to the API.

PEP8 standards have been applied.

Requirements have been updated.

15 Model Tests have been added (in addition to the API tests).

API Tests now support django fixtures and user authentication.
