def solution(s):
    if len(s) % 2 != 0:
        s += '_'
    if s =='':
        a = []
        return a
    elif len(s) % 2 == 0:
        a = []
        for i in range(0, len(s)-1, 2):
            a.append(s[i : i+2])
        return a
    
    elif len(s) % 2 != 0:
        a = []
        for i in range(0, len(s), 2):
            a.append(s[i : i+2])
        
        return a 
    
    pass
