from datetime import datetime
import json
""" 
Napiš program, který:

    Spravuje seznam knih v jednoduché knihovně.
    Umožní uživateli následující akce:
        Přidat novou knihu.
        Vyhledat knihu podle názvu nebo autora.
        Zobrazit všechny knihy v knihovně.
        Vymazat knihu. 
        Ukončit program.
        """


def init_library():
    with open('library_manager/my_library.json', mode='w', encoding='utf-8') as file:
        init_dictionary = {"books": []}
        json.dump(init_dictionary, file, ensure_ascii=False, indent=4)


def add_book(name: str, author: str = None, year=int):
    with open('library_manager/my_library.json', mode='r+', encoding='utf-8') as file:
        file_data = json.load(file)
        time_added = str(datetime.now().strftime('%Y-%m-%d %H:%m'))
        record = {'name': name, 'author': author,
                  'year': year, 'time_added': time_added}
        file_data["books"].append(record)
        file.seek(0)
        json.dump(file_data, file, ensure_ascii=False, indent=5)


def find_book(name: str = None, author: str = None, year: int = None):
    with open('library_manager/my_library.json', mode='r', encoding='utf-8') as file:
        library_dictionary = json.load(file)

    search = [name, author, year]
    id_number = len(search) - search.count(None)
    matching_books = []

    for book_record in library_dictionary["books"]:
        book_name = book_record['name']
        book_author = book_record['author']
        book_year = book_record['year']

        if id_number == 3:
            if book_name == name and book_author == author and book_year == year:
                matching_books.append(book_record)

        if id_number == 2:
            if book_name == name and book_author == author:
                matching_books.append(book_record)
            if book_author == author and book_year == year:
                matching_books.append(book_record)
            if book_name == name and book_year == year:
                matching_books.append(book_record)

        if id_number == 1:
            if book_name == name:
                matching_books.append(book_record)
            if book_author == author:
                matching_books.append(book_record)
            if book_year == year:
                matching_books.append(book_record)

    return matching_books

def show_all():
    with open('library_manager/my_library.json', mode='r', encoding='utf-8') as file:
        library_dictionary = json.load(file)

    return library_dictionary['books']



# init_library() # use only for the first time
# add_book('Jak nespat', 'Lex', 2010)
# print(find_book(author='Dan'))
print(show_all())