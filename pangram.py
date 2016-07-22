import re
    
def check_pangram(text):
    l1 = list('qwertyuiolpasdkjfhgzmnxcbv')
    t = text.lower()
    print(t)
    for n in l1:
        if n in list(t):
            l1.pop(l1.index(n))
            print(l1.index(n)
        if len(l1)< 1:
            return True
    return False


check_pangram("The quick brown fox jumps over the lazy dog.")

