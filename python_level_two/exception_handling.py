# this code block handal perticuler exception error
try:
    f = open('testfile','r')
    f.write('Hello welcome to python')
except IOError:
   print("Error: Could not find file or read data")
else:
   print("successfully")
   f.close()

#this code block handle any type of exception

try:
    f = open('testfile','r')
    f.write('Hello welcome to python')
except:
    # This will check for any exception and then execute this print statement
   print("Error: Could not find file or read data 2")
else:
   print("successfully")
   f.close()


"""
Output : 
Error: Could not find file or read data
Error: Could not find file or read data 2

"""

#finally block example
try:
   f = open("testfile", "w")
   f.write("Hello welcome to python")
finally:
   print("Always executing this block")
#output : Always execute finally code blocks
