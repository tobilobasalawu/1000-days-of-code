'''
myDictionary = {"names" : "Ian", "health" : 219, "strength" : 199, "equipped" : "Axe"}

for name, values in myDictionary.items():
    print(f"{name} : {values}")

'''
name = input("name: ")
url = input("url: ")
desc = input("desc: ")
rating = input("rating: ")

web = {'name': name, 'url': url, 'desc': desc, 'rating': rating}

for key, values in web.items():
    print()
    print(f'{key}: {values}')

#print(example)