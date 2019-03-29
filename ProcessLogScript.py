"""
Log file for the process Id
CPU usage and Memory usage


Use Top command and give the exact process name as a input ..
"""


import commands
import os


x = raw_input("Enter the process name :")

pid =  commands.getoutput("top -b -n 1 | grep %s | awk '{print $1}'" %x)

cpu = commands.getoutput("top -b -n 1 | grep %s | awk '{print $9}'" %x)

mem = commands.getoutput("top -b -n 1 | grep %s | awk '{print $10}'" %x)

proc_file = open("proclog.txt", 'w+')

proc_file.write("Process Log File"+"\n"+"\n")
proc_file.write("Process Id"+":"+pid+"\n")
proc_file.write("Cpu usage"+":"+cpu+'\n')
proc_file.write("Memory usage"+":"+mem)

print "Log file created in the path"+"-"+os.getcwd()
