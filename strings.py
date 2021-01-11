# New comment
# Another comment
# import os

print('Hello   World')
message = 'Hello World'
print(message)
# Embedded Quote

print(message)
print("Bobby's World")


print('Bobby\'s World')
# multiline triple quotes '''
message2 = '''Hello World was a
good place to
hang out'''
print(message2)

# characters in a string

print(len(message))
print(len(message2))

# Access characters in string, index starting by 0 last  = -1
# Sliceing strings
print(message[0])
print(message[-1])

# print range of characters

print(message[0:5])
# Start at 0 end at 4 (5 not inclusive)

print(message[:5])
print(message[6:])

# str methods
print(message.lower())
print(message.upper())

# Count occurances of substring
print(message.count('l'))
print(message.count('Hello'))

# find and replace substring
print(message.replace('l', 't'))
print(message.replace('World', 'Universet'))
print(message.find('l'))
