from models import (Base, session, Book, engine)
import csv
import datetime


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


def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    split_date = date_str.split(' ')
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.datetime(year, month, day)


def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)


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
    # app()
    # add_csv()
    clean_date('November 12, 2019')
