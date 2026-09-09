import re

with open("preproinsulin-seq.txt") as f:
    text = f.read()

text = text.replace("ORIGIN", "").replace("//", "")
cleaned = re.sub("[^a-zA-Z]", "", text)

print(cleaned)
print(f"Length: {len(cleaned)}")
