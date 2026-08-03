str1="this is a string.we are creating string in python"
print(str1)
#concatenation of strings
str2="artificial"
str3="intelligence"
print("concatenation of str2 and str3:", str2 + " " + str3)
#length of string
print("length of str2=",len(str2))
print("length of str3=",len(str3))
#indexing 
print("character at index 3 of str1:",str1[3])
#slicing
print("slicing str1 from index 5 to 9:",str1[5:9])
print("slicing str1 from start to index 4:",str1[:4])
print("slicing str1 from index 10 to end:",str1[10:])
#string functions
print("endswith 'python' or not:",str1.endswith("python"))
print("startswith 'It' or not:",str1.startswith("It"))
print("capitalize str1:",str1.capitalize())
print("replace 'string' with 'text' in str1:",str1.replace("string","text"))
print("find 'creating' in str1:",str1.find("creating"))
print("count of 'string' in str1:",str1.count("string"))
