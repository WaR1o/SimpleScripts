# Create a function that will return a list of fibonacci numbers
fibon_list = []
def fibon(rang):
    global fibon_list
    a, b = 0, 1
    for i in range(rang):
        fibon_list.append(a)
        a, b = b, a + b
        
    return fibon_list

fibon(5000)

# Check if 10000 - opacity is in fibonacci number list, return its index
def check_age(opacity):
    default = 10000
   
    for n in range(5000):
        if n in fibon_list:
            default -= n
            print(str(n) + ' is fibbonaci number, so default = ' + str(default))
            if default == opacity:
                return n
        else:
            default += 1
            print(str(n) + ' isn\'t fibbonaci number, so default = ' + str(default))
            if default == opacity:
                return n
    


print(check_age(9990))
    
        
