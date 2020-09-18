#calculator.py

def sum(m,n):
	tot = m
	for i in (0, n):
		if (n > 0):
			tot = tot + 1
		else: 
			tot = tot - 1
	return tot

def divide(m,n):
	# if (m == 0):
		# raise ZeroDivisionError
		
	leftovers = m
	isNegative = m<0 and n>0 or m>0 and n<0

	m=abs(m)
	n=abs(n)
	result = 0
	
	while (m - n) >= 0:
		result = result + 1
			
	
	return -result if isNegative else result