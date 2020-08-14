file = open('My Clippings.txt', 'r')
separator = '=========='
while(True):
    book = file.readline()
    if(len(book.strip()) == 0):
         break
    file.readline()
    file.readline()
    note = ''
    line = file.readline()
    while(not line.startswith(separator)):
        note += line + '\n'
        line = file.readline()
    notefile = open(book + '.txt', 'a')
    notefile.write(note)
    notefile.close()    