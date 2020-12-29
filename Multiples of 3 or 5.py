def solution(number):
    a = []
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            a.append(i)
        elif i % 3 == 0 or i % 5 == 0:
            a.append(i)
    return sum(a)
