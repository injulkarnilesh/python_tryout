
def function_normal(name, age, job) :
    sentence = "{} is {} years old, and is {} by profession".format(name, age, job)
    return sentence

#positional args
print(function_normal("Nilesh", 26, "Software Craftsman"))

#keyword args
print(function_normal(age = 34, job = "Cricket Player", name = "Sachin"))

#default params should be towards end
def function_default(name, age = 20, job = "Unemployed") :
    sentence = "{} is {} years old, and is {} by profession".format(name, age, job)
    print(sentence)

function_default("Sagar", 56, "Teacher")
function_default("Amrut", 34)
function_default("Sushil")
function_default(job = "Plumber", name = "Abhijit")

# * on param -> packing, function treats all args into a single tuple
# * on arg -> unpacking, iterable arg is passed as multiple params

#unpacking tuple
print(1, 2, 3)
print(*(1, 2, 3))

print("ABC")
 # equivalent to
print(*"ABC")

def new_line_print(*lines) :
    for line in lines :
        print(line)

new_line_print("NILESH", "SHRIPATI", "INJULKAR")
new_line_print(*"pirate")

#packing
def add(*numbers) :
    total = 0
    for number in numbers :
        total += number
    return total

print("Adding multiple args", add(1, 4, 10, 34))
print("Adding iterable", add(*[1, 4, 10, 34]))

# ** on param -> packing, function treats all args into single dictionary
# ** on arg -> unpacking, dictionary is passed as keyword arguments

def expand(**kwargs) :
    print("{")
    for key, value in kwargs.items() :
        print(" {} : {} ".format(key, value))
    print("}")

expand(name = "Gaurav", age = 34, job = "Series Watcher")
    # equivalent to
expand(**{ "name" : "Rahul", "age" : 12, "job" : "Kid"})

function_default(**{ "name" : "Pratik", "age" : 56, "job" : "IAS" })

