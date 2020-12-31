def longest_repetition(s):
    max_re = 1
    max_abs = 1
    if len(s) == 0:
        return tuple(['', 0])
    else:
        part = s[0]
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            max_re += 1
            if max_re > max_abs:
                max_abs = max_re
                part = s[i]
            elif max_re == max_abs:
                max_abs = max_re
                
        
        else:
            max_re = 1
            
    a = tuple([part, max_abs])
    return a

print(longest_repetition('aabb'))
