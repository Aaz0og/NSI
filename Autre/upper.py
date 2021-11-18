import re
import pyperclip
text = str(input("?: "))
patn = re.sub(r"[\([{})\]]", "", text)

pyperclip.copy(patn.upper())
