# Python lists

#Ex1:Print the second item in the fruits list.
fruits=["apple","banana","cherry"]
print(fruits[1])
#Ex2:Change the value from "apple" to "kiwi", in the fruits list.
fruits[0]="kiwi"
#Ex3:Use the append method to add "orange" to the fruits list.
fruits.append("orange")
#Ex4:Use the insert method to add "lemon" as the second item in the fruits list.
fruits.insert(1,"lemon")
#Ex5:Use the remove method to remove "banana" from the fruits list.
fruits.remove("banana")
#Ex6:Use negative indexing to print the last item in the list.
print(fruits[-1])
#Ex7:Use a range of indexes to print the third, fourth, 
#and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#Ex8:Use the correct syntax to print the number of items in the list.
print(len(fruits))

# Python tuples

#Ex1:Use the correct syntax to print 
#the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#Ex2:Use the correct syntax to print the number 
#of items in the fruits tuple.
print(len(fruits))
#Ex3:Use negative indexing to print 
#the last item in the tuple.
print(fruits[-1])
#Ex4:Use a range of indexes to print the third, 
#fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

# Python sets
#Ex1:Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#Ex2:Use the add method to add "orange" to the fruits set.
fruits.add("orange")
#Ex3:Use the correct method to add 
#multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#Ex4:Use the remove method to remove 
#"banana" from the fruits set.
fruits.remove("banana")
#Ex5:Use the discard method 
#to remove "banana" from the fruits set.
fruits.discard("banana")

# Python dicts
#Ex1:Use the get method to print the value of the 
#"model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#Ex2:Change the "year" value from 1964 to 2020.
car["year"]=2020
#Ex3:Add the key/value pair 
#"color" : "red" to the car dictionary.
car["color"]="red"
#Ex4:Use the pop method
#to remove "model" from the car dictionary.
car.pop("model")
#Ex5:Use the clear method to
#empty the car dictionary.
car.clear()

# Python while

#Ex1:Print i as long as i is less than 6.
i = 1
while i < 6:
  print(i)
  i += 1
#Ex2:Stop the loop if i is 3
i = 1
while i < 6:
  if i == 3: 
    break
  i += 1
#Ex3:In the loop, when i is 3,
#jump directly to the next iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#Ex4:Print a message once the condition is false.
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Python for

#Ex1:Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#Ex2:In the loop, when the item value is "banana",
#jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#Ex3:Use the range 
#function to loop through a code set 6 times.
for x in range(6):
  print(x)
#Ex4:Exit the loop when x is "banana".

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      break
  print(x)
