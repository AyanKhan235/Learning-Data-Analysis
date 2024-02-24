# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.

import re 
text="The rain is Spain"
x=re.search("^The.*Spain$", text)
if x:
    print("YES ! we have match")
else:
    print("No ! we have not match")

