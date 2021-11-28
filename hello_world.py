# W3 Schools
print("Hello World!")
# if 5>2:
#     print("five is gretaer than 2")
# x=7
# y="juliet is learning python"
# X=8
# Y="Learning continues"
        # print(x+X)
        # print(y)
# PDF Learning

# message = 'Hello Python World!'
# print(message)

# message = "Hello Python Crash Course world!"
# print(message)

# message = "Hello Python Crash Course reader!"
# print(message)


# ALL ABOUT STRINGS
name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())

# CONCATENATION
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name)
message = "Hello, " + full_name.title() + "!"
print(message)

# WHITESPACES & NEW LINES IN A STRING
# no space
print('Python')
# for tab in text
print('\tPython')
# to add a newline
print("Languages:\nPython\nC\nJavaScript")
# newlines and tabs (producing f=different lines of output using 1 line of code)
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# stripping or removing a whitespace, we use the method strip(), for the right side is rstrip(), for the left side we use lstrip() and strip() for both sides.
# In the real world, stripping functions are used to clean up user inputs before storing in the program.
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)


# BEWARE OF SYNTAX ERRORS


# NUMBERS 
age = 23
message = 'Happy ' + str(age) + 'rd Birthday!'
print(message)

# LIST
bicycles = ['trek','cannondale','redline','specialized']
message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print(message)