# Backend-Django-Python-with-Flutter


![image](https://github.com/user-attachments/assets/f9cc1d52-8bf2-4fdc-b523-067f069fa89f)

Django Setup VScode Create Project


Step 1.1: Install Django and Django REST Framework
pip install django djangorestframework

====================================
Step 1.2: Create a Django Project
django-admin startproject myproject
cd myproject
python manage.py startapp myapp

====================================
Step 1.3: Define a Model in myapp/models.py

from django.db import models

class MyData(models.Model):
    input_text = models.CharField(max_length=255)

    def __str__(self):
        return self.input_text

====================================
Step 1.4: Create a Serializer in myapp/serializers.py

from rest_framework import serializers
from .models import MyData

class MyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyData
        fields = ['input_text']


====================================
Step 1.5: Create an API View in myapp/views.py



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



====================================

Step 1.6: Add the URL for the API in myapp/urls.py

from django.urls import path
from .views import save_data

urlpatterns = [
    path('save/', save_data, name='save_data'),
]


====================================

Step 1.7: Include the app URLs in myproject/urls.py

from django.urls import path, include

urlpatterns = [
    path('api/', include('myapp.urls')),
]

====================================

Step 1.8: Run Migrations

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Your Django API is now ready to accept POST requests at http://127.0.0.1:8000/api/save/ to save data in the database.

====================================
https://docs.djangoproject.com/en/5.1/intro/install/
Go to the main Directory

Django/
   ├── myproject/
       ├── myapp/
       ├── manage.py

cd ../../..
cd D:/7th Semester/FYP/backendDjango/Django/myproject
Step 2: Run Migrations

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

https://docs.djangoproject.com/en/5.1/ref/django-admin/#django-admin-startproject
====================================
If not working
pip install django-cors-headers

In settings.py
when you use this command then automatically
the following code will install in backend

write in cmd
D:\7th Semester\FYP\backendDjango\Django\myproject
python manage.py runserver

# Allow all domains to make requests
CORS_ALLOW_ALL_ORIGINS = True

====================================

myapp/urls.py
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    # Define the URL pattern for the API endpoint
    path('api/save/', views.save_data, name='save_data'),
]
This defines a route /api/save/ that points to the save_data view in your views.py.
====================================

Now, create the save_data view in your views.py file (in your app folder, e.g., myapp/views.py). This view will handle the POST request and save the data to the database.

Here’s a simple view that reads data from a POST request and saves it to the database:

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Import your models if you need to save to the database

@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            input_text = data.get('input_text', '')

            # You can now save this input_text to the database if needed
            # Example (if you have a model for this):
            # MyModel.objects.create(text=input_text)

            return JsonResponse({'message': 'Data saved successfully!'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

====================================

myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include the URLs from your app
]
====================================
python manage.py runserver

====================================
setting.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]


# Allow all domains to make requests
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    # Add your Flutter web app's origin if you're running it as web.
]



====================================

2. Check the Database
To check if your data is being saved, you can:

Using Django Admin


1. Ensure you have created a superuser by running:
python manage.py createsuperuser

2. Run your Django server:
python manage.py runserver

3. Navigate to http://127.0.0.1:8000/admin and log in with your superuser credentials. You should see the model you created for saving input data and be able to view the records.

Using Django Shell: You can also check your database using the Django shell.

python manage.py shell

from yourapp.models import InputText
InputText.objects.all()  # This will list all saved entries.

====================================
3. Retrieving Data in Your Flutter App

1. Create a GET endpoint in your Django API to retrieve the saved data. For example:

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InputText
from .serializers import InputTextSerializer

class InputTextList(APIView):
    def get(self, request):
        texts = InputText.objects.all()
        serializer = InputTextSerializer(texts, many=True)
        return Response(serializer.data)

====================================
Step 2: Add the InputData Model

from django.db import models

class InputData(models.Model):
    input_text = models.TextField()  # Field to store the input text
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to now when the object is created

    def __str__(self):
        return self.input_text  # Return the input text when the object is printed

====================================
python manage.py makemigrations
python manage.py migrate
====================================
Step 4: Register the Model in Django Admin (Optional)

Open the admin.py file located in the same app directory (myapp/admin.py).

from django.contrib import admin
from .models import InputData  # Import your model

admin.site.register(InputData)  # Register the model with the admin site
====================================

Step 5: Create a View to Access the Data (Optional)
1. Create a View: In your views.py, create a view function:

from django.shortcuts import render
from .models import InputData

def data_list(request):
    data = InputData.objects.all()  # Get all saved input data
    return render(request, 'data_list.html', {'data': data})  # Pass data to template

2. Create a Template: Create a template file named data_list.html in your templates directory:

<h1>Saved Input Data</h1>
<ul>
    {% for item in data %}
        <li>{{ item.input_text }} - {{ item.created_at }}</li>
    {% endfor %}
</ul>

3. Add URL for the View: In urls.py, add the path for the view:

from django.urls import path
from .views import data_list

urlpatterns = [
    path('data/', data_list, name='data_list'),
]

====================================
Step 6: Access the Data

Django Admin: Log in to your Django admin at http://127.0.0.1:8000/admin/ to view, edit, or delete input data.
Custom View: Navigate to http://127.0.0.1:8000/data/ to see the list of saved input data.

====================================
settings.py
myproject/myproject/settings.py
Add another line 

'myapp',  # Make sure this line is present

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'myapp',  # Make sure this line is present

]

====================================
view.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import InputData  # Import your model

@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            input_text = data.get('input_text', '')

            if not input_text:
                return JsonResponse({'error': 'No input text provided'}, status=400)

            # Save the input data to the database
            InputData.objects.create(input_text=input_text)

            return JsonResponse({'message': 'Data saved successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def data_list(request):
    data = InputData.objects.all()  # Get all saved input data
    return render(request, 'data_list.html', {'data': data})  # Pass data to template





python manage.py makemigrations
python manage.py migrate
python manage.py runserver



python manage.py dbshell



















