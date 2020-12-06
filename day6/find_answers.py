

def common_answers(answers_list):
	# figure out which letters are in all answers
	length = len(answers_list)
	b = answers_list.pop()
	if length == 1:
		print len(b)
		return len(b)
	for a in answers_list:
		print "list:", answers_list
		b = set(a).intersection(b)
		print "for loop set b", b, "length b", len(b)
		if b == None:
			return 0
	print "set b", b, "length b", len(b)
	return len(b)

answers_count = []
with open("test.txt") as data:
	answers = []
	for line in data:
		if line == "\n":
			print answers
			count = common_answers(answers)
			answers_count.append(count)
			answers = []
		else: 
			answers.append(line.rstrip())


count = common_answers(answers)
answers_count.append(count)
print sum(answers_count)
