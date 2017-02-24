
message = "Good Morning"
print(message.count('o'))
print(message.count("ng"))
print("Upper", message.upper())
print("Lower", message.lower())

#immutable
print("Immutable", message)

message = message.lower()
print("Captalized", message.capitalize())
print("Titled", message.title())

print("abcD islower :", "abcD".islower())
print("abcd islower :", "abcd".islower())

print("aBcd isupper :", "aBcd".isupper())
print("ABC isupper :", "ABC".isupper())

print("Nilesh Injulkar istitle :", "Nilesh Injulkar".istitle())
print("Pune mh istitle :", "Pune mh".istitle())

print("aBcd isalpha :", "aBcd".isalpha())
print("AB CD isalpha :", "AB CD".isalpha())

print("12312 isdigit :", "12312".isdigit())
print("B67T isdigit :", "B67T".isdigit())

print("12312 isalnum :", "12312".isalnum())
print("B67T isalnum :", "B67T".isalnum())
print("B67!T isalnum :", "B67!T".isalnum())

greeting = "Happy Birthday"
print("len", len(greeting))
print("index", greeting.index("day"))

#Errors out if not found
#print("index not found", greeting.index("Day"))

print("find", greeting.find("Birthday"))
print("find not found", greeting.find("birthday"))

greeting = "###Happy Birthday####"
print("strip #", greeting.strip("#"))
print("sltrip #", greeting.lstrip("#"))
print("rstrip #", greeting.rstrip("#"))

greeting = " Nice Day  "
print("strip", greeting.strip())
