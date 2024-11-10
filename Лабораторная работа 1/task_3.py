amount_of_memory = 1.44 * 1024 * 1024
number_of_pages = 100
number_of_lines = 50
number_of_symbols = 25
symbol_weight = 4

number_of_books = int(amount_of_memory // (number_of_pages * number_of_lines * number_of_symbols * symbol_weight))

print("Количество книг, помещающихся на дискету:", number_of_books)

