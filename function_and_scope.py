
def printAddition(x, y) :
    print(x+y)

def add(x, y) :
    return x+y

nothing = printAddition(29, 8)
print(nothing, type(nothing))

addition = add(2, 7)
print(addition, type(addition))

number = 100

def fun1() :
    number = 200 #new local
    print("LOCAL", number)

def fun2() :
    number = 300 #new local
    print("LOCAL", number)

def fun3() :
    global number
    number = 1
    print("UPDATING LOCAL", number)

def fun4() :
    b = number + number
    print("USING GLOBAL", b)
    
    
fun1()
fun2()
print("NO CHANGE GLOABL", number)

fun3()
print("AFTER GLOBAL", number)
fun4()

# globla list, dictionaries can not be reassigned
# but internal values can be changed
movies = ['Life of pie', 'Pirates', 'Dark Knight', 'King\'s speech']
print("ORIGINAL", movies)

def updateMovie(index, newMovie) :
    movies[index] = newMovie

updateMovie(0, 'Fight Club')

print("UPDATED", movies)


