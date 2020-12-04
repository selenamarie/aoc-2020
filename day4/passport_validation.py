
from pprint import pprint
import re

#    byr (Birth Year)
#    iyr (Issue Year)
#    eyr (Expiration Year)
#    hgt (Height)
#    hcl (Hair Color)
#    ecl (Eye Color)
#    pid (Passport ID)
#    cid (Country ID) optional

# 8 fields

good_passport = {
	'byr': 'required', 
	'iyr': 'required', 
	'eyr': 'required', 
	'hgt': 'required', 
	'hcl': 'required', 
	'ecl': 'required', 
	'pid': 'required', 
	'cid': 'optional'
}
good_passport_keys = good_passport.keys()
good_passport_keys.remove('cid')

def test_passport_keys(p):
	p_keys = p.keys()

	try: 
		p_keys.remove('cid')
	except:
		pass

	if set(p_keys) == set(good_passport_keys):
		return 1
	return 0


# validation for each value in a passport
def byr(value):
	if 1920 <= int(value) <= 2002:
		return 1
	else:
		return 0

def iyr(value):
	if 2010 <= int(value) <= 2020:
		return 1
	else:
		return 0

def eyr(value):
	if 2020 <= int(value) <= 2030:
		return 1
	else:
		return 0

def hgt(value):
	pattern = '(\d{2,3})(cm|in)'
	match = re.search(pattern, value)
	if match:
		(number, units) = match.groups()
		if units == 'cm':
			if 150 <= int(number) <= 193:
				return 1
		elif units == 'in':
			if 59 <= int(number) <= 76:
				return 1
	return 0

def hcl(value):
	hex = re.compile(r'^#[0-9a-fA-F]{6}$')
	m = re.search(hex, value)
	if m:
		return 1
	return 0

def ecl(value):
	if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return 1
	else:
		return 0
	

def pid(value):
	pattern = '^\d{9}$'
	match = re.search(pattern, value)
	if match:
		return 1
	else:
		return 0

def cid(value):
	return 1

def validate_passport(p):
	# byr 1920..2002
	# iyr 2010..2020
	# eyr 2020..2030
	# hgt ## cm|in - cm: 150..193; in 59..76
	# hcl \#XXXXXX (hex)
	# ecl ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	# pid XXXXXXXXX (all numbers, incl leading zeros)

	for key, value in p.iteritems():
		if globals()[key](value) == 0:
			#print key, value
			return 0

	# all validation passed
	pprint(p)
	return 1

total_passports = 0
num_records = 0

with open("input.txt") as data: 
	passport = {}
	for line in data: 
		if line == "\n":
			num_records += 1
			if test_passport_keys(passport):
				total_passports += validate_passport(passport)
			passport = {}
		else: 
			records = line.split()	
			for r in records: 
				f, v = r.split(":")
				if f == 'byr' or f == 'iyr' or f == 'eyr': 
					passport[f] = int(v)
				else:
					passport[f] = v
				
	if test_passport_keys(passport):
		total_passports += validate_passport(passport)
	num_records += 1

print total_passports, num_records
