#"leet**cod*e"
stack = []
for letter in "leet**cod*e":
    if letter not in "*":
        stack.append(letter)
        continue
    stack.pop()
newstring = ''.join(stack)
print(newstring)

