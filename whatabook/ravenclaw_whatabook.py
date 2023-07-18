""" 
    Title: ravenclaw_whatabook.py
    Author: Hannah Del Real and Tiffany Reyes
    Date: 14 July 2023
    Description: Connecting Python with What-a-Book database on MongoDB
"""

# Import MongoDBClient
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

def display_books_by_genre():
    print("--Select one of the following genres to see books--- \n")
    genres = db.books.distinct("genre")
    for genre in genres:
        print(genre)
    selection = input("\n ---Enter a genre:--- \n")
    if selection in genres:
        print(f"\n ---Displaying books by the genre: {selection}--- \n")
        display_books(db.books.find({"genre": selection}))
    else:
        print("\n Invalid, this genre does not exist in our system. Please try again. \n")    

display_books_by_genre()

# Display books by author

def display_books_by_author():
    print("--Select one of the following authors to see books--- \n")
    authors = db.books.distinct("author")
    for author in authors:
        print(author)    
    selection = input("\n ---Enter an author:--- \n")
    if selection in authors:
        print(f"\n ---Displaying books by the author: {selection}--- \n")
        display_books(db.books.find({"author": selection}))
    else:
        print("\n Invalid, this author does not exist in our system. Please try again. \n")    

display_books_by_author()

# Display books by bookId

def display_books_by_book_id():
    book_ids = db.books.distinct("bookId")
    selection = input("\n ---Enter a bookId to see book details:--- \n")
    if selection in book_ids:
        print(f"\n ---Displaying book by the bookId: {selection}--- \n")
        display_books(db.books.find({"bookId": selection}))
    else:
        print("\n Invalid, this bookId does not exist in our system. Please try again. \n")  
    
display_books_by_book_id()

# Display books in wishlist by customerId

def display_wishlist_by_customer_id():
    customer_ids = db.customers.distinct("customerId")
    selection = input("\n ---Enter your customerId to view your wishlist:--- \n")
    if selection in customer_ids:
        customer = db.customers.find_one({"customerId": selection})
        wishlist = db.wishlists.find_one({"customerId": selection}, {"_id": 0, "wishlistbooks": 1})
        wishlist_items = wishlist["wishlistbooks"]
        customer_name = customer["firstName"]
        print(f" \n ---Displaying books in {customer_name}'s Wishlist: --- \n ")
        for items in wishlist_items:
            book_id = items['bookId']
            details = db.books.find({"bookId": book_id})
            for book in details:
                print(f"* {book['title']} \n    by {book['author']} \n ")
    else:
        print("\n Invalid, this bookId does not exist in our system. Please try again. \n")  
   
display_wishlist_by_customer_id()
        
# Add books to a customer's wishlist

def add_wishlist_book_by_customer_id():
    print("\n---Add a book to a customer's wishlist---\n")
    customer_ids = db.customers.distinct("customerId")
    customer_selection = input("\n---Enter a customerId:---\n")
    if customer_selection in customer_ids:
        book_ids = db.books.distinct("bookId")
        book_selection = input("\n---Enter a bookId to add to your wishlist:---\n")
        if book_selection in book_ids:
            db.wishlists.update_one(
                { "customerId": customer_selection },
                { "$addToSet": { "wishlistbooks": { "bookId": book_selection } } }
            )
        else:
            print("Invalid, this bookId does not exist in our system. Please try again.")
    else:
        print("Invalid, this customerId does not exist in our system. Please try again.")
        
   
add_wishlist_book_by_customer_id()

# Remove book from a customer's wishlist

def remove_wishlist_book_by_customer_id():
    print("\n---Remove a book from a customer's wishlist---\n")
    customer_ids = db.customers.distinct("customerId")
    customer_selection = input("\n---Enter a customerId:---\n")
    if customer_selection in customer_ids:
        # Find all book ids in the customer's wishlist
        wishlist = db.wishlists.find_one({"customerId": customer_selection})
        wishlistbooks = wishlist["wishlistbooks"]
        wishlistbook_ids = [wishlistbook['bookId'] for wishlistbook in wishlistbooks]

        # Find customer's name
        customer = db.customers.find_one({"customerId": customer_selection})
        customer_name = customer["firstName"]

        book_selection = input(f"\n---Enter a bookId to remove from {customer_name}'s wishlist:---\n")
        if book_selection in wishlistbook_ids:
            db.wishlists.update_one({"customerId": customer_selection},  { "$pull": {
                "wishlistbooks": {
                    "bookId": { "$eq": book_selection }
                }
            }})
        else:
            print("Invalid, this bookId does not exist in our system. Please try again.")
    else:
        print("Invalid, this customerId does not exist in our system. Please try again.")
   
remove_wishlist_book_by_customer_id()


                





