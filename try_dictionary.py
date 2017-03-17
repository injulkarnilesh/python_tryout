
people = { "Harry" : 45, "Ron" : 33, "Hermione" : 39 }

print(people, type(people))
print(people.keys(), type(people.keys()))
print(people.values(), type(people.values()))

print(people["Harry"])

#not a list
#people.keys()[0]
#peope.values()[2]

print(list(people.keys())[1])
print(list(people.values())[0])

#error
#print(people["Voldemort"])

people["Ron"] = 34
print(people["Ron"])

people["Severus"] = 90
print(people)

people["Dumbledore"] = "TOO OLD"
print(people)

they = { "US" : ["Alex", "001", 12], "IN" : ["Nilesh", "003", 43] }
print(they["IN"][1:])

westeros = {
        "Tyrian" : { "House" : "Lannister", "Age" : 39, "Alive" : True },
        "Ned" : { "House" : "Stark", "Age" : 54, "Alive" : False },
        "Jon" : { "House" : "Stark", "Age" : 31, "Alive" : False },
        "Lyanna" : {"House" : "Bear Island", "Age" : 14, "Alive" : True }
    }
print(westeros["Lyanna"]["House"])
print(westeros)
westeros["Jon"]["Alive"] = True
print(westeros)
westeros["Davos"] = {"House" : "Seaworth", "Age" : 65, "Alive" : True }
print(westeros)


