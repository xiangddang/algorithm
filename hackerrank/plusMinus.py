def plusMinus(arr):
    # Write your code here
    n = len(arr)
    positive = negative = zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    print("%.6f" % (positive / n))
    print("%.6f" % (negative / n))
    print("%.6f" % (zero / n))