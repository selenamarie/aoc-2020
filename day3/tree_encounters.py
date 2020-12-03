

location = 0
tree_count = 0

move_right = 1
down = 2
line_num = 0

with open("input.txt") as data: 
	for line in data: 
		line_num += 1
		if (line_num % down) == 0:
			continue
		print location, line[location], line_num
		if line[location] == "#":
			tree_count += 1
		location = (location + move_right) % (len(line) - 1 )

print tree_count
