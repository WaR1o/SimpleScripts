import re
 # create a set with lowercase letters
eq = re.compile('[a-z]')
text = "a" * 9000 + "b" * 1000
text = text.lower()
text_st = []
for i in text:
    if eq.match(i):
        text_st.append(i)
text_st = set(text_st)
print(text_st)
    # count all letters from the set in the text and put them in dict
text_dict = {}
for w in text_st:
    text_dict[w] = text.count(w)
print(text_dict)
    
    # check which letter have max count
maxCount = max(text_dict.values())
text_max_list = [k for k,v in text_dict.items() if v == maxCount]
text_max_list = sorted(text_max_list)
mwl = text_max_list[0]
return mwl
    
    # if some letters have the same count, append them to the list, sort it and return first item in that list
    
    #replace this for solution
    
