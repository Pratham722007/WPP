def ispangram(s):
    s = s.replace(" ", "").lower()
    sorts_1=sorted(s)
    set_1=set(sorts_1)
    if(len(set_1)==26):
        return True
    else:
        return False
s=input()
if(ispangram(s)):
    print("it is a pangram")
else:
    print("it is not a pangram")
