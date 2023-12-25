"""ocr_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from ocr_app.views import create_ocr_record, get_ocr_records, update_ocr_record, delete_ocr_record

urlpatterns = [
    path('api/ocr/', create_ocr_record, name='create_ocr_record'),
    path('api/ocr/', get_ocr_records, name='get_ocr_records'),
    path('api/ocr/<str:record_id>/', update_ocr_record, name='update_ocr_record'),
    path('api/ocr/<str:record_id>/', delete_ocr_record, name='delete_ocr_record'),
    # Add other CRUD endpoints as needed
]
