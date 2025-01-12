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


def add_book(name: str, author: str, year=int):
    with open('library_manager/my_library.json', mode='r+', encoding='utf-8') as file:
        file_data = json.load(file)
        time_added = str(datetime.now().strftime('%Y-%m-%d %H:%m'))
        record = {'name': name, 'author': author,
                  'year': year, 'time_added': time_added}
        file_data["books"].append(record)
        file.seek(0)
        json.dump(file_data, file, ensure_ascii=False, indent=5)


# init_library() # use only for the first time
add_book('test', 'author', 2014)
