import os
import math
print "gear 1: 4 disk"
os.system("../src/disksim paraid5_1.parv paraid5_1.outv ascii 0 1")
os.system("grep 'IOdriver Response time average' paraid5_1.outv")
filename1="paraid5_1.outv"
filename2="paraid5_2.outv"
T=0.8
f=open(filename1)
utilization_list=[]
lines=f.readlines()
for line in lines:
	if len(line)>30:
		if str(line[7:30])==str("Total utilization time:"):
			temp=line.split()
			utilization_list.append(float(temp[-1]))
		elif str(line[0:35])==str("Overall I/O System Number of reads:"):
			temp=line.split()
			A_read=float(temp[-1])
			print "A_read",A_read
		elif str(line[0:36])==str("Overall I/O System Number of writes:"):
			temp=line.split()
			A_write=float(temp[-1])
			print "A_write",A_write
U=sum(utilization_list)
mean=U/len(utilization_list)
var=0
for utilization in utilization_list:
	var+=(utilization-mean)**2
var/=U/len(utilization_list)
S=math.sqrt(var)
print "average utilization time:",U
print "stand deviation of utilization time:",S
print "U+S=",U+S
if U+S>T:
	print "should up-shifting."
else:
	print "don't need to up-shifting."
	exit(0)


print "gear 2: 5 disk"
os.system("../src/disksim paraid5_2.parv paraid5_2.outv ascii 0 1")
os.system("grep 'IOdriver Response time average' paraid5_2.outv")
utilization_list=[]
f=open(filename2)
U=0
lines=f.readlines()
for line in lines:
	if len(line)>30:
		if str(line[7:30])==str("Total utilization time:"):
			temp=line.split()
			utilization_list.append(float(temp[-1]))
		elif str(line[0:35])==str("Overall I/O System Number of reads:"):
			temp=line.split()
			A_read=float(temp[-1])
			print "A_read",A_read
		elif str(line[0:36])==str("Overall I/O System Number of writes:"):
			temp=line.split()
			A_write=float(temp[-1])
			print "A_write",A_write
U=sum(utilization_list)
mean=U/len(utilization_list)
var=0
for utilization in utilization_list:
	var+=(utilization-mean)**2
var/=U/len(utilization_list)
S=math.sqrt(var)
print "average utilization time:",U
print "stand deviation of utilization time:",S
print "U+S=",U+S
if U+S<T:
	print "should down-shift."
else:
	print "don't need to down-shift."
