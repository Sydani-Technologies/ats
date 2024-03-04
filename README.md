# Application Tracking System Using Langchain and CrewAi

## Setup

Clone the repo and cd into the project folder

### Follow the instruction

1. Create python virtual environment `python -m venv .venv` and activate it using `.venv/Scripts/Activate`

2. Install the dependencies cd into the backend folder and run `pip install -r requirements.txt`

3. Run: `uvicorn main:app --reload` this will run the app on localhost port 8000

4. Use Postman or any other API testing platform send a post request with raw data to
  url: `http://127.0.0.1:8000/screen` raw-data: `{"cv_url": "CV URL From ERP", "criteria": "Job requirement from ERP"}`
  