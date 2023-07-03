"""You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa."""


def swap_case(s):
    s1 = ""
    for i in range(len(s)):
        if (s[i].isupper()):
            s1 += s[i].lower()
        elif (s[i].islower()):
            s1 += s[i].upper()
        else:
            s1 += s[i]
    return s1


s = input()
result = swap_case(s)
print(result)
