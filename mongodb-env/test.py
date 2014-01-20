import time
 
def main():
    # define the variable 'current_time' as a tuple of time.localtime()
    current_time = time.localtime() 
    print(current_time)              # print the tuple
 
    # if the year is 2009 (first value in the current_time tuple)
    if current_time[0] == 2009: 
        print('The year is 2009')    # print the year
 
if __name__ == '__main__':     # if the function is the main function ...
    main() # ...call it