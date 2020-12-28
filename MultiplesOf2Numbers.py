# Python version: return multiples of 2 numbers in a list
def multiples(s1,s2,s3):
    a = []
    for i in range(1, s3):
        if i % s2 == 0 and i % s1 ==0:
             a.append(i)   
    return a
