import base64
from google.cloud import vision
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import OCRRecord
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import get_object_or_404


@csrf_exempt
def create_ocr_record(request):
    if request.method == 'POST':
        try:
            # Extract image content from the request
            image_content = request.FILES['image'].read()

            # Process image using Google Vision API
            # (Rest of the code remains the same)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    

def get_ocr_records(request):
    if request.method == 'GET':
        # Implement logic to fetch OCR records from the database
        # You can add filters based on date, status, etc.
        # Return the records in JSON format
        records = OCRRecord.objects.all().values()
        return JsonResponse({"records": list(records)})
    
def update_ocr_record(request, record_id):
    if request.method == 'PUT':
        try:
            # Extract updated information from the request
            # Modify the logic based on the fields you want to update
            name = request.POST.get('name')
            last_name = request.POST.get('last_name')
            date_of_birth = request.POST.get('date_of_birth')
            date_of_issue = request.POST.get('date_of_issue')
            date_of_expiry = request.POST.get('date_of_expiry')

            # Retrieve the OCR record to update
            ocr_record = get_object_or_404(OCRRecord, pk=record_id)

            # Update the fields
            ocr_record.name = name
            ocr_record.last_name = last_name
            ocr_record.date_of_birth = date_of_birth
            ocr_record.date_of_issue = date_of_issue
            ocr_record.date_of_expiry = date_of_expiry

            # Save the updated record
            ocr_record.save()

            return JsonResponse({
                "status": "success",
                "message": f"OCR record {record_id} updated successfully",
            })
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

def delete_ocr_record(request, record_id):
    if request.method == 'DELETE':
        try:
            # Retrieve the OCR record to delete
            ocr_record = get_object_or_404(OCRRecord, pk=record_id)

            # Soft delete the record (set a flag, don't actually delete from the database)
            ocr_record.delete()

            return JsonResponse({
                "status": "success",
                "message": f"OCR record {record_id} deleted successfully",
            })
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})