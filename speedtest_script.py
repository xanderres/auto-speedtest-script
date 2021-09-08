#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import datetime
import csv
try:
    import speedtest
except:
   print("please install speedtest-cli !!! --> pip3 install speedtest-cli")

# Config
data_path = '/home/pi/speedtest/'

def st_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    down = round(st.download() / 1e+6, 2)  #Mbit/s
    up = round(st.upload() / 1e+6, 2)  #Mbit/s
    return down, up

def csv_write(data_row, output_file):
    csv_file = open(output_file, 'a+')
    writer = csv.writer(csv_file)
    writer.writerow(data_row)

def csv_read():
    

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
row = [date, time] + list(st_test())
csv_file = data_path + now.strftime("%Y-%m") + '.csv'
csv_write(row, csv_file)

