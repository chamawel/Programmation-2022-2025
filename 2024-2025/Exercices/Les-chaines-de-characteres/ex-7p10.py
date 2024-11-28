string          : str = "radar"
upside_down_str : str = ""

for i in string:
    upside_down_str = i + upside_down_str

if upside_down_str == string:
    print("C'est un palindrome")

else:
    print("Ce n'est pas un palindrome")
