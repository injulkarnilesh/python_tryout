
#input user name
name = input("What's your name? : ")

#input age
age = input("How old are you? : ")

# input country
country = input("What country do you live in? : ")

print(name + " " +age +  " years old, lives in " + country);

#using format {number} number starting with 0 is optional
message = "You are {}, {} years old, living in {}";
output = message.format(name, age, country);
print(output);
