#!/usr/bin/env python
# coding: utf-8

# In[1]:


class LMS:
    login_heading: str="Welcome to Library Managment System"
    print(f'{login_heading:-^50}\n')

    def __init__(self,price):
        self.__price=price

    def get_price(self):
        return self.__price

    def set_price(self,price):
        self.__price=price
        
    def additional_info(self):
        print("We are best Programmer")

class Book(LMS):
    """
    Book class is responsible for creating book objects.
    It also has methods to check if a book is available, update
    """
    def __init__(self, price, title, author, genre, year_of_publish, isbn,pages,copies):
        super().__init__(price)
        self.title = title
        self.author = author
        self.genre = genre
        self.year_of_publish = year_of_publish
        self.isbn = isbn
        self.pages = pages
        self.copies = copies

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Year_of_publish: {self.year_of_publish}")
        print(f"ISBN: {self.isbn}")
        print(f"pages: {self.pages}")
        print(f"copies: {self.copies}")

class Magzine(LMS):
    def __init__(self, price, title, author, genre, year_of_publish, isbn,pages,copies):
        super().__init__(price)
        self.title = title
        self.author = author
        self.genre = genre
        self.year_of_publish = year_of_publish
        self.isbn = isbn
        self.pages = pages
        self.copies = copies
        
        

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Year_of_publish: {self.year_of_publish}")
        print(f"ISBN: {self.isbn}")
        print(f"pages: {self.pages}")
        print(f"copies: {self.copies}")
        

class Novel(LMS):
    def __init__(self, price, title, author, genre, year_of_publish, isbn,pages,copies):
        super().__init__(price)
        self.title = title
        self.author = author
        self.genre = genre
        self.year_of_publish = year_of_publish
        self.isbn = isbn
        self.pages = pages
        self.copies = copies

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Year_of_publish: {self.year_of_publish}")
        print(f"ISBN: {self.isbn}")
        print(f"pages: {self.pages}")
        print(f"copies: {self.copies}")
        
class Reference_book(LMS):
    def __init__(self, price, title, author, genre, year_of_publish, isbn,pages,copies):
        super().__init__(price)
        self.title = title
        self.author = author
        self.genre = genre
        self.year_of_publish = year_of_publish
        self.isbn = isbn
        self.pages = pages
        self.copies = copies
      

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Year_of_publish: {self.year_of_publish}")
        print(f"ISBN: {self.isbn}")
        print(f"pages: {self.pages}")
        print(f"copies: {self.copies}")
        
    def additional_info(self):
        print("Visit us Again!")
        
import csv#we have created the csv file in our pc and import it to read the info of book in lms project
file_path=r"/Users/fajarfatima/Desktop/add_book.py.csv"
def information_of_csv(file_path):
    with open(file_path, mode="r") as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader, None)#code to not show the data when csv import in project

        book_info = 0#instead of showing data of books we can show the total books in project
        for row in csv_reader:#to read the books
            book_info += 1 #by using increment we can count the total books in csv 

        return book_info

#now we can tell how many books we have in project 
book_info = information_of_csv(file_path)
print(f"Total number of books which are available in our Library: {book_info}")

             
class UserInformation(LMS):
    def __init__(self,name,age,gender,issue_date,type_of_book):
        self._name = name
        self._age = age
        self._gender = gender
        self._issue_date = issue_date
        self._type_of_book = type_of_book
        
    def get_name(self):
        return self._name
    def  get_age(self):
        return self._age
    def get_gender(self):
        return self._gender
    def get_issue_date(self):
        return self._issue_date
    def get_type_of_book(self):
        return self._type_of_book
    def set_name(self,name):
        self._name = name
    def set_age(self,age):
        self._age = age
    def set_gender(self,gender):
        self._gender = gender
    def set_issue_date(self,issue_date):
        self._issue_date = issue_date
    def set_type_of_book(self,type_of_book):
        self._type_of_book = type_of_book
#we don't use get set method directly we use input method to store data in csv file 

# now to make a csv file and to stored data of user 
import csv 
name=input("Enter your Name: ")
age=input("Enter your Age: ")
your_roll=input("Enter your Roll(Student/Teacher): ")
issue_date =input("Enter Today's Date(DD/MM/YYYY): ")
issue_date.split("/")
gender =input("Enter your Gender (M/F): ")
import pandas as pd
import csv
with open("Main1_register.py.csv","w+")as file:
    myfile=csv.writer(file)
    myfile.writerow(["Name","Age","Your_roll","Issue_Date","Gender"])
    myfile.writerow([name,age,your_roll,issue_date,gender])

    def information_of_book():
        file_path==r"/Users/fajarfatima/Desktop/add_book.py.csv"
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            books = [row for row in csv_reader]
            

    
books_categories={
            "Books": [
                "To Kill a Mockingbird" , "The Great Gatsby",
                "Moby-Dick" , "Harry Potter" , "The Catcher in the Ray",
                "The Hobbit" , "War and Peace"
            ],
            "Magazines": [
                "Time","National Geographic", "The New Yorker", "Forbes" ,  "Vogue"
                "Scientific American" ,"Rolling Stone" , "Sports Illustrated"
            
            ],
            "Novels":[
                "The Name of the Wind" , "Dune" , "1984" , "Gone Girl" , "Pride and Prejudice" , "The Book Thief"
            ],
            "Reference_Books":[
                "Encyclopedia Britannica" , "Oxford English Dictionary" , "Gray's Anatomy" ,
                "The Chicago Manual of Style" ,"Roget's International Thesaurus" , "Guinness World Records" ,
                "DSM-5","Atlas of the World"
            ]}
    
print("We have following options please select one")
print("""
    Press 1 for Books
    Press 2 for Magazines
    Press 3 for Novels
    Press 4 for Reference book
    Press 5 for Exit
""")
option=input("Press your options(1/2/3/4/5):")
category=""
if option == "1":
    category = "Books"
elif option == "2":
    category = "Magazines"
elif option == "3":
    category = "Novels"
elif option == "4":
    category = "Reference_Books"
elif option == "5":
    print("Thank you for using our LMS")
    exit()
else:
    print("Invalid option")
    exit()
    
df = pd.read_csv(r"/Users/fajarfatima/Desktop/add_book.py.csv")
print(f"\nCategories in {category}:")
for book in books_categories[category]:
    print(f"- {book}")

book_title = input("Enter the title of the book you want to view: ")
book_data = df[df['title'] == book_title]

if not book_data.empty:
    book_info = book_data.iloc[0]
else:
    print("Book not found in the list.")

if not book_data.empty:
    book_info = book_data.iloc[0]
    print(f"\nBook info for '{book_title}':")
    print(f"Author: {book_info.get('author', 'N/A')}")
    print(f"Year Published: {book_info.get('year_of_publish', 'N/A')}")
    print(f"Genre: {book_info.get('genre', 'N/A')}")
    print(f"ISBN: {book_info.get('isbn', 'N/A')}")
    print(f"Pages: {book_info.get('pages', 'N/A')}")
    print(f"Copies: {book_info.get('copies', 'N/A')}")
    print(f"Price: {book_info.get('price', 'N/A')}")

    book_choice = input("Do you want to read or borrow? ").lower()
    if book_choice == "read":
        print("Here you go. Have a nice day!")
    elif book_choice == "borrow":
        print("For Borrow Book,Please pay 250/- at the counter.")
        print("Thank you! And have a nice day!")
    else:
        print("Invalid option.")
        print("Thank you for using our LMS.")
else:
    print(f"Book info for '{book_title}' not found.")        
obj=Reference_book('price', 'title', 'author', 'genre', 'year_of_publish', 'isbn', 'pages', 'copies')
obj.additional_info()


# In[ ]:




