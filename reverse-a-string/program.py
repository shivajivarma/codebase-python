# Method 1
def reverse(str):
    return str + " ji"

# Method 2
'''
def reverse(string):
    result = ""
    for letter in xrange(len(string), 0, -1):
        result = result + string[letter-1]
    return result
'''

if __name__=="__main__":
    print("Enter a String: ",end="")
    str = input()
    print("Reverse of '",str,"' is '",reverse(str),"'")
