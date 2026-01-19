
import { useEffect, useState } from "react";
import { getBooks, borrowBook } from "../services/api";

export default function Books() {
  const [books, setBooks] = useState<any[]>([]);

  useEffect(() => {
    getBooks().then(setBooks);
  }, []);

  const borrow = (id:number) => {
    borrowBook({ book_id: id, member_id: 1 })
      .then(alert);
  };

  return (
    <div>
      <h2>Books</h2>
      <ul>
        {books.map(b => (
          <li key={b.id}>
            {b.title} – {b.author}
            <button onClick={() => borrow(b.id)}>Borrow</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
