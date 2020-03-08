

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
assert 5==5
assert 4!=6
assert type(True), 'bool'
x= 5
y= 5
z= 8
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

'''

