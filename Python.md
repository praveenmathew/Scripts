For easy reference:- 
```
https://www.teclado.com/30-days-of-python/python-30-day-0-getting-set-up
```

Python Basic I/O
```
print(30)
print("My age is 30")

age = 31
print("My age next year will be ",age)

print("What is your age?")
x = input()
print (x)

name = input("What is your name?")
print(name)
```

Supplying arguments inside print()
```
title = "Joker"
director = "Todd Philips"
release_year = 2019

print(title + "  (" + str(release_year) + ")," + "  directed by " + director)
#or
print(f"{title} ({release_year}), directed by {director}")
```


List [] and Tuples () 

```
movies = [
         (
         "sky", 
         "Nolan",
         2030,
         "$100"
         ),
         (
          "Batman",
          "Jogn",
          2024,
          "$200"
          )
         ]

second = (input("title: "), input("director: "), input("year: "), input("budget: "))

print(movies)

movies.append(second)
print(movies)
movies.pop(0)
print(movies)
```


Supplying elements from a list/tuple to a print(). It differs for string and int elements. 
```
numbers = [1,2,3,4,5]
print (numbers)
new_number = []
for i in numbers:
    new_number.append(str(i))
    
print (f"The numbers are: {','.join(new_number)}")
```
