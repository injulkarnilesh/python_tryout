
english = input("Say what? ").strip();
words = english.split(" ");

pig_latin= ""

for word in words :
    if word[0] in "aeiouAEIOU" :
        piggy_word = word + "yay"
    else :
        i = 0
        consonants = ""
        while (i < len(word)) and (word[i] not in "aeiouAEIOU") :
            consonants += word[i]
            i += 1
        if i < len(word) : 
            remains = word[i:]
            piggy_word = remains + consonants + "ay"
    pig_latin += piggy_word + " "

print(pig_latin.strip())

print("-".join(["Thank", "You"]))
