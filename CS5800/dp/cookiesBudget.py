'''
You have a budget of B dollars and want to buy as many cookies as possible from a bakery. 
The bakery offers n different types of cookies, each priced at c1, c2, . . . , cn dollars 
(you can assume ci > 0 for all i). Design an efficient algorithm that determines the maximum number of cookies 
you can purchase while spending all of your money. If it is not possible to spend all of the B dollars, 
the algorithm should return “Impossible”.
For example if there are two types of cookies priced c1 = 2 and c2 = 5, and you have a budget of B = 9 dollars, 
you can buy a maximum of three cookies (one of the second type and two of the first type).
'''

def cookiesBudget(B, C):
    # Initialize the dp array, using '-1' to tag 'impossible'
    budget = [-1] * (B+1)
    budget[0] = 0
    
    # Preprocessing coins make it in asscending order
    C.sort()

    for i in range(1, B+1):
        for cookie in C:
            if cookie == i or (cookie < i and budget[i - cookie] != -1):
                budget[i] = max(budget[i], budget[i - cookie] + 1)

    return budget[B] if budget[B] != -1 else 'Impossible'

B = 9
C = [2, 5]
result = cookiesBudget(B, C)
print(result) # Output: 3

B = 11
C = [2, 5]
result = cookiesBudget(B, C)
print(result)  # Output: 4

B = 7
C = [2, 3, 5]
result = cookiesBudget(B, C)
print(result)  # Output: 3 

B = 10
C = [2, 3, 7]
result = cookiesBudget(B, C)
print(result)  # Output: 5