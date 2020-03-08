# If you are not sure what type a value has, the interpreter can tell you.
assert 'hello', 'str'
assert 10, 'int'
assert 3.1415, 'float'

# An assignment statement creates new variables and gives them values:
message = 'And now for something completely different'
assert message, 'str'

'''
Variable names can be arbitrarily long. They can contain both letters and numbers, but they cannot start with a number. It is
legal to use uppercase letters, but it is a good idea to begin variable names with a lowercase letter (you'll see why later).
The underscore character ( _ ) can appear in a name. It is often used in names with multiple words, such as my_name or
airspeed_of_unladen_swallow . Variable names can start with an underscore character, but we generally avoid
doing this unless we are writing library code for others to use.

Python reserves 33 keywords:
and del from None True
as elif global nonlocal try
assert else if not while
break except import or with
class False in pass yield
continue finally is raise
def for lambda return

A statement is a unit of code that the Python interpreter can execute. 

The operators + , - , * , / , //, %,  and ** perform addition, subtraction, multiplication, division,
 integer division, modulos and exponentiation. 
 Python follows mathematical convention for precedence order operators (PEMDAS)
 the + operator Cn be used to concatenation of strings
 
An expression is a combination of values, variables, and operators.

Sometimes we would like to take the value for a variable from the user via their keyboard. Python provides a built-in function
called input that gets input from the keyboard . When this function is called, the program stops and waits for the user to
type something. When the user presses Return or Enter , the program resumes and input returns what the user
typed as a string.

comments # Good variable names can reduce the need for comments, but long names can make complex expressions hard to read, so there
is a trade-off.

'''

# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
name = input("Name: ")
hours = float(input("Hours: "))
rate = float(input("Rate: "))
print("Pay " , hours * rate,  ' $ for ', name)

