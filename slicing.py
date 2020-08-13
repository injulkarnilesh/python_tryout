word = "supercalifragilisticexpialidocious"

print("Letter at index : ", word[0]) #s
print("Letter at index : ", word[5]) #c

print("Slice with start and end : ", word[5:17]) #califragilis 17th excluded
print("Siice wihout end : ", word[5:]) #califragilisticexpialidocious
print("Siice wihout start : ", word[:9]) #supercali

print("Slice with step : ", word[5:9:1]) #cali
print("Slice with step : ", word[5:17:2]) #clfaii
print("Slice with step : ", word[::2]) #sprairglsiepaioiu

print("Slice with negative step : ", word[::-1]) #suoicodilaipxecitsiligarfilacrepus
print("Slice with negative index : ", word[-10:-1:1]) #alidociou
print("Slice with negative index and step : ", word[-1:-10:-1]) #suoicodil
print("Slice with paritial negative index : ", word[-10:0:-1]) #aipxecitsiligarfilacrepu
print("Slice with paritial negative index : ", word[5:0:-1]) #crepu

print("Slice with out of bound index : ", word[0:100:1]) #supercalifragilisticexpialidocious

print("Index", word.index("super")) #0
print("Index", word.index("exp")) #20
print("Index", word.index("fragil")) #9
#error if substring not found
print("Index", word.index("xyxyxyxy")) #ValueError: substring not found
