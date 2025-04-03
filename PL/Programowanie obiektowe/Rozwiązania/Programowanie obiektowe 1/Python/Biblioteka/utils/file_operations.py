import json

## \brief Loads book data from a JSON file.
#  \param file_path Path to the JSON file containing book data.
#  \return List of dictionaries containing book data.
def load_books(file_path):
    try:
        with open(file_path, 'r') as file:
            books_data = json.load(file)
            return books_data
    except FileNotFoundError:
        return []

## \brief Saves book data to a JSON file.
#  \param file_path Path to the JSON file to save book data.
#  \param books List of dictionaries containing book data.
def save_books(file_path, books):
    with open(file_path, 'w') as file:
        json.dump(books, file, indent=4)

## \brief Loads member data from a JSON file.
#  \param file_path Path to the JSON file containing member data.
#  \return List of dictionaries containing member data.
def load_members(file_path):
    try:
        with open(file_path, 'r') as file:
            members_data = json.load(file)
            return members_data
    except FileNotFoundError:
        return []

## \brief Saves member data to a JSON file.
#  \param file_path Path to the JSON file to save member data.
#  \param members List of dictionaries containing member data.
def save_members(file_path, members):
    with open(file_path, 'w') as file:
        json.dump(members, file, indent=4)

## \brief Loads history data from a text file.
#  \param file_path Path to the text file containing history data.
#  \return List of strings containing history entries.
def load_history(file_path):
    try:
        with open(file_path, 'r') as file:
            history = file.readlines()
            return history
    except FileNotFoundError:
        return []

## \brief Saves history data to a text file.
#  \param file_path Path to the text file to save history data.
#  \param history List of strings containing history entries.
def save_history(file_path, history):
    with open(file_path, 'a') as file:
        for entry in history:
            file.write(entry + '\n')