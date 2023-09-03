def golomb(n):
    print('recursion')
    if n == 1:
        return 1

    return 1 + golomb(n - golomb(golomb(n - 1)))


def golomb_optimised(n, memo={}):
    print('recursion optimised')
    if n == 1:
        return 1

    if not memo.get(n, False):
        memo[n] = 1 + golomb_optimised(
            n - golomb_optimised(golomb_optimised(n - 1, memo), memo), memo)
    return memo[n]


print(golomb(4))  # 19 calls for N = 4
print(golomb_optimised(4))  # 10 calls for N = 4
