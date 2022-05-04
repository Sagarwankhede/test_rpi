class py_solution:
  def twoSum(self, nums, target):
       lookup = {}
       for i, num in enumerate(nums):
           if target - num in lookup:
               return (lookup[target - num], i )
           lookup[num] = i
print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))

class find_pair:
	def __init__(self):
		self.numbers, self.target = [10,20,10,40,50,60,70], 50
	

def find_pair_func():
	number, target = [10,20,10,40,50,60,70], 50
	_len = len(number)
	
	for i, no in enumerate(number):
		if i+1 == _len:
			break
		if no+number[i+1] == target:
			print(i, i+1)
find_pair_func()

class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))

class Student:
	pass

class Marks:
	pass

print(type(Student))
print(Student.__dict__.keys())
print(Student.__dict__.values())
S1 = Student()
M1 = Marks()


print(isinstance(S1, Student) and isinstance(S1, object))
print(isinstance(M1, Marks) and isinstance(M1, object))


class Car:    
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
    
    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def __drive1(self):
        print('driving. maxspeed ' + str(self.__maxspeed))
        
    def _drive2(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

redcar = Car()

