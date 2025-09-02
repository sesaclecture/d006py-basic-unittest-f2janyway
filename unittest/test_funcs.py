# TODO: 사용자 모듈 import

# TODO: 아래의 코드를 삭제하고 unittest를 작성하세요.
from func import check_is_odd, avg, get_max, get_min
import statistics
import random

def test_is_odd():
	assert check_is_odd(1) is True
	assert check_is_odd(2) is False 
	assert check_is_odd(0) is False
	assert check_is_odd(-1) is True

def test_avg():
	arr = [1,2,3,4]
	assert avg(arr) == 2.5
	arr = [x for x in range(100)]
	a = avg(arr)
	print(a)
	assert a  == statistics.mean(arr)

def test_max():
	arr = [1,2,3,4]
	assert  get_max(arr) == 4
	arr = [random.randint(-1000,1000) for x in range(100)]
	assert max(arr) == get_max(arr)
	

def test_min():
	arr = [1,2,3,4]
	assert get_min(arr) == 1
	arr = [random.randint(-1000,1000) for x in range(100)]
	assert min(arr) == get_min(arr)

