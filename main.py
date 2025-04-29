from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [{"title": "book one", "category": "Math", "author": "Mohamad"},
         {"title": "book two", "category": "Science", "author": "Mohamad2"},
         {"title": "book three", "category": "Math", "author": "Mohamad3"},]


@app.get("/books")
async def root():
    return BOOKS

@app.get("/books/{title}")
async def get_book_by_book_title(title: str):
    for book in BOOKS:
        if book["title"] == title:
            return book
@app.get("/books/author/{author}")
async def get_book_by_author(author: str):
    final_books = []
    for book in BOOKS:
        if book["author"] == author:
            final_books.append(book)
    return final_books
@app.get("/books/")
async def get_books_query_by_category(category: str):
    final_books = []
    for book in BOOKS:
        if book["category"] == category:
            final_books.append(book)
    return final_books


@app.get("/books/{book_author}/")
async def get_book_by_author(book_author: str, category: str):
    final_books = []
    for book in BOOKS:
        if book["author"] == book_author and book.get("category") == category:
            final_books.append(book)
    return final_books


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if  BOOKS[i]["title"] == update_book["title"]:
            BOOKS[i] = update_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"] == book_title:
            BOOKS.pop(i)
            break