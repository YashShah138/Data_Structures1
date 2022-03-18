{% include navigation.html %}

# Data Structures Project Documentation

## Code Snippets
<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@YashShah49/Data_Structures1?embed=true"></iframe>

## Code / Runtime Links
[Repl](https://replit.com/@YashShah49/TT0-Menu#main.py)


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
