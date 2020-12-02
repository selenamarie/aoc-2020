

total_good_passwords = 0

with open("input.txt") as data:
	(a, b, c) = zip(*[line.rstrip().split() for line in data])
	b = map(lambda s: s.strip(":"), b)
	for i in range(len(c)):
		# for the range, min X characters from b, max Y characters of b
		number_times = c[i].count(b[i])
		(x, y) = a[i].split("-")
		if int(x) <= number_times and int(y) >= number_times:
			total_good_passwords += 1
			

print total_good_passwords

