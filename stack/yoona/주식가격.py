def solution(prices):
    answer = [i for i in range(len(prices) - 1, -1, -1)]

    stack = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    return answer
