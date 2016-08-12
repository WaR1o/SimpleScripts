import re

# choose every bracket in the expression and put it to the list
expression = "((5+3)*2+1)"
#( or [ or { any symbols except another closing bracket and then same closing bracket
#expression matches 3 different regexes like
regex1 = re.compile('\(+[\d\+\-\*\/]*\)+')
regex2 = re.compile('\[+[\d\+\-\*\/]*\]+')
regex3 = re.compile('\{+[\d\+\-\*\/]*\}+')
#regex = re.compile('[\([^\]\}]
patt1 = re.match(regex1, expression)
patt2 = re.match(regex2, expression)
patt3 = re.match(regex3, expression)
print(patt1)
print(patt2)
print(patt3)            
symbols = "()[]{}"
open_symbol = "([{"
close_symbol = "(]}"
stripped = ""
for x in expression:
    if x in symbols:
        stripped += x
if stripped.count('(') == stripped.count(')') and stripped.count('[') == stripped.count(']') and stripped.count('{') == stripped.count('}'):
    print('Matched')
    #return True
else:
    print('wrong')
    #return False
#print(stripped.count('('))
    
#def checkio(expression):
    
    # for loop checks that every open bracket in the list should have closing bracket
    #return True or False


"""#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem" """
