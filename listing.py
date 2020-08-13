people = [ "Nilesh", "Rahul", "Gaurav" ]
new_people = [ "Satish",  "Sangram" ]
people = people + new_people;
people[3] = "Karan"
print(people)
# ['Nilesh', 'Rahul', 'Gaurav', 'Karan', 'Sangram']

print(people[0], people[2]);
# Nilesh Gaurav

variant_list = ["Injulkar", 23, 3.4, "Kolhapur", True]
print(variant_list)
# ['Injulkar', 23, 3.4, 'Kolhapur', True]

name = input("What's your name ?").strip()
if name in people :
    print("Welcome back {}".format(name))
    remove_me = input("Would you like to remove yourself from list?").strip().lower()[0]
    if remove_me == 'y':
        people.remove(name)
    else:
        remove_index = input("Want to remove someone at index ? ").strip().lower()[0]
        if remove_index == 'y' :
            remove_index = int(input("What index? ").strip())
            if remove_index < len(people) and remove_index >=0 :
                del people[remove_index]
            else :
                print("Invalid index")
else :
    add_me = input("Would you like to add yourself ? ").strip().lower()[0]
    if add_me == 'y' :
        at_index = input("You have specific index in mind ? ").strip().lower()[0]
        if at_index =='y' :
            index = int(input("Enter index ?").strip())
            if index >= 0 and index <= len(people) :
                people.insert(index, name)
            else :
                print("Invalid index")
        else :
            people.append(name)
    
print(people)
                
                
