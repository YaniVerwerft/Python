output_file = open('books2.csv', 'w', encoding='UTF-8')
with open('Files Chapter 7/books.txt', encoding='UTF-8') as file:
    file.readline()  #titel lezen en niks mee doen
    book = file.readline()
    while book:
        author = file.readline()
        output_file.write(author.rstrip() + ';' + book)
        book = file.readline()
output_file.close()