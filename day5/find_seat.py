

# FB, 7 char
# F = lower
# B = upper
# rows 0..127
rows = range(128)

# RL, 3 char
# R = upper
# L = lower
#  columns 0..7
columns = range(8)

# inputs a range and instruction
def bin_search(numbers, instruction):
	#print instruction
	#print numbers
	#print len(numbers)
	numbers_len = len(numbers)
	if instruction == "B" or instruction == "R":
		x = slice(numbers_len / 2, numbers_len)
		return(numbers[x])
	elif instruction == "F" or instruction == "L":
		x = slice(numbers_len / 2)
		return(numbers[x])

def find_row(seat_rows, row_instructions):
	for i in row_instructions:
		seat_rows = bin_search(seat_rows, i)
	return seat_rows[0]
		

def find_column(seat_columns, column_instructions):
	for i in column_instructions:
		seat_columns = bin_search(seat_columns, i)
	return seat_columns[0]


# seat id  row * 8 + column 
def seat_id(r, c):
	return r * 8 + c

rowslice = slice(7)
columnslice = slice(7, 10)

seats  = []
with open("input.txt") as data:
	for line in data:
		new_row = list(rows)
		new_column = list(columns)
		row_num = find_row(new_row, line[rowslice])
		column_num = find_column(new_column, line[columnslice])

		seats.append( seat_id(row_num, column_num))


def diff_lists(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

seats.sort()
all_seats = range(32, 913)

print diff_lists(all_seats, seats)

#print seats[-1]

