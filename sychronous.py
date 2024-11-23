import time

def task1():
    print("Starting Task 1")
    time.sleep(2)  # Simulate a time-consuming operation
    print("Task 1 Completed")

def task2():
    print("Starting Task 2")
    time.sleep(3)  # Simulate another time-consuming operation
    print("Task 2 Completed")

# Execute tasks synchronously
task1()
task2()
print("All tasks completed")