import binascii
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Output binary CADU file name")
parser.add_argument("-i", "--input", help="Input binary file name")
parser.add_argument("-v", "--vcid", help="VCID in hex style (from 0 to F)")
parser.add_argument("-a", "--asm", help="ASM sync in hex style (1acffc1d)")
args = parser.parse_args()
#settings!
inputfile = args.input
outfile = args.output
asm = args.asm
vcduph = "3fc"
vcid = args.vcid
replayspare = "00"
vcduiz = "000000ff"
rs = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
#counter
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
countercadus = create_counter()
idf = 1
line = 1764
backline = 0
size = os.path.getsize(inputfile)
print("--------------------------------------------")
print("                                            ")
print("            CCSDS CADU Generator            ")
print("               by Egor UB1QBJ               ")
print("                                            ")
print("--------------------------------------------")
with open(inputfile, 'rb') as f:
        lines = f.read().hex()
while True:
    countcadus = countercadus()
    hexdata = hex(countcadus).split('x')[-1]
    if len(hexdata) == 1:
        vcducounter = "00000" + hexdata.upper()
    elif len(hexdata) == 2:
        vcducounter = "0000" + hexdata.upper()
    elif len(hexdata) == 3:
        vcducounter = "000" + hexdata.upper()
    elif len(hexdata) == 4:
        vcducounter = "00" + hexdata.upper()
    elif len(hexdata) == 5:
        vcducounter = "0" + hexdata.upper()
    else:
        vcducounter = hexdata.upper()
    x = lines[backline:line]
    backline = line
    line += 1764
    out = asm + vcduph + vcid + vcducounter + replayspare + vcduiz + x + rs
    with open(outfile, 'ab') as outcadun:
        outcadun.write(binascii.unhexlify(out))
    print("CADU frame. ASM: " + asm + " | VCID: " + vcid + " | Total CADUs: " + str(idf), end='\r')
    idf += 1
    sizeout = os.path.getsize(outfile)
    if(line >= size*2):
        print("")
        print("Done!", end='\r')
        break