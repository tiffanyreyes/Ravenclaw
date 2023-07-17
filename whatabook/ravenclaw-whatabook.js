/*
===========================================================================================
; Title: ravenclaw-whatabook.js
; Author: Tiffany Reyes and Hannah Del Real
; Date: 11 July 2023
; Description: WhatABook queries
;==========================================================================================
*/

// Delete the books, customers, and wishlists collections.
db.books.drop();
db.customers.drop();
db.wishlists.drop();

// Create the books, customers, and wishlists collections.
db.createCollection("books", {
	validator: { $jsonSchema: {
		bsonType: "object",
        required: ["title", "author", "genre", "bookId"],
		properties: {
			title: {
				bsonType: "string"
			},
			author: {
				bsonType: "string"
			},
            genre: {
				bsonType: "string"
			},
			bookId: {
				bsonType: "string"
			}
		}
	}}
});

db.createCollection("customers", {
	validator: { $jsonSchema: {
		bsonType: "object",
        required: ["customerId", "firstName", "lastName"],
		properties: {
			customerId: {
				bsonType: "string"
			},
			firstName: {
				bsonType: "string"
			},
            lastName: {
				bsonType: "string"
			}
		}
	}}
});

db.createCollection("wishlists", {
	validator: { $jsonSchema: {
		bsonType: "object",
        required: ["wishlistId", "customerId", "wishlistbooks"],
		properties: {
            wishlistId: {
				bsonType: "string"
			},
            customerId: {
				bsonType: "string"
			},
			wishlistbooks: {
				bsonType: "array"
			}
		}
	}}
});

// Books
let book1 = {
    "title": "Pride and Prejudice",
    "author": "Jane Austin",
    "genre": "Romance",
    "bookId": "R001"
};

let book2 = {
    "title": "Harry Potter and the Prisoner of Azakaban",
    "author": "JK Rowling",
    "genre": "Fantasy",
    "bookId": "F003"
};

let book3 = {
    "title": "Harry Potter and the Goblet of Fire",
    "author": "JK Rowling",
    "genre": "Fantasy",
    "bookId": "F004"
};

// Insert book documents
db.books.insertOne(book1);
db.books.insertOne(book2);
db.books.insertOne(book3);

// Customers
let customer1 = {
    "customerId": "0003",
    "firstName": "Mina",
    "lastName": "Myoi"
};

let customer2 = {
    "customerId": "0004",
    "firstName": "Jihyo",
    "lastName": "Park"
};

// Insert customer documents
db.customers.insertOne(customer1);
db.customers.insertOne(customer2);

// Wishlists
let wishlist1 = {
    "wishlistId": "10001",
    "customerId": "0004",
    "wishlistbooks": [
        {
            "bookId": "F003"
        },
        {
            "bookId": "F004"
        }
    ]
};

let wishlist2 = {
    "wishlistId": "10000",
    "customerId": "0003",
    "wishlistbooks": [
        {
            "bookId": "R001"
        },
        {
            "bookId": "F003"
        }
    ]
};


// Insert wishlists documents
db.wishlists.insertOne(wishlist1);
db.wishlists.insertOne(wishlist2);

// Query to display list of books
db.books.find();

// Query to display list of books by genre
db.books.find( { "genre": "Fantasy" } );

// Query to display a list of books by author
db.books.find( { "author": "Jane Austin" } );

// Query to display a book by bookId
db.books.find( { "bookId": "R001" } );

// Query to display a wishlist by customerId
db.wishlists.find( { "customerId": "0004" } );

// Query to add a book to customer's wishlist
db.wishlist.updateOne(
    { "customerId": "0004" },
    { "$addToSet": {
        wishlist: {
            "title": "Scythe",
            "author": "Neal Shusterman",
            "genre": "Fantasy",
            "bookId": "F005"
        }
    }}
);

// Query to remove a book from customer's wishlist
db.wishlist.updateOne(
    { "customerId": "0004" },
    { "$pull": {
        wishlistbooks: { "bookId": { $eq: "F005" } }
    }
}
);
