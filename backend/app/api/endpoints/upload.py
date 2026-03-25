from fastapi import APIRouter, UploadFile, File
import os
from app.services.pdf_service import extract_text_from_pdf
from app.services.text_splitter import split_text
from app.services.vector_service import save_to_vector_db


router = APIRouter()

UPLOAD_DIR = "app/uploads"

@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # 파일 저장
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # 텍스트 추출
    text = extract_text_from_pdf(file_path)

    # 텍스트 쪼개기
    chunks = split_text(text)

    # 벡터 DB 저장
    save_to_vector_db(chunks)

    return {
        "filename": file.filename,
        "text_preview": text[:300]
    }