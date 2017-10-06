#Analysis and Plotting
#Authors: Grant Keller and Kathleen Nicholson

#Q1
#Pseudocode



#Q2
#Pseudocode

"""
1. load in data (open file or straight to dataframe?)
    Data contains headers, not as separate row:
        format: HEADER: DATA HEADER: DATA...
        63 positions * 20 amino acids * 10 decoys = 12,600 lines
        Waaaay too many. Gonna snag a single position (200).
        Plot BindingScore vs. Solvation energy?
2. 
"""
# open file
# for each line
#   split line by ' '
#   headers
#   append info

inFile = open('HCV1406_scan.fasc', 'r')

filename = []
total_score = []
fa_atr = []
fa_rep = []
fa_sol = []
fa_intra_rep = []
fa_elec = []
pro_close = []
hbond_sr_bb = []
hbond_lr_bb = []
hbond_bb_sc = []
hbond_sc = []
dslf_fa13 = []
rama = []
omega = []
fa_dun = []
p_aa_pp = []
yhh_planarity = []
ref = []
TotalScore = []
HLAScore = []
TCRScore = []
BindingScore = []
LoopRMSD = []
for line in inFile:
    line = line.strip().split(' ')
    


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
