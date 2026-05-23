# Type Content here...
text = input()

result = ""

for ch in text:
	if ch.isalnum() or ch == " ":
		result += ch

print(result)