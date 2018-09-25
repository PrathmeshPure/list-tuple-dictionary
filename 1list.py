#lists
'''lists are used to store an index list of items.
they are created using []
list index start from 0
'''
list_=["my","first","list"]
print(list_[0])		#my
print(list_[1])		#first
print(list_[2])		#list
print(list_[-1])	#list
print(list_[:-1])	#['my', 'first']     #slicing
'''
empty list is created by empty pair of square brackets
empty_list=[]

list may contain several different types and can also be nested
'''
list_2=[list_,1,["some","thing"],2.5]
print(list_2)
#[['my', 'first', 'list'], 1, ['some', 'thing'], 2.5]
print(list_2[0])
#['my', 'first', 'list']
print(list_2[1])
#1
print(list_2[2])
#['some', 'thing']
print(list_2[3])
#2.5
'''
>>>list_2[4]
>>>Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list_2[4]
IndexError: list index out of range
>>>
#this error occurs when you try to access list item which is not present
'''
#strings can be indexed like list
string_="hello prathmesh"
print(string_[6])	#this return character at specified index
#p
'''
#list operations
'''
#lists can be added and multiplied same as strings
list_3= list_ + list_2
print(list_3)
#['my', 'first', 'list', ['my', 'first', 'list'], 1, ['some', 'thing'], 2]

#items of list can be reassigned
list_3[4]=4
list_3[6]=6
print(list_3)
#['my', 'first', 'list', ['my', 'first', 'list'], 4, ['some', 'thing'], 6]

'''
list functions
''' 
#append method, inserts item at end
list_3.append("seven")
print(list_3)
#['my', 'first', 'list', ['my', 'first', 'list'], 4, ['some', 'thing'], 6,'seven']

#len function to get number of items in list
print(len(list_3))
#8

#insert item by index
list_3[3].insert(2,"nested")
print(list_3)
#['my', 'first', 'list', ['my', 'first', 'nested', 'list'],  4, ['some', 'thing'], 6, 'seven']

#poping item from list
list_3.pop(7)
print(list_3)
#['my', 'first', 'list', ['my', 'first','nested', 'list'], 4, ['some', 'thing'], 6]

#delete 
del list_3[6]
print(list_3)
#['my', 'first', 'list', ['my', 'first','nested', 'list'], 4, ['some', 'thing']]

#remove() removes item by value
list_3.remove("my")
print(list_3)
#['first', 'list', ['my', 'first','nested', 'list'], 4, ['some', 'thing']]

#we can sort the list using sort() in ascending
list_4=[3,2,4,8,5,6,1]
list_4.sort()
print(list_4)
#[1, 2, 3, 4, 5, 6, 8]
 
#to reverses the list use reverse()
list_4.reverse()
print(list_4)
#[8, 6, 5, 4, 3, 2, 1]

#max() and min()
max(list_4)
#8
min(list_4)
#1 
