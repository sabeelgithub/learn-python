########### SCOPE ###########
# global
global_var = 10  # Global variable

def my_function():
    print(global_var)  # Accessing the global variable

my_function()
print(global_var)

# local
global_var =8
def my_function():
    local_var = 5  # Local variable
    print(local_var)
    print(global_var)

my_function()  


# both
global_var = 30  # Global variable
global_var = 50
def my_function():
    global global_var
    global_var = 20  # Modifying the global variable
    print(global_var)


my_function() 

print(global_var)  

############## END ################



