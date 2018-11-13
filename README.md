# hackathon19-Django
This project is used for Boston Hackathon 2019.

A memo of how to use Django 2.1.3

>python 3

[Django Documentation](https://docs.djangoproject.com/en/2.1/)  

start:
```cmd
python manage.py runserver
```
---
## Project related files:
urlG.py: get the google stree pictures of giving location.

generate_circle_linspace.py: get the route between two given points.

url_to_img_tag.py: use google cloud vision api to get the object from given pictures.

result.csv: test the html when google cloud vision api is not available.

---
## Django related files:
url.py: control the mapping of url.

views.py: realize the core logic about how it response when getting a url request.

models.py: related to the database.

apps.py: need to install in the root setting file so that Django can recognize your app.(Case Sensitive in INSTALLED_APPS)

templates: form html.

static: include css, js and other resource.