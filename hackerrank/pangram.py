def pangrams(s):
    # Write your code here
    s = s.replace(" ", "")
    s = s.lower()
    if len(set(list(s))) == 26:
        return "pangram"
    else:
        return "not pangram"