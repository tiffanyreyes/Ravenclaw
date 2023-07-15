""" 
    Title: ravenclaw_whatabook.py
    Author: Hannah Del Real and Tiffany Reyes
    Date: 14 July 2023
    Description: Connecting Python with What-a-Book database on MongoDB
"""

# Import mongoDBClient
from pymongo import MongoClient

# Create a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.ozktyyu.mongodb.net/web335DBretryWrites=true&w=majority")

# Assign web335 database to variable db
db = client['web335DB']

# Create space between outputs
print("\n")


# Call the find function to display all books in the collection
def display_books():
    for book in db.books.find({}):
        print(f"{book['title']} by {book['author']} \n Details: \n  Genre: {book['genre']} \n  bookId: {book['bookId']} \n")

print("---Displaying all books in What-A-Book's collection--- \n")
print(display_books())


print("---See books by any of the following genres---")
genres = db.books.distinct("genre")
for genre in genres:
    print(genre)
    
print()


for genre in genres:
    print(f"Displaying books by the genre: {genre} \n")
    books = db.books.find({"genre": genre})
    for book in books:
        print(f"{book['title']} by {book['author']} \n Details: \n  Genre: {book['genre']} \n  bookId: {book['bookId']} \n")

