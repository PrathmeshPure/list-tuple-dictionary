#dictionaries
'''
this is a data structure used to map keys to values
dictionaries can be indexed in the same way as lists
'''
dictionary_={"key1":"value1","key2":"value2","name":"prathmesh"}
print(dictionary_["name"])
#prathmesh

#values may be number, string ,or may be list also 
dictionary_2={"samsung":["s7","s8","s9"],"apple":[6,7,"x"]}
print(dictionary_2["samsung"])
#['s7', 's8', 's9']
print(dictionary_2["apple"])
#[6, 7, 'x'] 

#we can simply add keys by assignment
dictionary_2["xiomi"]=["a1","a2",]
#{'samsung': ['s7', 's8', 's9'], 'apple': [6, 7, 'x'], 'xiomi': ['a1', 'a2']}

#we can append items in dictionary
dictionary_2["apple"].append("7plus")
dictionary_2
#{'samsung': ['s7', 's8', 's9'], 'apple': [6, 7, 'x', '7plus'], 'xiomi': ['a1', 'a2']}

#we can get keys in dictionry by key()
print(dictionary_2.keys())
#dict_keys(['samsung', 'apple', 'xiomi'])


#delete xiomi
del dictionary_2['xiomi']
print(dictionary_2)
#{'samsung': ['s7', 's8', 's9'], 'apple': [6, 7, 'x', '7plus']}

#we can remove all entries from dictionary by clear()
dictionary_2.clear()
print(dictionary_2)
#{}