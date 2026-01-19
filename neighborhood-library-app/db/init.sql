
CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT);
CREATE TABLE members (id INTEGER PRIMARY KEY, name TEXT, email TEXT);
CREATE TABLE borrowings (
    id INTEGER PRIMARY KEY,
    book_id INTEGER,
    member_id INTEGER,
    borrowed_at DATE,
    returned_at DATE
);
