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
