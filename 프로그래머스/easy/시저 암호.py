def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = (ord(s[i]) - ord("A") + n)
            s[i] = chr((s[i] % 26 ) + ord("A"))
        elif s[i].islower():
            s[i] = (ord(s[i]) - ord("a") + n)
            s[i] = chr((s[i] % 26 ) + ord("a"))
    return "".join(s)

assert "e F d" == solution("a B z", 4)
assert "BC" == solution("AB", 1)
assert "a" == solution("z", 1)
