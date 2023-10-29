def matchingStrings(strings, queries):
    # Write your code here
    res = []
    for q in queries:
        arr = [x for x in strings if x == q]
        res.append(len(arr))
    return res