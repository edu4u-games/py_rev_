'''
Boolean Expressions
A boolean expression is an expression that is either true or false.
True and False are special values that belong to the class bool ; they are not strings:
the comparison operators are:
x != y # x is not equal to y
x > y # x is greater than y
x < y # x is less than y
x >= y # x is greater than or equal to y
x <= y # x is less than or equal to y
x is y # x is the same as y
x is not y # x is not the same as y
'''
assert 5 == 5
assert 4 != 6
assert type(True), 'bool'
x = 5
y = 5
z = 8
assert x is y
assert x is not z

'''
Logical Operators
There are three logical operators: and , or , and not . The semantics (meaning) of these operators is similar to their
meaning in English.
Strictly speaking, the operands of the logical operators should be boolean expressions, but Python is not very strict. 
Any nonzero number is interpreted as "true."
'''
assert x > 0 and y < 10
assert x % 2 == 0 or z % 2 == 0
assert not (x > z)
assert 21 and True

'''
Conditional Execution
if - elif - else
'''
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

'''
Catching exceptions Using Try and Except
The idea of try and except is that you know that some sequence of instruction(s) may have a problem and
you want to add some statements to be executed if an error occurs. These extra statements (the except block) are ignored if
there is no error.

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
'''

'''
Short-Circuit Evaluation of Logical Expressions
When Python is processing a logical expression such as x >= 2 and (x/y) > 2 , it evaluates the expression from left
to right. Because of the definition of and , if x is less than 2, the expression x >= 2 is False and so the whole
expression is False regardless of whether (x/y) > 2 evaluates to True or False .
When the evaluation of a logical expression stops because
the overall value is already known, it is called short-circuiting the evaluation,  the short-circuit behavior leads to
a clever technique called the guardian pattern, for example preventing a zero division, like the code:
x >= 2 and y != 0 and (x/y) > 2
If y == 0 then the term (x/y) is not executed.
'''
'''
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate
 for hours worked above 40 hours and prevet it for ilegal imput. 
'''
while True:
    name = input("Name: ")
    try:
        hours = float(input("Hours: "))
        rate = float(input("Rate: "))
    except:
        print("Please enter a number")
    if hours > 40:
        extra_hours = hours - 40
        print("Pay ", 40 * rate + extra_hours * rate * 1.5, ' $ for ', name)
    else:
        print("Pay ", hours * rate, ' $ for ', name)
    if input("Type 'S' to exit.") == 'S':
        break
