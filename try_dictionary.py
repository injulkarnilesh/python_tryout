
people = { "Harry" : 45, "Ron" : 33, "Hermione" : 39 }

print(people, type(people)) #<class 'dict'>
print(people.keys(), type(people.keys())) #<class 'dict_keys'>
print(people.values(), type(people.values())) #<class 'dict_values'>

print(people["Harry"]) #45

#not a list
#people.keys()[0]
#peope.values()[2]

print(list(people.keys())[1]) #Ron
print(list(people.values())[0]) #45

#error
#print(people["Voldemort"])

people["Ron"] = 34
print(people["Ron"]) #34

people["Severus"] = 90
print(people) # Severus added

people["Dumbledore"] = "TOO OLD"
print(people) #Dumbledore Added

they = { "US" : ["Alex", "001", 12], "IN" : ["Nilesh", "003", 43] }
print(they["IN"][1:]) #["003", 43]

westeros = {
        "Tyrian" : { "House" : "Lannister", "Age" : 39, "Alive" : True },
        "Ned" : { "House" : "Stark", "Age" : 54, "Alive" : False },
        "Jon" : { "House" : "Stark", "Age" : 31, "Alive" : False },
        "Lyanna" : {"House" : "Bear Island", "Age" : 14, "Alive" : True }
    }
print(westeros["Lyanna"]["House"]) #Bear Island
print(westeros)
westeros["Jon"]["Alive"] = True
print(westeros)
westeros["Davos"] = {"House" : "Seaworth", "Age" : 65, "Alive" : True }
print(westeros)


