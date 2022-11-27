import binascii
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Output binary CADU file name")
parser.add_argument("-ip", "--inputp", help="Input primary binary file name")
parser.add_argument("-is", "--inputs", help="Input secondary binary file name")
args = parser.parse_args()
inputfile1 = args.inputp
inputfile2 = args.inputs
outfile = args.output

def create_counter():

    i = -1
    
    def func():
        nonlocal i
        i += 1
        if i == 16777216:
            i = 0
            return i
        else:
            return i
    
    return func

idf = 1
line1 = 2048
backline1 = 0
line2 = 2048
backline2 = 0
size1 = os.path.getsize(inputfile1)
size2 = os.path.getsize(inputfile2)

print("--------------------------------------------")
print("                                            ")
print("              CCSDS CADU Mixer              ")
print("               by Egor UB1QBJ               ")
print("                                            ")
print("--------------------------------------------")

with open(inputfile1, 'rb') as f:
        lines1 = f.read().hex()
with open(inputfile2, 'rb') as f:
        lines2 = f.read().hex()
x1 = ""
x2 = ""
while True:
    x1 = lines1[backline1:line1]
    backline1 = line1
    line1 += 2048
    x2 = lines2[backline2:line2]
    backline2 = line2
    line2 += 2048
    if(line1 > size1*2):
        x1 = ""
        vc1 = "Writing done!"
    if(line2 > size2*2):
        x2 = ""
        vc2 = "Writing done!"
    out = x1 + x2
    with open(outfile, 'ab') as fout:
        fout.write(binascii.unhexlify(out))
    print("CADU Frames: " + str(idf*2), end='\r')
    idf += 1
    if(x1 == x2 == ""):
        print("")
        print("Done!", end='\r')
        break