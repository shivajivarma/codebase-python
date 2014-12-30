def oneBy2PowerN(N):
    b = pow(5,N)
    l = N - len(str(b))
    output = "0."
    for j in range(0, l):
        output = output + "0"
    return output + str(b)

if __name__=="__main__":
    print("Enter a number (n) : ",end="")
    num = int(input())
    print("1/(2^n) =", oneBy2PowerN(num))
