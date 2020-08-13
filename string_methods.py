
message = "Good Morning"
print(message.count('o')) #3
print(message.count("ng")) #1
print("Upper", message.upper()) #GOOD MORNING
print("Lower", message.lower()) #good morning

#immutable
print("Immutable", message)

message = message.lower()
print("Captalized", message.capitalize()) #Good morning
print("Titled", message.title()) #Good Morning

print("abcD islower :", "abcD".islower()) #False
print("abcd islower :", "abcd".islower()) #True

print("aBcd isupper :", "aBcd".isupper()) #False
print("ABC isupper :", "ABC".isupper()) #True

print("Nilesh Injulkar istitle :", "Nilesh Injulkar".istitle()) #True
print("Pune mh istitle :", "Pune mh".istitle()) #False

print("aBcd isalpha :", "aBcd".isalpha()) #True
print("AB CD isalpha :", "AB CD".isalpha()) #False

print("12312 isdigit :", "12312".isdigit()) #True
print("B67T isdigit :", "B67T".isdigit()) #False

print("12312 isalnum :", "12312".isalnum()) #True
print("B67T isalnum :", "B67T".isalnum()) #True
print("B67!T isalnum :", "B67!T".isalnum()) #False

greeting = "Happy Birthday"
print("len", len(greeting)) #14
print("index", greeting.index("day")) #11

#Errors out if not found
#print("index not found", greeting.index("Day"))

print("find", greeting.find("Birthday")) #6
print("find not found", greeting.find("birthday")) #-1

greeting = "###Happy Birthday####"
print("strip #", greeting.strip("#")) #Happy Birthday
print("sltrip #", greeting.lstrip("#")) #Happy Birthday####
print("rstrip #", greeting.rstrip("#")) ####Happy Birthday

greeting = " Nice Day  "
print("strip", greeting.strip()) #Nice Day
