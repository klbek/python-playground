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
        init_dictionary = {"books": {}}
        json.dump(init_dictionary, file, ensure_ascii=False, indent=4)


def add_book(id: int ,name: str, author: str = None, year=int):
    with open('library_manager/my_library.json', mode='r+', encoding='utf-8') as file:
        file_data = json.load(file)
        time_added = str(datetime.now().strftime('%Y-%m-%d %H:%m'))
        record = {'name': name, 'author': author,
                  'year': year, 'time_added': time_added}
        file_data['books'][id] = record
        file.seek(0)
        json.dump(file_data, file, ensure_ascii=False, indent=5)


def find_book(**kwargs):
    with open('library_manager/my_library.json', mode='r', encoding='utf-8') as file:
        library_dictionary = json.load(file)
    query_id = kwargs.get('id')

    if query_id:
        return library_dictionary["books"].get(kwargs['id'], None)
    
    filtered_books = []
    for book_record in library_dictionary["books"].values():
        if all(book_record.get(key) == value for key, value in kwargs.items() if key != 'id'):
            filtered_books.append(book_record)
    return filtered_books


def show_all():
    with open('library_manager/my_library.json', mode='r', encoding='utf-8') as file:
        library_dictionary = json.load(file)

    return library_dictionary['books']


def delete_book(name: str = None, author: str = None, year: int = None):
    with open('library_manager/my_library.json', mode='r+', encoding='utf-8') as file:
        library_dictionary = json.load(file)
        
        search = [name, author, year]
        id_number = len(search) - search.count(None)

        for book_record in library_dictionary["books"]:
            
            book_name = book_record['name']
            book_author = book_record['author']
            book_year = book_record['year']

            # if id_number == 3:
            #     if book_name == name and book_author == author and book_year == year:
            #         del library_dictionary["books"][id]
            #         print(library_dictionary)

            #         file.seek(0)
            #         json.dump(library_dictionary, file, ensure_ascii=False, indent=5)



# init_library() # use only for the first time
# add_book(6,'Na vesnici', 'Tax', 2020)
# print(find_book(id='1'))
print(find_book(author='Tax', year=2020))
# print(find_book(author='Tax'))
# print(show_all())

# delete_book(name='test2', author='John', year=2014)
# print(show_all())

# with open('library_manager/my_library.json', mode='r+', encoding='utf-8') as file:
#     library_dictionary = json.load(file)
# # for i in library_dictionary['books']:
# #     if i['author'] == 'Dan':
# #         del i
# #     print(i)
# print(library_dictionary['books'])