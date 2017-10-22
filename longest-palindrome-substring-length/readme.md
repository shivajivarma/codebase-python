[Longest Palindrome Sub String Length](http://shivajivarma.com/code-base/2014/12/30/longest-palindrome-substring-length/)
===============

> Program to compute length of longest sub string which is palindrome.

### CODE
```python
def maxPalindromeSubStringLen(str):
	leng = 0
	ext = 0
	
	while(len(str)>0):
		if(str.count(str[0])%2==0):
			leng = leng + (str.count(str[0]))
		else:
			leng = leng + (str.count(str[0])) - 1
			ext = 1
		str = str.replace(str[0],"")
		
	return leng + ext
```

:+1:
