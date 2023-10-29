def superDigit(n, k):
    # Write your code here
    sum_digit = sum(int(i) for i in n)
    sum_digit *= k
    return sum_digit if len(str(sum_digit)) == 1 and k == 1 else superDigit(str(sum_digit), 1)