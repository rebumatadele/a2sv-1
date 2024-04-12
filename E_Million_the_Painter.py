n = int(input())
string  = input()
if 'CC' in string or 'YY' in string or 'MM' in string:
    print("No")
elif string[0] == "?" or string[-1] == "?" or "C?C" in string or "M?M" in string or "Y?Y" in string or "??" in string:
    print("Yes")
# if one ? is at the middle and 
else:
    print("No")