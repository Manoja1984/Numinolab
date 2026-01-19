# Numinolab
neighborhood-library-app/
│
├── backend/
│   ├── app/
│   │   ├── main.py              
│   │   ├── config.py            
│   │   ├── database.py         
│   │   ├── models.py            
│   │   ├── schemas.py           
│   │   ├── crud.py             
│   │   ├── routes/
│   │   │   ├── books.py
│   │   │   ├── members.py
│   │   │   └── borrowings.py
│   │   └── __init__.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── alembic/                 
│
├── frontend/
│   ├── pages/
│   │   ├── index.tsx
│   │   ├── books.tsx
│   │   └── members.tsx
│   ├── components/
│   │   ├── BookList.tsx
│   │   └── BorrowForm.tsx
│   ├── services/
│   │   └── api.ts
│   ├── package.json
│   └── next.config.js
│
├── db/
│   ├── init.sql                 
│   └── seed.sql                 
│
├── docker-compose.yml
├── README.md
└── .env.example

## Neighborhood Library Service

### Tech Stack
- Python (FastAPI)
- PostgreSQL
- Next.js (React)
- Docker & Docker Compose

### Run Locally
```bash
docker-compose up --build
## Error Handling & Validation

- A book cannot be borrowed if it is already checked out.
- Input validation is enforced using Pydantic.
- Database-level constraints prevent inconsistent states.

### Common Errors
| Status | Reason |
|------|-------|
| 400 | Book already checked out |
| 422 | Invalid input payload |
| 404 | Resource not found |
