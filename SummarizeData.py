#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TO RUN: script from command line: python SummarizeData.py filename # not including file extension
Created on Fri Mar 20 16:30:24 2020

Assignment 6

Run this script once to open a user-defined data file, generate a pdf summary of figures, 
and a second time to do the same with a user-defined different data file. 
@author: wagne216
"""
# modules:
import numpy as n
import matplotlib.pyplot as m
import pylab as p
import sys as s # to get command line arg

# see if the arguments are working:
print('Working with file named ',s.argv[1]+'.txt')

# 1.) OPEN
# come back to later: add command-line cmd to ask user input file_title
# 1 header line # one var per column # name col's based on headers
#file_title=('Tippecanoe_River_at_Ora.Annual_Metrics') # test with known filename
file_title = s.argv[1] # accepts argument in command line for title 
in_file = file_title + '.txt'
yr,avg,mx,mn,sdev,tqmean,RB = \
 n.genfromtxt(in_file, \
 unpack=True, skip_header=1) 
 
#%% 2.) PLOT
# Create a new figure of size 8x6 points, using 100 dots per inch
m.figure(figsize=(9,15), dpi=50) # both of these affects size, quality
# ^ create fig size proportions 1,>=1.5 to avoid title, xlabel overlap. 

 # PLOT 1: mean, med, max streamflow (cfs) (lines)
m.subplot(3,1,1)
m.plot(yr, mn, color="blue", linewidth=2.5, linestyle="-", label="min")
m.plot(yr, mx, color="red", linewidth=2.5, linestyle="-", label="max")
m.plot(yr, avg, color="black", linewidth=2.5, linestyle="-", label="mean")

# add legend:
m.legend(loc='best', frameon=False)

# fix ticks/bounds:
m.ylim(0,1.05*mx.max())
m.xlim(yr.min(),yr.max())

# labels:
m.title('Annual Values for Streamflow')
m.xlabel('Year')
m.ylabel('Streamflow (cfs)')

 #%% PLOT 2: Tqmean % (symbols)
m.subplot(3,1,2)
m.plot(yr, tqmean*100, color='#32a850',marker='4',linestyle='none',label="tq") 
 
# fix ticks/bounds:
m.ylim(0,1.05*100*tqmean.max())
m.xlim(yr.min(),yr.max())

# labels:
m.title('Annual Values for % Tqmean')
m.xlabel('Year')
m.ylabel('Tqmean (%)')

 #%% PLOT 3: R-B Index (ratio) (bar)
m.subplot(3,1,3)
num = len(yr) # # bars
m.bar(yr,RB,color='#cbf525',edgecolor='#f525dd',width=1)

# fix ticks/bounds:
m.ylim(0,1.05*RB.max())
m.xlim(yr.min(),yr.max())

# labels:
m.title('Annual Values for R-B Index')
m.xlabel('Year')
m.ylabel('R-B Index (ratio)')

# %%3.) WRITE TO PDF
p.savefig(file_title+'.pdf') # use original filename input by user as the title
 
 