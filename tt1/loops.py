# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Yash",  
               "LastName": "Shah",  
               "DOB": "May 25",  
               "Residence": "San Diego",  
               "Email": "yashjshah138@gmail.com",  
               "Owns_Cars":["Mk3 Supra", "Porsche GT4 RS"]  
              })

InfoDb.append({  
               "FirstName": "John",  
               "LastName": "Cena",  
               "DOB": "April 23",  
               "Residence": "Hollywood",  
               "Email": "johncena@gmail.com",  
               "Owns_Cars":["2022 Invisi-Mobile"]  
              }) 

InfoDb.append({  
               "FirstName": "Liam",  
               "LastName": "Neeson",  
               "DOB": "January 23",  
               "Residence": "San Diego",  
               "Email": "liamn@gmail.com",  
               "Owns_Cars":["2005 Ferarri FXX", "2005 Honda CRV"]  
              })  

InfoDb.append({  
               "FirstName": "Ryan",  
               "LastName": "Reynolds",  
               "DOB": "August 27",  
               "Residence": "Los Angeles",  
               "Email": "ryanr@gmail.com",  
               "Owns_Cars":["2022 Tesla Model X", "Bentley Bentayga"]  
              })  


# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

# this is test driver or code that plays when executed directly, versus import which will not run these statements
def tester1():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling for invalid input
def fibonacci():
  num = int(input("Enter the length of your Fibonacci sequence: "))
  if num < 0:
    print("You cannot use a negative number")
  else:
    # for loops lets recursive fibonacci loop print every number in a fibonacci sequence in a certain range "num"
    for i in range(num):
      print(recur_fibonacci(i))

# recursive loop that takes a number input, n, and returns the nth number in a fibonacci sequence
def recur_fibonacci(n):
  if n <= 1:  
     return n  
  else:  
     return(recur_fibonacci(n-2) + recur_fibonacci(n-1))
  
