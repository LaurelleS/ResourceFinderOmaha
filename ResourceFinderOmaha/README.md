# ResourceFinderOmaha
**A web app that helps Omaha residents find local events and community resources.**

Built with **Django** (Python web framework) and **SQLite** (local database).

---

## Team Setup Guide

Follow these steps to get the project running on your computer.

### 1. Open the Project
- Download or clone the project folder (`ResourceFinderOmaha`)
- Open it in **VS Code**

---

### 2. Set Up Python Environment
We use a **virtual environment** so everyone has the same setup.

In the **VS Code terminal** here is some of the commands you can do:

```bash
# Activate the virtual environment (Powershell or CMD if powershell doesn't work for you) 
.\.venv\Scripts\Activate.ps1

#Install Django
py -m pip install Django==5.2.7 ##I had issues installing the 5.2.7 version so I just ran it without the '==5.2.7' part and it installed the latest version available

#run migrations
python manage.py makemigrations
python manage.py migrate

#creates a superuser (used for logging into the admin dashboard)
python manage.py createsuperuser

#Opens the Admin Dashboard
http://127.0.0.1:8000/admin

#This loads some sample's that I made that we can use for testing
python manage.py loaddata events/fixtures/seed.json

#Open Django shell
python manage.py shell
