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


print()

# Display books by genre

def displayBooksByGenre(selection):
    print("--Select one of the following genres to see books--- ")
    genres = db.books.distinct("genre")
    for genre in genres:
        print(genre)    
        if selection == genre:
            books = db.books.find({"genre": selection})
            print(f"\n ---Displaying books by the genre: {selection}--- \n")
            for book in books:
                print(f"{book['title']} by {book['author']} \n Details: \n  Genre: {book['genre']} \n  bookId: {book['bookId']} \n")

print(displayBooksByGenre("Fantasy"))

def display_wishlist_by_customerid(customer_Id):
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
                print(f"{book['title']} by {book['author']} \n ")
    else:
        print("Invalid, this customerId does not exist in our system. Please try again.")
        
   
print(display_wishlist_by_customerid("0004"))
        
    


                





