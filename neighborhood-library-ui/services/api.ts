
const API_URL = "http://localhost:8000";

export async function createBook(book:any) {
  const res = await fetch(`${API_URL}/books`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(book)
  });
  return res.json();
}

export async function getBooks() {
  const res = await fetch(`${API_URL}/books`);
  return res.json();
}

export async function borrowBook(data:any) {
  const res = await fetch(`${API_URL}/borrowings`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  return res.json();
}
