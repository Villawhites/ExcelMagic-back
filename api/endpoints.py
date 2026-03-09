from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from schemas.schemas import ExcelRequest
from core.gemini_client import gemini_client
from services.excel_service import excel_service
import os
import uuid

router = APIRouter()

# In-memory storage for demo purposes (should be DB in production)
generated_files_map = {}

@router.post("/generate")
async def generate_excel(request: ExcelRequest):
    # 1. Ask Gemini for the structure
    structure = await gemini_client.generate_excel_structure(request.description)
    
    if "error" in structure:
        raise HTTPException(status_code=500, detail=structure["error"])

    # 2. Generate the Excel file
    file_id = str(uuid.uuid4())
    filepath = excel_service.create_excel(structure, filename_prefix="excelmagic")
    
    generated_files_map[file_id] = filepath

    return {
        "file_id": file_id,
        "structure": structure,
        "message": "Excel structure generated successfully",
        "download_url": f"/api/download/{file_id}"
    }

@router.get("/download/{file_id}")
async def download_excel(file_id: str):
    filepath = generated_files_map.get(file_id)
    if not filepath or not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(
        path=filepath,
        filename=os.path.basename(filepath),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

@router.get("/health")
async def health_check():
    return {"status": "ok"}
