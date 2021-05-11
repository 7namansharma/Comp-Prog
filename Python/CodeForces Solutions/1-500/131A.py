s = input()
if s==s.upper() or (('a'<=s[0]<='z') and (s[1:]==s[1:].upper())):
    if s==s.upper():
        print(s.lower())
    else:
        print(s.capitalize())
else:
    print(s)
