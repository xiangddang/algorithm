#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    from collections import Counter
    c=list(Counter(s).values())
    if min(c)==max(c) or (min(c)==max(c)-1 and (sum(c)-1)/min(c)==len(c)) or (min(c)==1 and ((sum(c)-1)/max(c))==(len(c)-1)):
        return 'YES'
    else: 
        return 'NO'