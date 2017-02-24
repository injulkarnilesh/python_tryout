word = "supercalifragilisticexpialidocious"

print("Letter at index : ", word[0])
print("Letter at index : ", word[5])

print("Slice with start and end : ", word[5:17])
print("Siice wihout end : ", word[5:])
print("Siice wihout start : ", word[:9])

print("Slice with step : ", word[5:9:1])
print("Slice with step : ", word[5:17:2])
print("Slice with step : ", word[::2])

print("Slice with negative step : ", word[::-1])
print("Slice with negative index : ", word[-10:-1:1])
print("Slice with negative index and step : ", word[-1:-10:-1])
print("Slice with paritial negative index : ", word[-10:0:-1])
print("Slice with paritial negative index : ", word[5:0:-1])

print("Slice with out of bound index : ", word[0:100:1])

print("Index", word.index("super"))
print("Index", word.index("exp"))
print("Index", word.index("fragil"))
#error if substring not found
print("Index", word.index("xyxyxyxy"))
