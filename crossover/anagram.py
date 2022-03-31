first_string = input("Provide the first string: ")
second_string = input("Provide the second string: ")

if sorted(first_string) == sorted(second_string):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")