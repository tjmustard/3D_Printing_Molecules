#!/opt/local/bin/python2.7

import sys
import getopt
import math

### --- Arguments --- ###
program = "Clean-Slic3r-GCODE.py"

ifile = ''
ofile = ''

### Read command line args
try:
	myopts, args = getopt.getopt(sys.argv[1:],"i:o:h")
except getopt.GetoptError:
	print program + " -i <input> -o <output>"
	sys.exit(2)
###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
	if o == '-i':
		ifile = a
	elif o == '-o':
		ofile = a
	elif o == '-h':
		print program + " -i <input> -o <output>"
		sys.exit(0)
	else:
		print program + " -i <input> -o <output>"
		sys.exit(0)

### --- Open file and input each line into a list --- ###
f = open(ifile)
ifileList = f.readlines()
f.close()

def replaceFirstWith(start, end):
	newline = []
	if line[0] == start:
		for i in range(len(line)):
			if i == 0:
				newline.append(end)
			else:
				newline.append(line[i])
		templine = ' '.join(str(e) for e in newline) + "\n"
		f.write(templine)
		newline[:] = []
	return

### --- Output file WITHOUT Carbons to the ofile --- ###
#lastpercentage = float(0)
#printpercent = 1
startGCODE = False
f = open(ofile, 'w+')
f.write(";Edited by Clean-Slic3r-GCODE.py\n")
for i in range(len(ifileList)):
	line = ifileList[i].rstrip().split()
	###Print the percentage
	#if i % 10 == 0 and float(i / float(len(ifileList)) * 100) >= lastpercentage + 1:
	#	lastpercentage = int(i / float(len(ifileList)) * 100)
	#	printpercent = 1
	if line != []:
		if line[0] == "G0" or line[0] == "G21" or line[0] == "G90" or line[0] == "G28" or \
			line[0] == "M107" or line[0] == "M126" or line[0] == "M127" or line[0] == "M140" or \
			line[0] == "M101" or line[0] == "M103" or line[0] == "M106" or line[0] == "M109" and startGCODE == False:
			replaceFirstWith("NOPE", ";NOPE")
		elif ifileList[i].strip() == ";START GCODE":
			startGCODE = True
			f.write(ifileList[i])
		elif line[0] == "G0" or line[0] == "G21" or line[0] == "G90" or line[0] == "G28" or \
			line[0] == "M107" or line[0] == "M126" or line[0] == "M127" or line[0] == "M140" or \
			line[0] == "M101" or line[0] == "M103" or line[0] == "M106": #or line[0] == "M109"
			### Replace all G0 with G1
			replaceFirstWith("G0", "G1")
			### Remove all G21
			replaceFirstWith("G21", ";G21")
			### Remove all G90
			replaceFirstWith("G90", ";G90")
			### Replace G28 with G162
			replaceFirstWith("G28", "G162 X Y F2000 ;")
			### Replace M106 with G126
			replaceFirstWith("M106", "M126 T0 ;M106")
			### Replace M107 with G127
			replaceFirstWith("M107", "M127 T0 ;M107")
			### Replace M109 with M104
			replaceFirstWith("M109", "M104")
			### Remove extruder on/off lines
			replaceFirstWith("M101", ";M101")
			replaceFirstWith("M103", ";M103")
			### Remove fan stuff
			replaceFirstWith("M126", ";M126")
			replaceFirstWith("M127", ";M127")
			replaceFirstWith("M140", ";M140")
		##Reset the print percentage switch
		#elif line[0][0] == ";" and printpercent == 1:
		#	printpercent = 0
		else:
			f.write(ifileList[i])
	#else:
		#f.write(ifileList[i])
f.close()












