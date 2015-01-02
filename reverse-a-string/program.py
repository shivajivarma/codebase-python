# Method 1
def reverse(str):
    return str[::-1]

# Method 2
'''
def reverse(string):
    result = ""
    for letter in xrange(len(string), 0, -1):
        result = result + string[letter-1]
    return result
'''
