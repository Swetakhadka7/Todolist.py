<!-- install virtual environment -->
pip install virutalenv

<!-- activte virtual environment -->
env\Scripts\activate(cmd)
.\env\Scripts\activate(powershell)
source .env\bin\activate

<!-- install django -->
pip install django

<!-- create project -->
<!-- django-admin startproject <project_name> . -->
django-admin startproject project .

<!-- create app -->
<!-- python manage.py <app__name> -->
python manage.py startapp todo

<!-- run django -->
python manage.py runserver

<!-- requirements file create -->
pip freeze > requirements.txt

<!-- requirements file install -->
pip install -r requirements.txt

<!-- to open python shell -->
python manage.py shell

<!-- create data -->
MODEL_NAME.objects.create(field1= "..", field2 = "...")

<!-- get all the data of the model -->
MODEL_NAME.objects.all()

<!-- get single data -->
MODEL_NAME.objects.get(id = 1)
<!-- single data lai kunai veriable ma save garna milxa ani tai variable lai use 
garirw we can perform CRUD operation(Create Retrive Update Delete) -->
variable = MODEL_NAME.objects.get(id = 1)
variable.field_name
variable.field_name = "..."

<!-- filter data -->
MODEL_NAME.objects.filter(fields1 = ..., fields2 =...)

<!-- save data -->
MODEL_NAME.save()

<!-- delete -->
MODEL_NAME.delete()

<!-- create superuser -->
python manage.py createsuperuser
