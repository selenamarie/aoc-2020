

data = open("data.txt", "r")

with open("data.txt") as data:
	all_data = [int(line.rstrip()) for line in data]

def determine_again(x, y, new_list_data):
	for z in new_list_data:
		if z == y:
			next
		adding = x + y + z
		if adding == 2020:
			print x, y, z
			print x * y * z
			return 1
	


# try to figure out which things added together = 2020
def determine(x, list_data):
	for i in list_data:
		adding = x + i
		if adding > 2020:
			next
		else:
			if not determine_again(x, i, list_data):
				next
			else: 
				return 1

# naive
while all_data:
	x = all_data.pop()
	if not determine(x, all_data):
		next
	else: 
		break


