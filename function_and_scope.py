
def printAddition(x, y) :
    print(x+y)

def add(x, y) :
    return x+y

nothing = printAddition(29, 8) 
# 37

print(nothing, type(nothing))
# None <class 'NoneType'>

addition = add(2, 7)
print(addition, type(addition))
# 9 <class 'int'>


number = 100

def fun1() :
    number = 200 #new local
    print("LOCAL", number) # 200

def fun2() :
    number = 300 #new local
    print("LOCAL", number) # 300

def fun3() :
    global number
    number = 1
    print("UPDATING LOCAL", number) # 1

def fun4() :
    b = number + number
    print("USING GLOBAL", b) # 2
    
    
fun1()
fun2()
print("NO CHANGE GLOABL", number) # 100

fun3()
print("AFTER GLOBAL", number) # number is 1
fun4()

# global list, dictionaries can not be reassigned
# but internal values can be changed
movies = ['Life of pie', 'Pirates', 'Dark Knight', 'King\'s speech']
print("ORIGINAL", movies)

def updateMovie(index, newMovie) :
    movies[index] = newMovie

updateMovie(0, 'Fight Club')
print("UPDATED", movies)


#updateMovie(5, 'Joker')
#print("UPDATED", movies) # index out of range
