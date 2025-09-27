#BASIC INTRO TO PYTHON
message = "hello python world"
print(message)
message = "hello Python Crash Course World!"
print(message)
name = "ada lovelace"
print(name.title())
print(name.lower())
print(name.upper())
first_name="ada"
last_name="lovelace"
full_name=f"{first_name}{last_name}"
print(full_name.lower())
print(f"hello there,{full_name.title()}!")#method for capitalization
message=f"Hola, {full_name.title()} of the house of warriors!"
print("message")
print("\tPython")#\t is space to the left
print("languages:\nEnglish\nFrench\nSpanish") #\n is line break
print("PROLANGS:\n\tPython,\n\tHTML,\n\tcss,\n\tjavascript") #combination of both
favourite_lang = "  python   "
print(favourite_lang)
print(favourite_lang.rstrip())#removes white spaces to the right
print(favourite_lang.lstrip())
print(favourite_lang.strip())
nostarch_url = "https:\\nostarch.com"
link=nostarch_url.removeprefix("https:\\")
print(link)
universal_age = 14_000_000
print(universal_age)
x,y,z=9,2,6
print(x,y,z)
import this #this will print the zen of python
MAX_CONNECTIONS = 300 #all caps variables are constant
#EXERCISE 2-10
my_num = 9
hello = f"Your favourite number is {my_num}"
print(hello)

