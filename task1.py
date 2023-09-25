from collections import Counter

def solution(collection):
    couters = Counter(collection)
    if not collection:
        return 0
    rv = couters.most_common(5)
    return rv[0][1]


print(solution([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]))
print(solution())
