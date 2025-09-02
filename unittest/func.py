
#def test_is_odd():
#	assert check_is_odd(1) is True
#	assert check_is_odd(2) is False 
#
#def test_avg():
#	arr = [1,2,3,4]
#	assert avg(arr) == 5
#
#def test_max():
#	arr = [1,2,3,4]
#	assert  get_max(arr) == 4
#
#def test_min():
#	arr = [1,2,3,4]
#	assert get_min(arr) == 1

import sys
##########################
def check_is_odd(num):
	if num % 2 == 0:
		return False
	else:
		return True

def avg(arr:[list]):
	temp  = 0
	count = len(arr)
	for i in arr:
		temp += i
	
	return temp / count
		
def get_max(arr):
	temp_max = -sys.maxsize - 1
	for i in arr:
		if temp_max < i:
			temp_max = i
	return temp_max

def get_min(arr):
	temp_min = sys.maxsize
	for i in arr:
		if temp_min > i:
			temp_min = i
	return temp_min
