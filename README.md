# Thai ID OCR App

This project is a Thai ID OCR (Optical Character Recognition) application that extracts information from Thai ID cards using Google Vision API for OCR processing. The extracted data is stored in a MongoDB database, and the application provides a set of REST API endpoints for CRUD operations on OCR records.

## Setup
For frontend you can visit templates folder in my repository-
https://github.com/luck2406/Thai-ID-OCR-App


### Prerequisites

- Python 3.x
- pip
- virtualenv (recommended)

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/<username>/thai-id-ocr.git
   ```
2. Navigate into the project directory
   ```bash
   cd thai-id-ocr
   ```
3. Create and activate a virtual environment 
   ```bash
   virtualenv env
   source env/bin/activate
   ```
4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
5. Configure environment variables
   ```bash
   # In .env file
   export GOOGLE_VISION_API_KEY=<your_api_key>
   export MONGODB_URI=<your_mongodb_uri>
   ```
6. Run migrations
   ```bash
   python manage.py migrate
   ```
7. Start development server
   ```bash
   python manage.py runserver
   ```
   
The app will be served at `http://127.0.0.1:8000`

## Dependencies

- Django
- Djongo
- google-cloud-vision
- Pillow
- python-dotenv

## Architecture

The app follows a simple Model-View-Controller architecture with the following components:

**Models**

- `OCRRecord` - Stores extracted Thai ID data

**Views** 

- `create_ocr_record` - Processes image and extracts data
- `get_ocr_records` - Returns paginated list of OCR records
- `update_ocr_record` - Updates a record  
- `delete_ocr_record` - Soft deletes a record

**Controller**

- `ocr_app/urls.py` - Maps endpoints to views

**Utils**

- `ocr.py` - Optical character recognition helper using Google Vision API
- `extract.py` - Parses OCR results and extracts structured fields
 
