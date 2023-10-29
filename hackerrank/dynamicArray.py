def dynamicArray(n, queries):
    # Write your code here
    last = 0
    arr = [[] for _ in range(n)]
    ans = []

    for q in queries:
        if q[0] == 1:
            idx = (q[1] ^ last) % n

            arr[idx].append(q[2])
        else:
            idx = (q[1] ^ last) % n
            second = q[2] % len(arr[idx])
            last = arr[idx][second]
            ans.append(last)

    return ans