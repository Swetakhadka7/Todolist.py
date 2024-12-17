<!-- install virtual environment -->
env\Scripts\activate(cmd)
.\env\Scripts\activate(powershell)
source .env\bin\activate (linux)

<!-- install django -->
pip install django

<!-- create project -->
django-admin startproject myproject .

<!-- create app -->
<!-- python manage.py <app_name> -->

python manage.py startapp todo

<!-- run django -->
python manage.py runserver

<!-- create requirement file -->
 pip freeze> requirements.txt

 <!-- install requirement file -->
 pip install -r requirements.txt

<!-- to open python shell -->
python manage.py shell



