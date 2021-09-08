#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import datetime
import csv
try:
    import speedtest
except:
   print("please install speedtest-cli !!! --> pip3 install speedtest-cli")


global output_file
output_file = '/home/pi/Desktop/output_test.csv'


def test():
    st = speedtest.Speedtest()
    st.get_best_server()
    down = round(st.download() / 1e+6, 2)  #Mbit/s
    up = round(st.upload() / 1e+6, 2)  #Mbit/s
    return down, up

def csv_write(row):
    file = open(output_file, 'a+')
    writer = csv.writer(file)
    writer.writerow(row)


now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
row = [date, time] + list(test())
csv_write(row)

