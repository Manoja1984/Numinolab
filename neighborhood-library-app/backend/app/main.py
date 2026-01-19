
from fastapi import FastAPI
from app.routes import books, members, borrowings

app = FastAPI(title="Neighborhood Library Service")

app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(members.router, prefix="/members", tags=["Members"])
app.include_router(borrowings.router, prefix="/borrowings", tags=["Borrowings"])
