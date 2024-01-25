"""
Pass a tuple to the divmod() function and obtain the quotient and the remainder.
"""
result = divmod(17, 3)
print(result)
tpl = (17, 3)
result = divmod(*tpl)
print(result)
