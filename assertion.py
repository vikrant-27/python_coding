# General meaning of Assertion is stating facts Confidently or a statement that is strongly believed is True.
#
#
# 3.2 Assertion in Python
# Assertions in python are simple boolean expressions that check if the condition is True or False.
#
# If the condition in the assertion is evaluated to be True then it will do nothing and execute the code,if the condition in the assertion is False
# then it will throw an error and the program stops.
#
#
# 3.3 assert statement
# Assertion in python is achieved by using assert statement.
#
#
# Syntax:
#
#
# assert expression,message
#
def division(n,d):

    assert d!=0,"denominator cant be zero"
    div=n/d
    print("division is : ",div)
division(9,0)
