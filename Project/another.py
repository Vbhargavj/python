import time

named_tuple = time.localtime() # get struct_time
time_string = int(time.strftime("%M", named_tuple))
time_string1 = int(time.strftime("%H", named_tuple))

time_count =  time_string1
intir = time.time()

print(intir)

# print(time_string1)
# print(time_string)