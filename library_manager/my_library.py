from datetime import datetime
import json


def init_library():
    with open('library_manager/my_library.json', mode='w', encoding='utf-8') as file:
        init_dictionary = {"books": {}}
        json.dump(init_dictionary, file, ensure_ascii=False, indent=4)


def add_book(id: int, name: str, author: str = None, year=int):
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


def delete_book(**kwargs):
    with open('library_manager/my_library.json', mode='r+', encoding='utf-8') as file:
        library_dictionary = json.load(file)
        query_id = kwargs.get('id')

        if query_id:
            if str(query_id) in library_dictionary["books"].keys():
                del library_dictionary["books"][str(query_id)]

        file.seek(0)
        file.truncate()
        json.dump(library_dictionary, file, ensure_ascii=False, indent=5)


# init_library() # use only for the first time
# add_book(6,'Na vesnici', 'Tax', 2020)
# print(find_book(id='1'))
# print(find_book(author='Tax', year=2020))
# print(find_book(author='Tax'))
# print(show_all())
# delete_book(name='test2', author='John', year=2014)
# print(show_all())
print(delete_book(id=1))
