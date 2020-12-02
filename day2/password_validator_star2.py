

total_good_passwords = 0

with open("input.txt") as data:
	(a, b, c) = zip(*[line.rstrip().split() for line in data])
	b = map(lambda s: s.strip(":"), b)
	for i in range(1,len(c)):
		# for the range, min X characters from b, max Y characters of b
		number_times = c[i].count(b[i])
		password = c[i]
		letter = b[i]
		(x, y) = a[i].split("-")
		first = int(x) - 1
		second = int(y) - 1
		if (first < len(password) and letter == password[first]) and not (second < len(password) and letter == password[second]):
			total_good_passwords += 1
		elif not (first < len(password) and letter == password[first]) and (second < len(password) and letter == password[second]):
			total_good_passwords += 1

print total_good_passwords

