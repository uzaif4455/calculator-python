#string slicing
#in python numbering starts from zero for the first letter here zero="m"
mystr="my name is uzaif"
print(len(mystr))
print(mystr[0:16])
#for advanced string slicing
"""here in the below program 0->starting letter "m", 5->total 5 character length shouldb be shown from the actual string,2-> 2 will give spacing and will not include letter between two count"""
#for reverse the string
print(mystr[::-1])
#for start from"m" till 5 characters count leaving 2 characters
print(mystr[0:5:2])
#for advance string slicing for negative
print(mystr[-16:16:])
# string functions
#1) here the below example will find is the string is continued without space  then true, here there are alpha numeric spaces
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("uzaif"))
print(mystr.count("a"))
print(mystr.capitalize())
print(mystr.find("is"))