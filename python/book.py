books=[]

for i in range(3):
    book=dict()
    book["author"]=input("enter author name: ")
    book["title"]=input("enter title of book: ")
    books.append(book)

for book in books:
    print(f"{book["author"]} wrote {book["title"]}")