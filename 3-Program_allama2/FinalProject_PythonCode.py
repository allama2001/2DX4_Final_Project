import serial
import math

#Modify the following line with your own serial port details
#   Currently set COM3 as serial port at 115.2kbps 8N1
#   Refer to PySerial API for other options.  One option to consider is
#   the "timeout" - allowing the program to proceed if after a defined
#   timeout period.  The default = 0, which means wait forever.

s = serial.Serial("COM3", 115200)
output = ''
print("Opening: " + s.name)
f=open("projectfile2dx4.xyz", "a")#PAY ATTENTION TO THIS

for i in range(43):
    x = s.read()        # read one byte
    c = x.decode()      # convert byte type to str
    output+=c
    
    while(c!= "\n"):
        x = s.read()        # read one byte
        c = x.decode()
        output+=c
    print("output:" + output)
    
    ans = output.split()
    #print(ans)
    #for ans in output.split():
    if (ans[0].isdigit()):
        ans = int(output)
        angle = 11.25*(i-10)
        #print("angle:" + angle)
        #ans = int(output)
        #print(ans)
        x = 350*1
        y = float(ans)*math.sin(angle*(math.pi/180))
        z = float(ans)*math.cos(angle*(math.pi/180))
        a = "{} {} {}\n".format(x,y,z)
        print("X, Y, Z:" + a)
        f.write(a)
    
    output = ''
f = open("projectfile2dx4.xyz", "r")#CHANGE THIS IF NEEDED
print(f.read())
f.close()
print("Closing: " + s.name)
s.close();
