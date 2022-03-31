{% include navigation.html %}

# Data Structures Project Documentation

## Code Snippets
<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@YashShah49/Data_Structures1?embed=true"></iframe>

## Code / Runtime Links
[Repl](https://replit.com/@YashShah49/DataStructures1#.replit)

### Tech Talk 0
```
menu_options = {
	1: 'Swap',
	2: 'Animation',
	3: 'Loops',
	4: 'Fibonacci',
	5: 'Exit',
}

submenu_swap = {
	1: 'Number Swap', 
	2: 'Lesser Number 1st',
	3: 'Return',
	4: 'Exit',
}



def print_options():
  for key in menu_options.keys():
    print('\x1B[3m', key, '--', menu_options[key], '\x1B[0m' )
  runOptions1()

def print_sm_options():
  for key in submenu_swap.keys():
    print('\x1B[3m', key, '--', submenu_swap[key], '\x1B[0m' )
  runOptions2()

def print_sml_options():
  for key in submenu_loop.keys():
    print('\x1B[3m', key, '--', submenu_loop[key], '\x1B[0m' )
  runOptions2()
	
def runOptions1():
	while True:
    try:
      option = int(input('\n' + 'Select a number 1-3: '))
      if option == 1:
        print_sm_options()
      elif option == 2:
        smile()
      elif option == 3:
        print_sml_options()
      elif option == 4:
        fibonacci()
      elif option == 5:  
        print('Goodbye!')
          exit() 
      else:
        print('Invalid input. Please enter a number between 1 - 3.')
  except ValueError:
      print('Invalid input. Please enter an integer input.')

def runOptions2():
  while True:
    try:
       option = int(input('Select a number 1-4: '))
      if option == 1:
          swap()
      elif option == 2:
          lessnumswap()
      elif option == 3:
          print("Returning to the main menu")  
          runOptions1()
      elif option == 4:
          print('You will now exit the menu')
          exit() 
      else:
          print('Invalid option. Please enter a number between 1 - 4.')
  except ValueError:
      print('Invalid input. Please enter an integer input.')
```


### Tech Talk 1
```
InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Yash",  
               "LastName": "Shah",  
               "DOB": "May 25",  
               "Residence": "San Diego",  
               "Email": "yashjshah138@gmail.com",  
               "Owns_Cars":["2019 Bugatti Divo","2020 Rolls Royce Cullinan","2022 Porsche GT4 RS","2022 Lamborghini Aventador STO", "Ferrari 296 GT3"]  
              })  

InfoDb.append({  
               "FirstName": "Liam",  
               "LastName": "Neesom",  
               "DOB": "June 7",  
               "Residence": "New York",  
               "Email": "liamneeson@gmail.com",  
               "Owns_Cars":["2019 Ford F-250 Heavy Duty","2018 Ferrari 488","Subaru WRX STI"]  
              })

InfoDb.append({  
               "FirstName": "Ryan",  
               "LastName": "Reynolds",  
               "DOB": "October 23",  
               "Residence": "Los Angeles",  
               "Email": "sexyryan@gmail.com",  
               "Owns_Cars":["Toyota Prius","Tesla Model S","Lamborghini Aventador"]  
              })

InfoDb.append({  
               "FirstName": "Jeff",  
               "LastName": "Bezos",  
               "DOB": "January 12",  
               "Residence": "Maui",  
               "Email": "kingjeff@gmail.com",  
               "Owns_Cars":["Koenigsegg CCXR Trevita","Bugatti Veyron Mansory","Lamborghini Veneno Roadster", "Ferrari Pininfarina Sergio", "Lykan HyperSport"] 							})

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

def for_loop(n):
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
def fibonacci():
  num = int(input("Enter sequence length: "))
  if num < 0:
    print("Enter a number greater than 0")
  else:
    for n in range(num):
      print(print_fib(n))

def print_fib(i):
  if i <= 1:  
     return i  
  else:  
     return(print_fib(i-2) + print_fib(i-1))
```
### Crossover
anagram.py
```
first_string = input("Provide the first string: ")
second_string = input("Provide the second string: ") 

if sorted(first_string) == sorted(second_string):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")
```

addition.py
```
# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
```

subtraction.py
```
# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Subtract two numbers
difference = float(num1) - float(num2)

# Display the difference
print('The difference of {0} and {1} is {2}'.format(num1, num2, difference))
```

multiplication.py
```
# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Multiply two numbers
product = float(num1) * float(num2)

# Display the product
print('The product of {0} and {1} is {2}'.format(num1, num2, product))
```

division.py
```
# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Divid two number
quotient = float(num1) / float(num2)

# Display the quotient
print('The quotient of {0} and {1} is {2}'.format(num1, num2, quotient))
```
