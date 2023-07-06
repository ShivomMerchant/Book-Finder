##############################################################
    #  Computer Project #6
    #  import math, csv, and itemgetter
    #  Define menu options
    #
    #  Open file function
    #   Takes input for what file
    #       Try/ except to see if file opens
    #           returns file or returns open file
    #  
    #  Read file function
    #   Create a list
    #   Use for loop to iterate through text
    #       Define all varibles
    #       Use list to imput all data in list and apppend values to the tuple
    #   return the tuple
    #
    #  Get books criterion function
    #   Create a list
    #   For loop to iterate through tuple
    #       Finds values to create a list
    #   Returns a list or muliple lists
    #
    #  Get books criteria function
    #   defines sorted books by using get books criterion function
    #   returns sortedbooks
    #   
    #  Get books by keyword function
    #   for loop to iterate through
    #       finds keyword in tuple
    #   returns key books
    #
    #  Sort authors function
    #   Creates sort list
    #   Return list
    #   
    #  recoomend books function
    #   defines sorted books by using get books criterion function
    #   returns sortedbooks
    #
    #
    #  Display books functions
    #   formats the information in tuples
    #   For loop to iterate through values
    #   Prints formatting
    #
    #  Get option function
    #   prints and imputs values for menu
    #   Keeps prompting till correct option
    #
    #
    #  Main function
    #   Call necessary functions
    #   If statement for error message
    #       print error statement and menu options
    #   Intiate while loop for when the option is not 3
    #       Initiate while loop for every option
    #           Call necessay functions to the main function in each option
    #           Print statemnets for options
    #           Print menu options 
    #    Display closing message
##############################################################

#import modules
import math
import csv
from operator import itemgetter

TITLE = 1
CATEGORY = 3
YEAR = 5
RATING = 6
PAGES = 7

TITLE_FORMAT = "{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}"
TABLE_FORMAT = "{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}"

MENU = "\nWelcome to the Book Recommendation Engine\n\
        Choose one of below options:\n\
        1. Find a book with a title\n\
        2. Filter books by a certain criteria\n\
        3. Recommend a book \n\
        4. Quit the program\n\
        Enter option: "

CRITERIA_INPUT = "Choose the following criteria\n\
                 (3) Category\n\
                 (5) Year Published\n\
                 (6) Average Rating (or higher) \n\
                 (7) Page Number (within 50 pages) \n\
                 Enter criteria number: "

def open_file():
    """
    Checks for if file is a vaild file

    Returns
    -------
    a file

    """
    #Try, except to see if file opens
    #returns flle if it does not work to reprompt
    while 1==1:
        file = input("Enter file name: ")
        try:
            #looks to see if the file can open 
            fp = open(file, "r", encoding="utf-8")
            return fp
        except:
            #if the file is not found return the function to reask for file
            print("Error opening file. Please try again.")
            print("")
            return open_file()

def read_file(fp):
    """
    This function reads the file

    Parameters
    ----------
    fp : string
        file pointer

    Returns
    -------
    list_of_tuples : list
        A tuple that contains the information

    """
    list_of_tuples = []
    reader = csv.reader(fp)
    next(reader)
    #For loop to iterate through file
    #Assign varibles and create tuple
    for line in reader:
        try:
            isbn13 = line[0]
            title = line[2]
            authors = line[4]
            categories = list(line[5].lower().split(","))
            description = line[7]
            year = line[8]
            rating = float(line[9])
            num_pages = int(line[10])
            rating_count = int(line[11])
            list_tuple = (isbn13, title, authors, categories, description, year, rating, num_pages, rating_count)
            list_of_tuples.append(list_tuple)
        except:
            pass
    return list_of_tuples
    

def get_books_by_criterion(list_of_tuples, criterion, value):
    """
    List created based on criterion

    Parameters
    ----------
    list_of_tuples : list
        information that is in a tuple
    criterion : int
        DESCRIPTION.
    value : string
        DESCRIPTION.

    Returns
    -------
    tuple
        Tuple that contains information.

    """
    #iterates through previous tuple created
    #Creates a new list
    List = []
    for val in list_of_tuples:
        if criterion == TITLE and value.lower() == str(val[TITLE]).lower():
            return val
        elif criterion == CATEGORY and value.lower() in [i.lower() for i in val[CATEGORY]]:
            List.append(val)
        elif criterion == YEAR and value == str(val[YEAR]):
            List.append(val)
        elif criterion == RATING and float(value) <= float(val[RATING]):
            List.append(val)
        elif criterion == PAGES and abs(int(value) - val[PAGES]) <= 50:
            List.append(val)
    return List


def get_books_by_criteria(books, category=None, rating=None, page=None):
    """
    list of tuples based off criteria

    Parameters
    ----------
    books : strings
        book title.
    category : string, optional
        the catagory to search for. The default is None.
    rating : float, optional
        the rating . The default is None.
    page : int, optional
        The page number. The default is None.

    Returns
    -------
    sortedbooks : tuple
        A list of tuples created.

    """
    #Defines sorted books
    #Creates sorted book lists by using previous functions
    sortedbooks = books
    sortedbooks = get_books_by_criterion(sortedbooks, CATEGORY, category)
    sortedbooks = get_books_by_criterion(sortedbooks, RATING, str(rating))
    sortedbooks = get_books_by_criterion(sortedbooks, PAGES, str(page))
    return sortedbooks

def get_books_by_keyword(list_of_tuples, keywords):
    """
    

    Parameters
    ----------
    list_of_tuples : tuple
        list of tuples for books.
    keywords : list
        list of key words.

    Returns
    -------
    key_books : tuple
        the list of tuples for books.

    """
    
    #Iterates through tuple and finds key words
    #Creates another list to find key books
    key_books = []
    for book in list_of_tuples:
        book_lower = book[4].lower()
        for key in keywords:
            if key.lower() in book_lower:
                if book not in key_books:
                    key_books.append(book)
                    break
    return key_books

def sort_authors(list_of_tuples, a_z = True):
    """
    Sorts the lists based of the authors name 

    Parameters
    ----------
    list_of_tuples : tuple
        list of tuples for books.
    a_z : boolean, optional
        The default is True.

    Returns
    -------
    sort_list : list
        the sorted list of tuples.

    """
    
    #Creates sorted list by sorted function
    if a_z:
        sort_list = sorted(list_of_tuples, key=itemgetter(2))
    else:
        sort_list = sorted(list_of_tuples, key=itemgetter(2), reverse=True)
    return sort_list

def recommend_books(list_of_tuples, keywords, category=None, rating=None, page_number=None, a_z=True): 
    """
    Creates list based on user imput

    Parameters
    ----------
    list_of_tuples : list
        the tuple made orginally.
    keywords : list
        list of key words.
    category : string, optional
        The string found. The default is None.
    rating : TYPE, optional
        the rating to search. The default is None.
    page_number : int, optional
        The page number imputted. The default is None.
    a_z : boolean, optional
        The default is True.

    Returns
    ------- 
    sort_books : list
        tuple that is created.

    """
    #Creates sort books by using prevoius functions
    sort_books = list_of_tuples
    sort_books = get_books_by_criterion(sort_books, CATEGORY, category)
    sort_books = get_books_by_criterion(sort_books, RATING, rating)
    sort_books = get_books_by_criterion(sort_books, PAGES, page_number)
    key_books = get_books_by_keyword(sort_books, keywords)
    sort_books = sort_authors(key_books, a_z=a_z)
    return sort_books


def display_books(list_of_tuples): 
    """
    Formatted tavle of tuple

    Parameters
    ----------
    list_of_tuples : list
        list of tuples orginally created.

    Returns
    -------
    None.

    """
    #Make a for loop to iterate through tiple and assign values
    #Create formatting for table
    if list_of_tuples == []:
        print("Nothing to print.")
        
    else:
        print("\nBook Details:")
        print(TITLE_FORMAT.format("ISBN-13", "Title", "Authors", "Year", "Rating", "Number Pages", "Number Ratings"))
        for a_tuple in list_of_tuples:
            isbn13 = a_tuple[0]
            title = a_tuple[1]
            author = a_tuple[2]
            year = a_tuple[5]
            rating = a_tuple[6]
            number_pages = a_tuple[7]
            number_ratings = a_tuple[8]
            
            #Error checking for lenght of title and authors name
            if len(title) > 35: 
                continue
            if len(author) > 35:
                continue
            
            print(TABLE_FORMAT.format(isbn13, title, author, year, rating, number_pages, number_ratings))                


def get_option():
    """
    Gets the option 

    Returns
    -------
    option : int
        The option as an int.

    """
    #Creates a list to error check
    codes = (1,2,3,4)
    print(MENU)
    option = int(input(""))
    if option in codes:
        return option
    if option not in codes:
        print("Invaild option")
        print(MENU)
        option = int(input(""))
        return None
    
def main():
    file = open_file()
    option = get_option()
    list_of_tuples = read_file(file)
    
    #If option 4 break out of loop
    while option == None:
        option = get_option()
    while option == 4:
        break
    
    while option ==1:
        book_im = input("Input a book title: ")
        #Create a list to append title to the list
        list1 = []
        for val in list_of_tuples:
            if book_im == val[1]:
                list1.append(val)
                break
        display_books(list1)
        option = get_option()
        
    while option ==2:
        print(CRITERIA_INPUT)
        criteria_in = int(input(""))
        codesCrit = 3,5,6,7
        #Error checking
        if criteria_in not in codesCrit:
            print("\nInvalid input")
            print(CRITERIA_INPUT)
            criteria_in = int(input(""))
        value_in = input("Enter value: ")
        
        if criteria_in == RATING:
            while True:
                try:
                    value_in = float(value_in)
                    break
                except:
                    value_in = input("\nEnter value: ")
                    continue
        elif criteria_in == PAGES:
            while True:
                try:
                    value_in = float(value_in)
                    break
                except:
                    value_in = input("\nEnter value: ")
                    continue
        #New list made by using function
        #Use new list to make another list
        #Print out necessary tables by calling function
        list_of_tuples_two = get_books_by_criterion(list_of_tuples, criteria_in, value_in)
        sort_list_of_tuple = sort_authors(list_of_tuples_two, a_z = True)
        if len(sort_list_of_tuple) >= 30:
            sort_list_of_tuple = sort_list_of_tuple[0:30]
        display_books(sort_list_of_tuple)
        option = get_option()

# DO NOT CHANGE THESE TWO LINES
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()
