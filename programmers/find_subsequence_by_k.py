def solution(sequence, k):
    answer = []
    left = 0
    total = 0

    for right in range(len(sequence)):
        total += sequence[right]

        while total > k:
            total -= sequence[left]
            left += 1

        if total == k:
            answer.append([left, right])
    
    return min(answer, key=lambda x: (x[1]-x[0], x[0]))

    