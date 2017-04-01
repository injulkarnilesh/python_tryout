from random import choice

number = 1
while number <= 10:
    if number % 2 == 0 :
        print(number)
    number += 1

questions = [ "Why is sky blue?", "Where are all the dinasours?",
              "How it rains?", "Does life has purpose?" ]
question = choice(questions)

answer = input(question).strip().lower();

while answer != "don't know" :
    answer = input("Why?").strip().lower();


#for

for i in range(1, 11, 2) :
    print(i)
    
vowels,consonants = 0,0
str = input("Your str ? ").strip().lower()
for ch in str :
    if ch in "aeiou" :
        vowels += 1
    elif ch == " " :
        pass
    else :
        consonants += 1

print("{0} number of vowels".format(vowels))
print("{0} number of consonants".format(consonants))

students = {
        "male" : [ "Frannk", "David", "Chris", "Tom" ],
        "female" : [ "Drew", "Monica", "Charlie" ]
    }
for key in students.keys() :
    for name in students[key] :
        if "a" in name :
            print(name)

even = [x for x in range(1, 101) if x % 2 == 0 ]
print(even)
print([x**2 for x in range(1, 11)])

words = [ "quick", "brown", "fox", "jumps", "over", "lazy", "dog" ]
print([ [w.lower(), w.upper(), len(w)] for w in words])

