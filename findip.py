#!/usr/bin/python
import csv
import re
import sys
import codecs

def txt_to_list(file1):
    #create the IP list
    ips=[]
    #open the source file which contains IPs
    iplist = open(file1, "r")
    for line in iplist:
        ips.append(line.strip())
    return ips

def find_line(list1,file1):
    
    matched_lines =[]
    #read target csv, and split on "," the line
    print("[+] Reading logs from " + file1)
    try:
        log_data = codecs.open(file1, "r", encoding="UTF-8")
    except:
        raise Exception("Invalid input file")
    # go through each IP in the iplist
    for line in log_data:
        for ip in list1:
            if str(ip) in str(line):
                matched_lines.append(str(line)) #add the matched line in a list

    print("[+] Writing to CSV")
    newfilename = file1+'_scanned.csv'  # Get base file name from logfile
    #Added the newline option to prevent blank rows from outputting to CSV
    with open(newfilename, 'w', newline='') as fileh:
        for row in matched_lines:
            fileh.write(row)  # write data
    print("[+] Finished - " + str(len(matched_lines)) + " rows written to " + newfilename)

if len(sys.argv) > 1:
    iplist = str(sys.argv[1])
    target_file = str(sys.argv[2])
    IOC=txt_to_list(iplist)
    find_line(IOC,target_file)
else:
    raise Exception("No input file specified")
