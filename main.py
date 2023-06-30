#calc_average(numbers: list)

def calc_average(numbers: list) -> float:
    if not numbers:
        raise ValueError('Empty list')

    total = 0
    count = 0

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError('Invalid value in the list')
        total += num
        count += 1

    return total / count


#print_pyramid(rows: int)

def print_pyramid(rows: int) -> None:
    if not isinstance(rows, int):
        raise ValueError('Invalid value for rows')

    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))


#clean_string(my_string: str)

def clean_string(my_string: str) -> str:
    special_chars = "!@#$%^&*()_-+=~`[{]}\|;:'\",<.>/?"
    digits = "0123456789"

    cleaned_string = ""
    for char in my_string:
        if char not in special_chars and char not in digits:
            cleaned_string += char

    return cleaned_string


#count_special_char(my_string: str)

def count_special_char(my_string: str) -> int:
    special_chars = "!@#$%^&*()_-+=~`[{]}\|;:'\",<.>/?"
    digits = "0123456789"

    special_char_count = 0
    digit_count = 0

    for char in my_string:
        if char in special_chars:
            special_char_count += 1
        elif char in digits:
            digit_count += 1
    return special_char_count + digit_count



#dict_to_list(dictionary: dict)

def dict_to_list(dictionary: dict) -> list:
    return list(dictionary.values())


#list_to_dict(key_list: list, value_list: list)

def list_to_dict(key_list: list, value_list: list) -> dict:
    if len(key_list) != len(value_list):
        raise ValueError('Lists must be of the same length')

    dictionary = dict(zip(key_list, value_list))
    return dictionary


#chunk_list(my_list: list, chunks: int)

def chunk_list(my_list: list, chunks: int) -> list:
    if not my_list:
        raise ValueError('The list must not be empty')

    list_length = len(my_list)
    if list_length % chunks != 0:
        raise ValueError('The list length must be divisible by chunk size')

    chunk_size = list_length // chunks
    chunked_list = [my_list[i:i+chunk_size] for i in range(0, list_length, chunk_size)]
    return chunked_list


#class Book

class Book:
    def __init__(self, name: str, author: str, genre: str, borrowed: bool = False):
        self.name = name
        self.author = author
        self.genre = genre
        self.borrowed = borrowed

    def __str__(self):
        return f"{self.name}, {self.author}, {'Borrowed' if self.borrowed else 'Not Borrowed'}"


#class Library

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.book_list.append(book)

    def get_all_books(self):
        return self.book_list

    def borrow_book(self, book):
        if isinstance(book, Book):
            if book in self.book_list:
                if book.borrowed:
                    print('Book already borrowed')
                else:
                    book.borrowed = True
            else:
                print('Book does not exist')

    def return_book(self, book):
        if isinstance(book, Book):
            if book in self.book_list:
                if not book.borrowed:
                    print('Book has not been borrowed')
                else:
                    book.borrowed = False
            else:
                print('Book does not exist')


#class Bookstack

class BookStack:
    def __init__(self):
        self.stack = []

    def push(self, book):
        if isinstance(book, Book):
            self.stack.append(book)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


#count_words(file_path: string)

def count_words(file_path: str) -> int:
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading file.")
    except UnicodeDecodeError:
        print("Unable to decode file.")
    return 0


#count_lines(file_path: string)

def count_lines(file_path: str) -> int:
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")
    except UnicodeDecodeError:
        print("Unable to decode the file.")
    return 0


#write_even(input_file_path: string, output_file_path)

def write_even(input_file_path: str, output_file_path: str):
    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            lines = input_file.readlines()
            even_lines = lines[1::2] 
            output_file.writelines(even_lines)
    except FileNotFoundError:
        print("Input file not found.")
    except IOError:
        print("Error reading/writing file.")
    except UnicodeDecodeError:
        print("Unable to decode file.")
