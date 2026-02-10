#Tuple
#A tuple is an immutable type of a list(It cannot change)
#To introduce a tuple,we use the parenthesis()

counties = ("Nairobi", "Mombasa", "Kisumu", "Kisii", "Kitale", "Kiambu")
print(counties)

#slicing of tuples
print(counties[3:])

#accessing items of a tuple by use of the indexes
print(counties[5])

#Note:Below will  generate an error
#Attribute error
counties.append("Machakos")
print(counties)