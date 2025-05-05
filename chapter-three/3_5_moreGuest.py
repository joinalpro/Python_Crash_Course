new_guest = ['panu']
new_guest.insert(0,'zishan')
print(new_guest)
new_guest.append('mamun')
print(new_guest)
print(f"All of you are invited {new_guest[0]}, {new_guest[1]}, {new_guest[2]}. \nI hope to see you soon!")

new_guest.pop()
print(f"All of you are invited {new_guest[0]}, {new_guest[1]}. \nI hope to see you soon!")

del new_guest[0]
print(new_guest)
del new_guest[0]
print(new_guest)