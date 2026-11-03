# Zoo Visitors API — Fiscal Year 2569

RESTful API developed with Python and FastAPI using official open government data from Data.go.th.

## Project Information

- Dataset: zoo-visitors2569
- Fiscal Year: 2569
- Data Provider: องค์การสวนสัตว์แห่งประเทศไทย ในพระบรมราชูปถัมภ์
- Source: https://data.go.th/dataset/zoo-visitors2569
- Data Format: XLSX
- API Response: JSON
- Deployment: Render

## API Endpoints

**GET /api/zoo-visitors**

https://zoo-visitors-fastapi-8549.onrender.com/api/zoo-visitors

**Swagger UI /docs**

https://zoo-visitors-fastapi-8549.onrender.com/docs

## Technologies

- Python
- FastAPI
- Pandas
- OpenPyXL
- Postman
- Render
- GitHub

## API Test Results

- HTTP Method: GET
- Status Code: 200 OK
- Response Type: application/json
- Fiscal Year: 2569
- Total Records: 63

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

http://127.0.0.1:8000/docs

## Postman Testing

Screenshot: [View Postman Test](postman-render-test.png)

## Data Source

ข้อมูลรายงานสถิติจำนวนผู้เข้าชมสวนสัตว์ ปีงบประมาณ 2569 จากองค์การสวนสัตว์แห่งประเทศไทย ในพระบรมราชูปถัมภ์ ผ่าน Data.go.th

All visitor statistics are read from the official XLSX resource, not generated as sample data.
