#有参数有返回值函数sum
def sum(x,y):
	z=x*x+y*y
	return z
print(sum(2,3))

#有参有返回值函数num
def num(n):
	return range(1,n)
print(num(5))
print(list(num(6)))

#无参无返回值函数myprint：
def myprint():
	print("hello world")
myprint()

#什么都不做函数fun：
def fun():
	pass
fun()
