One By 2 Power N
================

> Program to find exact value of 1/(2^n).

###Sample
```
Enter a number (n) : 15
1/(2^n) = 0.000030517578125
```

###CODE
```python
def oneBy2PowerN(N):
    b = pow(5,N)
    l = N - len(str(b))
    output = "0."
    for j in range(0, l):
        output = output + "0"
    return output + str(b)
```

With love,  
_Shivaji Varma_
