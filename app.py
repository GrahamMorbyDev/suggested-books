from models import (Base, session, Book, engine)
# Main menu - add, search, analysis, exit, view
# add books
# edit books
# search books
# data cleaning
# loop over program
if __name__ == '__main__':
    Base.metadata.create_all(engine)
