# Python-tools
 list of Python tools

Conver.py is a script to parse the Fortigate logs to CSV files.
basically a copy from https://github.com/N4SOC/fortilogcsv/blob/master/convert.py
Thanks Martin!

Findip.py is the tool to look through IPs (in string format) in the target CSV file.
Example:
findip.py iplist.txt parsed_fortigate_CSV.csv
Outpur would be a new CSV with same filename + scanned.

Spliter.py is tool to split huge CSV file to multipel small  CSVs

