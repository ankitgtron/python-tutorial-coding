import time
import threading

def calc_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.1)
        print("square", n*n)

def calc_cube(numbers):
    print('calculate cube of numbers')
    for n in numbers:
        time.sleep(0.1)
        print("cube", n*n*n)

arr = [2,3,8,9]

to = time.time()

t1 = threading.Thread(target= calc_square, args = (arr,))
t2 = threading.Thread(target = calc_cube, args= (arr,))

t1.start()
t2.start()

t1.join()
t2.join()


print("done in : ", time.time() -to)
print("i am done with all of my work")
