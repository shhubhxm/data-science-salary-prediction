# Django Deploy

This is before starting html
```python
django-admin startproject SalaryPrediction
python manage.py runserver - inside vscode
```

Inside vscode
```python
from django.shortcuts import render - views.py

def home(request):
    return render(request, "home.html") - views.py
    
from . import views - urls.py

path('', views.home, name="home") - urls.py(path)
```
