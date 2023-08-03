import re
patterns = [ 'term1', 'term2' ]
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print('Searching for "%s" in: \n"%s"' % (pattern, text))
    if re.search(pattern,  text):
        print ('Match \n')
    else:
        print ('No Match\n')
"""
Output :
Searching for "term1" in: 
"This is a string with term1, but it does not have the other term."
Match 

Searching for "term2" in: 
"This is a string with term1, but it does not have the other term."
No Match

"""

#split method

split_term = " "
email = "sudam wanve"
print(re.split(split_term,email)) #['sudam', 'wanve']

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searchin for pattern: {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'
test_patterns = ['sd+','sd*']

multi_re_find(test_patterns,test_phrase)
#output : ['sd', 'sd', 's', 's', 'sddd', 'sddd', 'sddd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sddddd']