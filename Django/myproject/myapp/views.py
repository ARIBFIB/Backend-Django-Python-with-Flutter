# myapp/views.py
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import InputData
from .serializers import InputDataSerializer
from django.shortcuts import render


@api_view(['POST'])
def save_data(request):
    if request.method == 'POST':
        serializer = InputDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Data saved successfully!'}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def input_form(request):
    # Your logic for rendering the input form goes here
    return render(request, 'input_form.html')  # Ensure this template exists