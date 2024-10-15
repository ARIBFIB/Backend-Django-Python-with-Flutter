# Backend-Django-Python-with-Flutter


![image](https://github.com/user-attachments/assets/f9cc1d52-8bf2-4fdc-b523-067f069fa89f)

Here's a refined version of your Django setup guide, organized and clearly presented without GitHub-specific formatting:

---

# Django Setup with VS Code

## Step 1: Install Dependencies

1. **Install Django and Django REST Framework**  
   Open your terminal and run:
   ```bash
   pip install django djangorestframework
   ```

## Step 2: Create a Django Project

1. **Create a new Django project and application**  
   In your terminal, execute:
   ```bash
   django-admin startproject myproject
   cd myproject
   python manage.py startapp myapp
   ```

## Step 3: Define a Model

1. **Create a model in `myapp/models.py`:**
   ```python
   from django.db import models

   class MyData(models.Model):
       input_text = models.CharField(max_length=255)

       def __str__(self):
           return self.input_text
   ```

## Step 4: Create a Serializer

1. **Create a serializer in `myapp/serializers.py`:**
   ```python
   from rest_framework import serializers
   from .models import MyData

   class MyDataSerializer(serializers.ModelSerializer):
       class Meta:
           model = MyData
           fields = ['input_text']
   ```

## Step 5: Create an API View

1. **Define an API view in `myapp/views.py`:**
   ```python
   from rest_framework import status
   from rest_framework.decorators import api_view
   from rest_framework.response import Response
   from .models import MyData
   from .serializers import MyDataSerializer

   @api_view(['POST'])
   def save_data(request):
       if request.method == 'POST':
           serializer = MyDataSerializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   ```

## Step 6: Set Up URLs

1. **Add the API URL in `myapp/urls.py`:**
   ```python
   from django.urls import path
   from .views import save_data

   urlpatterns = [
       path('save/', save_data, name='save_data'),
   ]
   ```

2. **Include the app URLs in `myproject/urls.py`:**
   ```python
   from django.urls import path, include

   urlpatterns = [
       path('api/', include('myapp.urls')),
   ]
   ```

## Step 7: Run Migrations

1. **Run the following commands to apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

Your Django API is now ready to accept POST requests at `http://127.0.0.1:8000/api/save/` to save data in the database.

## Step 8: Enable CORS (if necessary)

1. **If you encounter CORS issues, install the CORS headers package:**
   ```bash
   pip install django-cors-headers
   ```

2. **In your `settings.py`, update the installed apps and middleware:**
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'corsheaders',
       'myapp',  # Add your app here
   ]

   MIDDLEWARE = [
       'corsheaders.middleware.CorsMiddleware',
       'django.middleware.common.CommonMiddleware',
       'django.middleware.security.SecurityMiddleware',
       'django.contrib.sessions.middleware.SessionMiddleware',
       'django.middleware.csrf.CsrfViewMiddleware',
       'django.contrib.auth.middleware.AuthenticationMiddleware',
       'django.contrib.messages.middleware.MessageMiddleware',
       'django.middleware.clickjacking.XFrameOptionsMiddleware',
   ]

   # Allow all domains to make requests
   CORS_ALLOW_ALL_ORIGINS = True
   ```

## Step 9: Check the Database

1. **Create a superuser to access the Django admin:**
   ```bash
   python manage.py createsuperuser
   ```

2. **Run your Django server and access the admin interface:**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/admin` and log in with your superuser credentials to view the saved data.

## Step 10: Retrieving Data in Your Flutter App

1. **Create a GET endpoint in your Django API to retrieve saved data:**
   ```python
   from rest_framework.views import APIView
   from rest_framework.response import Response
   from .models import MyData
   from .serializers import MyDataSerializer

   class MyDataList(APIView):
       def get(self, request):
           data = MyData.objects.all()
           serializer = MyDataSerializer(data, many=True)
           return Response(serializer.data)
   ```

2. **Add the URL for this view in `myapp/urls.py`:**
   ```python
   from .views import MyDataList

   urlpatterns = [
       path('save/', save_data, name='save_data'),
       path('data/', MyDataList.as_view(), name='data_list'),
   ]
   ```

## Optional: Admin and Data View

1. **Register the model in `myapp/admin.py`:**
   ```python
   from django.contrib import admin
   from .models import MyData

   admin.site.register(MyData)
   ```

2. **Create a view to list the saved data:**
   ```python
   from django.shortcuts import render
   from .models import MyData

   def data_list(request):
       data = MyData.objects.all()
       return render(request, 'data_list.html', {'data': data})
   ```

3. **Update `myapp/urls.py` for the data view:**
   ```python
   urlpatterns = [
       path('save/', save_data, name='save_data'),
       path('data/', data_list, name='data_list'),  # Add this line
   ]
   ```

4. **Create a template `data_list.html`:**
   ```html
   <h1>Saved Input Data</h1>
   <ul>
       {% for item in data %}
           <li>{{ item.input_text }}</li>
       {% endfor %}
   </ul>
   ```

## Final Steps

1. **Run migrations again if you added new models:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Start your server:**
   ```bash
   python manage.py runserver
   ```

---

This guide provides a clear, organized approach to setting up your Django project with the necessary configurations and steps for creating a RESTful API.













