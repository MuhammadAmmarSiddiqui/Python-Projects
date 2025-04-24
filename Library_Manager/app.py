prog : str = ''
Record : list = []
try:
    with open('library.txt', 'r+') as file:
        for line in file:
            Record.append(eval(line.strip()))
        file.seek(0) # Move cursor to the beginning of file
        file.truncate() # Clear the file content
        file.close() # Clear file content after reading
except FileNotFoundError:
    print("No previous records found.")
    
while prog != 'exit':
    print("""
          Welcome to Personal Library Manager
            -----------------------------------
          1. Add a book
          
          2. Remove a book
          
          3. Display all books with their details
          
          4. Search for a book
          
          5. Statistics of your library
          
          6. Exit
          
            --------------------------------""")
    


    user_input = int(input("Enter the number of your choice:"))
    #user_input =user_input.lower()
    #Add Book Option
    if user_input == 1:
        print("You can now add a book to your library")
        title = input("Enter title of your book:")
        author = input("Enter author of your book:")
        public_date = input("Enter the publication date of your book:")
        genre = input("Enter genre of your book:")
        read_status = input("Have you read this book? (yes/no):")
        new_book = {
            "title": title.upper(),
            "author": author.upper(),
            "pubication date": public_date,
            "genre": genre,
            "read status": read_status.lower()
        }
        Record.append(new_book)
        print("Book Added Successfully!")
        
    elif user_input == 2:
        print("Delete a book by the title of your book")
        delete_title = input("Enter title of your book here: ")
        for book in Record:
            if book["title"] == delete_title.upper():
                Record.remove(book)
                print("Book Deleted Successfully!")
            else:
                print("No book found with the current title.")
    
    # 3. Display all books Option
    elif user_input == 3:
        if Record == []:
            print("No books in the library. Click on option 1 to add a book.")
        else:
            print(Record)
    
    # 4. Search Option
    elif user_input == 4:
        print("""You can search with title or author of the book.
              
            1. Search by title 
            
            2. Search by author 
              
              """)
        search_input = int(input("Please select one option:"))
        # Search using title of book
        if search_input == 1:
            search_list : list = []
            search_title = input("Enter title of your book:")
            
            if Record == []:
                print("No books in the library. Click on option 1 to add a book.")
            else:
                for book in Record:
                    if book["title"] == search_title.upper():
                        print("Book Found!")
                        search_list.append(book)
                if search_list == []:
                    print("No book found with current search input.")
                else:
                    print(search_list)
                    search_list.clear()    
        
        # Search using author of book                
        elif search_input == 2 :
            search_author = input("Enter author of your book:")
            if Record == []:
                print("No books in the library. Click on option 1 to add a book.")
            else:
                for book in Record:
                    if book["author"] == search_author.upper():
                        print("Book Found!")
                        search_list.append(book)
                if search_list == []:
                    print("No book found with current search input.")
                else:
                    print(search_list)
                    search_list.clear()
        else:
            print("Please select valid search option")
    
    # 5. Stats Option of library
    elif user_input == 5:
        read_books: int = 0
        unread_books: int = 0
        print("Statistics of your library")
        if Record == []:
                print("No books in the library. Click on option 1 to add a book.")
        else:
            total_books = len(Record)
            print("Total number of books in your library:", total_books)
            for book in Record:
                if book["read status"] == 'yes':
                    read_books = read_books + 1
                elif book["read status"] == 'no':
                    unread_books = unread_books + 1
            read_percentage = (read_books/total_books)*100
            unread_percentage = (unread_books/total_books)*100
            print("You have read ", round(read_percentage, 2), "in your library")
            print("You have unread ", round(unread_percentage, 2), "in your library")
    
    # 6. Exit Option        
    elif user_input == 6:
        with open('library.txt', 'w') as file:
            for book in Record:
                file.write(str(book)+'\n')
        file.close()
        #print(user_input)
        prog = 'exit'
