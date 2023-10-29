def caesarCipher(s, k):
    # Write your code here
    res = []
    for i in s:
        if i.isalpha():
            if i.isupper():
                res.append(chr((ord(i) - ord("A")+ k) % 26 + ord("A")))
            else:
                res.append(chr((ord(i) - ord("a")+ k) % 26 + ord("a")))
        else:
            res.append(i)
    return ''.join(res)