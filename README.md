Welcome to BookCrud! This is a simple CRUD (Create, Read, Update, Delete) application built using Django and MySQL (XAMPP). BookCrud allows you to manage a collection of books by adding, updating, and deleting book entries.

Technologies Used: Django MySQL (XAMPP)

Features: Add books with title, author, and price information. Update book information such as title, author, and price. Delete books from the collection.

Getting Started To get started with BookCrud, follow these steps:

Clone the repository: git clone https://github.com/your-username/BookCrud.git

Install dependencies: pip install -r requirements.txt

Set up MySQL database: Install XAMPP and start the MySQL services. Create a new MySQL database for BookCrud.

Configure settings: In BookCrud/settings.py, update the DATABASES configuration to connect to your MySQL database. Run migrations:

python manage.py makemigrations python manage.py migrate

Run the development server: python manage.py runserver

Usage Adding a Book: Navigate to the "Add Book" page. Enter the title, author, and price of the book. Click the "Submit" button to add the book to the collection.

Updating Book Information: Navigate to the "Home" page for the book you want to update. Click on update Modify the title, author, or price as needed. Click the "Update" button to save the changes.

Deleting a Book: Navigate to the "home" page for the book you want to delete. Confirm the deletion by clicking the "Delete" button.

Home Page:
![Screenshot 2024-02-06 192636](https://github.com/Rushikeshthokale/BookCrud/assets/87907210/55669d44-1835-4ce3-b368-72fb5054c9c9)


AddBook page:

![Screenshot 2024-02-06 192646](https://github.com/Rushikeshthokale/BookCrud/assets/87907210/c700b58a-629d-493b-9c82-1fc43d31fb92)

UpdateBook Page: 
![Screenshot 2024-02-06 192656](https://github.com/Rushikeshthokale/BookCrud/assets/87907210/60e5c898-49eb-4981-b2a6-c16eecf06868)
