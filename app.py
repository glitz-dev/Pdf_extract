from fastapi import FastAPI
import PyPDF2
from hipaathesis import analyze as hipaa_analyze, AnalyzeReq
# import your other modules as needed

app = FastAPI(title="HIPAA Thesis App")

# Endpoint for Main page
@app.get("/")
def home():
    return {"message": "HIPAA Thesis App is running"}

# Endpoint for processing PDF 
@app.post("/analyze")
def analyze(req: AnalyzeReq):
    return hipaa_analyze(req)