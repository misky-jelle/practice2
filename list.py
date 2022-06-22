def numbers(a):
    a.remove(a[-2])
    print (a)
a=[2,4,6,8]
numbers(a)    

def day(days):
    c=(days.count("Monday"))
    print(c)
days=["Monday","Tuesday","Friday","Monday"]
day(days)    

def small(smallest):
    smallest.sort()
    return smallest[0]
smallest=([3,6,8,2,4,1,5,7])
small(smallest)    

def divisible_by_seven():
    for x in range(100,200):
        if x%7==0:
         print("is divisible by seven")
        else:
         print("is not divisible by seven")
divisible_by_seven()  
 
def number():
    num=int(input("Enter number:"))
    num1=int(input("Enter another number:"))
    sum=num+num1
    if sum >10:
        print("is greater than ten")
    elif sum < 10:
        print("is less than ten")
    else:
        sum == 10
        print("is equals to ten")
number()

fruits=["apples","grapes","pineapples"]
fruits.pop()
print(fruits)
    # or
fruit=["apples","grapes","pineapples"]
fruit.remove("apples")
print(fruit)

cars=["Ford","BMW","Volvo"]
cars.sort()
print (cars)




a=[1,2,3,4,5]  
def number(a):
  # for x in a:
    if 4 in a:
        return True
    else:
        return False  
number(a)

