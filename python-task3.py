print("##############################################")
print("TASK 1")
import ast
def calc_pol(pol_str, x = None):
   if x == None:
       text = "There is no value for x"
       result = text
   else:
       node = ast.parse(pol_str, mode='eval')
       code_object = compile(node, filename='<string>', mode='eval')
       result = eval(code_object)
       if result == 0:
           text = "Result = 0, so " + str(x) + " is a root of " + pol_str
           result = text
       else:
           text = "Result = "
           result = text + str(result)
   return result
a = calc_pol("2*x**2 + 3*x", )
print (a)

print("##############################################")
print("TASK 2")
def show_sequence(n):
    pass
    if n > 0:
        text = "0"
        i = 0
        sum = 0
        while i < n:
            i += 1
            text = text + "+" + str(i)
            sum += i
        out = text + " = " + str(sum)
    elif n < 0:
        out = str(n) + "<0"
    else:
        out = str(n) + "=0"
    return out

a = show_sequence(3)
print(a)

print("##############################################")
print("TASK 3")
def reverse(n):
    result = 0
    while n > 0:
        dec = n % 10
        n = n // 10
        result = result * 10
        result = result + dec
    return result

a = reverse(8552)
print(a)

print("##############################################")
print("TASK 5")
# your code
# fcn(21)/fcn(19) == fcn(19)/fcn(17)
# 4 == 4
# fcn(2) = 4
# n - power of 2

def fcn(n):
    if n >= 0:
        result = 2**n
    else:
        result = 'Error!'
    return result

a = fcn(10)
print(a)
