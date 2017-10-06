#Analysis and Plotting
#Authors: Grant Keller and Kathleen Nicholson

#Q1
#Pseudocode



#Q2
#Pseudocode



#Q3
#Pseudocode
#import packages
import numpy
import pandas
from plotnine import *
#read in .txt file and find size
data=pandas.read_csv("data.txt", sep="\t", header=0)
data.shape
#plan for storing info

#for loop starts
#if north, add all numbers and divide by length
#elif south, add all numbers and divide by length
#elif east, add all numbers and divide by length
#elif west, add all numbers and divide by length
barplot=ggplot(data,aes(x=""))
