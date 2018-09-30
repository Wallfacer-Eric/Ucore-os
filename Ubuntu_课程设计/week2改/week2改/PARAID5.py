import os
import math
filename1="paraid5_1.outv"
filename2="paraid5_2.outv"
T=0.8	#threshold
gear=2
iterTime=8
for _ in range(iterTime):
	if gear==1:
		print "gear 1: 4 disk"
		os.system("../src/disksim paraid5_1.parv paraid5_1.outv ascii 0 1")
		os.system("grep 'IOdriver Response time average' paraid5_1.outv")
		f=open(filename1)
		utilization_list=[]
		lines=f.readlines()
		for line in lines:
			if len(line)>30:
				'''
				if str(line[7:30])==str("Total utilization time:"):
					temp=line.split()
					utilization_list.append(float(temp[-1]))
				'''
				if str(line[8:29])==str("Completely idle time:"):
					temp=line.split()
					utilization_list.append(1-float(temp[-1]))
		f.close()
		U=sum(utilization_list)/len(utilization_list)
		var=0
		for utilization in utilization_list:
			var+=(utilization-U)**2
		var/=U
		S=math.sqrt(var)
		print "average utilization time:",U
		print "stand deviation of utilization time:",S
		print "U+S=",U+S
		print ">>>>>>>>"
		if U+S>T:
			print "U+S>T, should up-shift."
			gear=2
		else:
			print "U+S<T, don't need to up-shift."
			gear=1
		print ""
	elif gear==2:
		print "gear 2: 5 disk"
		os.system("../src/disksim paraid5_2.parv paraid5_2.outv ascii 0 1")
		os.system("grep 'IOdriver Response time average' paraid5_2.outv")
		utilization_list=[]
		f=open(filename2)
		U=0
		lines=f.readlines()
		for line in lines:
			if len(line)>30:
				'''
				if str(line[7:30])==str("Total utilization time:"):
					temp=line.split()
					utilization_list.append(float(temp[-1]))
				'''
				if str(line[8:29])==str("Completely idle time:"):
					temp=line.split()
					utilization_list.append(1-float(temp[-1]))
		f.close()
		U=sum(utilization_list)/len(utilization_list)
		var=0
		for utilization in utilization_list:
			var+=(utilization-U)**2
		var/=U
		S=math.sqrt(var)
		print "average utilization time:",U
		print "stand deviation of utilization time:",S
		print "U+S=",U+S
		print ">>>>>>>>"
		if U+S<T:
			print "U+S<T, should down-shift."
			gear=1
		else:
			print "U+S>T, don't need to down-shift."
			gear=2
		print ""
