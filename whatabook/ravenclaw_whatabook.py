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
def display_books(books):
    for book in books:
        print(f"{book['title']} by {book['author']} \n Details: \n  Genre: {book['genre']} \n  bookId: {book['bookId']} \n")

print("---Displaying all books in What-A-Book's collection--- \n")
display_books(db.books.find({}))

# Display books by genre

def display_books_by_genre(selection):
    print("--Select one of the following genres to see books--- ")
    genres = db.books.distinct("genre")
    for genre in genres:
        print(genre)    
    print(f"\n ---Displaying books by the genre: {selection}--- \n")
    display_books(db.books.find({"genre": selection}))

display_books_by_genre("Fantasy")

# Display books by author

def display_books_by_author(selection):
    print("--Select one of the following authors to see books--- ")
    authors = db.books.distinct("author")
    for author in authors:
        print(author)    
    print(f"\n ---Displaying books by the author: {selection}--- \n")
    display_books(db.books.find({"author": selection}))

display_books_by_author("JK Rowling")

# Display books by bookId

def display_books_by_book_id(book_id):
    print(f"\n ---Displaying books by the bookId: {book_id}--- \n")
    display_books(db.books.find({"bookId": book_id}))

display_books_by_book_id("R001")

# Display books in wishlist by customerId
def display_wishlist_by_customer_id(customer_Id):
    print("Enter your customerId to view your wishlist \n")
    customer = db.customers.find_one({"customerId": customer_Id})
    if customer:
        wishlist = db.wishlists.find_one({"customerId": customer_Id}, {"_id": 0, "wishlistbooks": 1})
        wishlist_items = wishlist["wishlistbooks"]
        customer_name = customer["firstName"]
        print(f"----Displaying books in {customer_name}'s Wishlist: --- \n ")
        for items in wishlist_items:
            book_id = items['bookId']
            details = db.books.find({"bookId": book_id})
            for book in details:
                print(f"* {book['title']} \n    by {book['author']} \n ")
    else:
        print("Invalid, this customerId does not exist in our system. Please try again.")
        
   
display_wishlist_by_customer_id("0004")
        
# Add books to a customer's wishlist
def add_wishlist_book_by_customer_id(customer_id):
    print("Select a book to add your wishlist \n")
    display_books(db.books.find({}))
    customer = db.customers.find_one({"customerId": customer_id})
    if customer:
        db.wishlists.update_one({"customerId": customer_id},  { "$addToSet": {
            "wishlistbooks": {
                "bookId": "R001"
            }
        }})
    else:
        print("Invalid, this customerId does not exist in our system. Please try again.")
        
   
add_wishlist_book_by_customer_id("0004")


# Remove book from a customer's wishlist    
def remove_wishlist_book_by_customer_id(customer_id):
    print("Select a book to add your wishlist \n")
    display_books(db.books.find({}))
    customer = db.customers.find_one({"customerId": customer_id})
    if customer:
        db.wishlists.update_one({"customerId": customer_id},  { "$pull": {
            "wishlistbooks": {
                "bookId": { "$eq": "R001" }
            }
        }})
    else:
        print("Invalid, this customerId does not exist in our system. Please try again.")

   
remove_wishlist_book_by_customer_id("0004")


                





