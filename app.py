from models import (Base, session, Book, engine)
# Main menu - add, search, analysis, exit, view


def menu():
    while True:
        print('''
            \nPROGRAMMING BOOKS
            \r1) Add book
            \r2) View all books
            \r3) Search for a book 
            \r4) Book Analaysis
            \r5) Exit
        ''')
        choice = input('What would you like to do? ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            input('''\rPlease choice one the options above
                     \rA number from 1-5.
                     \rPress enter to try again  ''')
# add books
# edit books
# search books
# data cleaning
# loop over program


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # Add book
            pass
        elif choice == '2':
            # View all books
            pass
        elif choice == '3':
            # Search for a book
            pass
        elif choice == '4':
            # Analyis a book
            pass
        else:
            print('Goodbye')
            app_running = False
            exit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()
