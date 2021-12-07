# Using Hexiwear with Python
import pexpect
import time

DEVICE = "30:AE:A4:05:A0:42"   # device #24

print("Hexiwear address:"),
print(DEVICE)

# Run gatttool interactively.
print("Running gatttool...")
child = pexpect.spawn("gatttool -I")

# Connect to the device.
print("Connecting to "),
print(DEVICE),
child.sendline("connect {0}".format(DEVICE))
child.expect("Connection successful", timeout=10)
print(" Connected!")

#print 'Press Ctrl-C to quit.'
# function to transform hex string like "0a cd" into signed integer
def hexStrToInt(hexstr):
    val = int(hexstr[0:2],16) + (int(hexstr[3:5],16)<<8)
    if ((val&0x8000)==0x8000): # treat signed 16bits
        val = -((val^0xffff)+1)
    return val

while True:
# Gyro
#for i in range(100):
#	child.sendline("char-read-hnd 0x2a")
#	child.expect("Characteristic value/descriptor: ", timeout=10)
#	child.expect("\r\n", timeout=10)
#	with open('data.txt', 'a') as f: f.write(child.before.decode('utf-8')+"\n")
#	print("Temperature:   "),
#	print(child.before)
#    time.sleep(5)

	child.sendline("char-write-req 0x2b 0200")
	child.expect("Indication   handle = 0x002a value: ", timeout=10)
	child.expect("\r\n", timeout=10)
	print(child.before)
