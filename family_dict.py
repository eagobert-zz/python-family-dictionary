#Define a dictionary that contains information about several members of your family.

#Create a dictionary called "my_family" with the keys: mother and father, which hold dictionary objects in their values. 
my_family = {
    "mother": {
        "name": "Earline Agobert",
        "age": 58
    },
    "father": {
        "name": "Dwain Agobert",
        "age": 60
    }
}

# print the entire dictionary
print(my_family)

#loop thru dictionary and print for each key
for k, v in my_family.items():
    print("My " + k + " is " + v["name"])

#print the value of a specific key in the dictionary
print(my_family["mother"])
print(my_family["father"])

#print all keys in a dictionary
print("Keys: ", my_family.keys())

# print all values in a dictionary
print("Values: ", my_family.values())

#print all keys and values in a dictionary
print("Keys and Values: ", my_family.items())

#Using a dictionary comprehension, produce output that looks like the following example: "Krista is my sister and is 42 years old."
family = { value["name"] + " is my " + key + " and is " + str(value["age"]) + " years old." for (key, value) in my_family.items()}

print(family)


