# import re
# sequence ='''banglore is capital of karnataka the silicon city of india is banglore 
# bangaluru was called garden city because of its greenary'''
# pattern = "bangalore"
# replacement ="bangaluru"

# print(re.sub(pattern, replacement,sequence))

import re
sequence = '''banglore is capital of karnataka the silicon city of india is bangalore 
bangaluru was called garden city because of its greenary'''
pattern = "bangalore"
replacement = "bangaluru"

sequence=re.sub(pattern, replacement, sequence )
print(sequence)
