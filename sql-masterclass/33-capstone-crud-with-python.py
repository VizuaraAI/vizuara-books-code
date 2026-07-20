"""
SQL Masterclass
Chapter 33: Capstone: CRUD Operations from Python
Section: Capstone and Interview Prep

Read this chapter: https://books.vizuara.ai/read/sql-masterclass/capstone-crud-with-python

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import psycopg2

conn = psycopg2.connect(
    host="localhost", dbname="library",
    user="postgres", password="your_password", port=5432,
)

def add_book(title, author):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO books (title, author) VALUES (%s, %s) RETURNING book_id;",
            (title, author),
        )
        new_id = cur.fetchone()[0]
    conn.commit()
    return new_id

# --- block 2 ---
def available_books():
    with conn.cursor() as cur:
        cur.execute(
            "SELECT book_id, title, author FROM books WHERE available = TRUE ORDER BY title;"
        )
        return cur.fetchall()

# --- block 3 ---
def issue_book(book_id, member_id):
    with conn.cursor() as cur:
        try:
            cur.execute(
                "INSERT INTO transactions (book_id, member_id) VALUES (%s, %s);",
                (book_id, member_id),
            )
            cur.execute(
                "UPDATE books SET available = FALSE WHERE book_id = %s;",
                (book_id,),
            )
            conn.commit()          # both writes land together
        except Exception:
            conn.rollback()        # or neither does
            raise

# --- block 4 ---
def return_book(book_id):
    with conn.cursor() as cur:
        try:
            cur.execute(
                "UPDATE transactions SET returned_on = CURRENT_DATE "
                "WHERE book_id = %s AND returned_on IS NULL;",
                (book_id,),
            )
            cur.execute(
                "UPDATE books SET available = TRUE WHERE book_id = %s;",
                (book_id,),
            )
            conn.commit()
        except Exception:
            conn.rollback()
            raise

# --- block 5 ---
def currently_issued():
    with conn.cursor() as cur:
        cur.execute("""
            SELECT b.title, m.name, t.issued_on
            FROM transactions t
            JOIN books   b ON b.book_id   = t.book_id
            JOIN members m ON m.member_id = t.member_id
            WHERE t.returned_on IS NULL
            ORDER BY t.issued_on;
        """)
        return cur.fetchall()
