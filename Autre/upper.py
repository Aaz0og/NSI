import re
import pyperclip
text = "They tryna be cray (Mm, yeah) They tryna be cray (Mm, yeah) She wanna meet Carti (Carti) That bitch is a Barbie (Yeah)"
patn = re.sub(r"[\([{})\]]", "", text)

pyperclip.copy(patn.upper())
