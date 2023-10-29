#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    count = 0
    for i in range(len(q)-1, 1, -1):
        if q[i-2] > q[i-1]:
            q[i-2], q[i-1] = q[i-1], q[i-2]
            count += 1
        if q[i-1] > q[i]:
            q[i-1], q[i] = q[i], q[i-1]
            count += 1
        
        if q[i] != i + 1:
            print("Too chaotic")
            return
    print(count)
    return