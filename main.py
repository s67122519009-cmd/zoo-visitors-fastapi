
from pathlib import Path
from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI(
    title="Zoo Visitors API",
    description="ข้อมูลผู้เข้าชมสวนสัตว์ ปีงบประมาณ 2569",
    version="1.0.0"
)

DATASET_URL = "https://data.go.th/dataset/zoo-visitors2569"
EXCEL_FILE = Path(__file__).resolve().parent / "zoo_visitors.xlsx"


@app.get("/")
def home():
    return {
        "message": "Zoo Visitors API is running",
        "docs": "/docs"
    }



@app.get("/api/zoo-visitors")
def get_zoo_visitors():

    if not EXCEL_FILE.exists():
        raise HTTPException(
            status_code=404,
            detail="ไม่พบไฟล์ zoo_visitors.xlsx"
        )

    try:
        df = pd.read_excel(
            EXCEL_FILE,
            dtype=str,
            keep_default_na=False
        )
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"อ่านไฟล์ Excel ไม่สำเร็จ: {error}"
        )

    # ใช้ชื่อคอลัมน์ที่มีอยู่ใน Excel จริง
    df.columns = [str(col).strip() for col in df.columns]

    # ลบแถวว่างทั้งหมด
    df = df[
        df.astype(str)
        .apply(lambda col: col.str.strip())
        .ne("")
        .any(axis=1)
    ]

    records = df.to_dict(orient="records")

    if not records:
        raise HTTPException(
            status_code=422,
            detail="ไม่พบข้อมูลในไฟล์ Excel"
        )

    return {
        "dataset": "zoo-visitors2569",
        "fiscal_year": 2569,
        "source": "https://data.go.th/dataset/zoo-visitors2569",
        "resource_name": "รายงานผู้เข้าชมสวนสัตว์ กันยายน 2569",
        "total_records": len(records),
        "data": records
    }

