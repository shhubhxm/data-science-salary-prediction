# Django Deploy on heroku

## CMD
```python
django-admin startproject file_name
-------------------------------------------------------------------------------------------------------------
python manage.py runserver                                                  - inside vscode
```

## VSCode
```python
from django.shortcuts import render                                         - views.py
-------------------------------------------------------------------------------------------------------------
def home(request):
    return render(request, "home.html")                                     - views.py
-------------------------------------------------------------------------------------------------------------  
from . import views                                                         - urls.py
-------------------------------------------------------------------------------------------------------------
path('', views.home, name="home")                                           - urls.py(path)
-------------------------------------------------------------------------------------------------------------
import os                                                                   - settings.py
-------------------------------------------------------------------------------------------------------------
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")                                        - settings.py(below static url)
]
-------------------------------------------------------------------------------------------------------------
{% load static %} {% static  "" %}                                          - home.html(at top)
```

## Heroku
```python
pip install gunicorn
create procfile
pip freeze > requirements
heroku login - vscode terminal
heroku keys - vscode terminal
heroku apps:rename newname(for renaming only)
```
