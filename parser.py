"""
for each congressional session 
get the total number of bills a congress person sponsored or cosponsored
divided into the subject ( health, military, etc)
"""
import os, json, pandas

bills = [bill_file for bill_file in os.listdir('bills/') if bill_file.endswith('.json')]

for bill in bills:
  print(bill)
