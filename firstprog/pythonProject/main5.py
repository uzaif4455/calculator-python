#dictionary in python
"""d1={}
print(type(d1))"""
"""d1={"Harry":"burger","rohan":"fish","skillf":"roti",
    "shubham":{"breakfast":"maggi","lunch":"vegetables","dinner":"chicken"}}
#print(d1["Harry"])
#print(d1["shubham"])
d1["Ankit"] = "tea"
d1[420]="kebabs"
del d1[420]
print(d1)
d2=d1.copy()
#del d2["Harry"]
#print(d2)
#print(d2.get("Harry")
d2.update({"leena":"toffee"})
print(d2)"""
#question: create a dictionary and take input from the user and return the meaning of the word from dictionary
print("Hello Welcome to uzaif's dictionary")
dictionary = {"mutable": "can be changed",
              "immutable": "cannot be changed",
              "inspire": "to motivate someone",
              "op": "over powered"}
enter = input("Enter word: ")
print("the meaning of the word is: ", (dictionary[enter]))

