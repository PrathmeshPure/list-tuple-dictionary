#tuples
'''
tuples are similar to lists,except that they can not be changed.
tuples are created using ().
tpl=()  creates empty tuple
'''
tuple_=("this","is","tuple",)
print(tuple_)
#('this', 'is', 'tuple')
print(tuple_[0])
#this
print(tuple_[1])
#is
print(tuple_[2])
#tuple

'''tuple can be created without () just by simply specifying items
 seperated by comma'''

tuple_2=0,"one",2,"three"
print(tuple_2)
#(0, 'one', 2, 'three')

#we can add tuples by following way
tuple_3=tuple_2+tuple_
print(tuple_3)
#(0, 'one', 2, 'three', 'this', 'is', 'tuple')

#creating nested tuples
tuple_4=(0,1,2,("three","four"),4)
print(tuple_4)
#(0, 1, 2, ('three', 'four'), 4)
print(tuple_4[3])
#('three', 'four')

#accesing nested tuples elements
print(tuple_4[3][0])
#three
  
print(len(tuple_4))
#5
