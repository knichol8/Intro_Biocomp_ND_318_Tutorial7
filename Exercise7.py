"""
Exercise 7
By: Kathleen Nicholson and Grant Keller

** import statements go at the top of a (Python) script during
    global declarations. That way, they're availabe to all modules.
"""

import pandas
from plotnine import *
from time import sleep

def q1():
    #Q1
    #Pseudocode
    pass
    
def q2():
    """
    1. load in data (open file or straight to dataframe?)
        Data contains headers, not as separate row:
            format: HEADER: DATA HEADER: DATA...
            63 positions * 20 amino acids * 10 decoys = 12,600 lines
            Waaaay too many. Gonna snag a single position (200).
            Plot BindingScore vs. Solvation energy?
    2. 
    """
    
    inFile = open('HCV1406_scan.fasc', 'r')
    
    pose_data = {'filename' : [], 'total_score' : [], 
            'fa_atr' : [], 'fa_rep' : [],
            'fa_sol' : [], 'fa_intra_rep' : [],
            'fa_elec' : [], 'pro_close' : [],
            'hbond_sr_bb' : [], 'hbond_lr_bb' : [],
            'hbond_bb_sc' : [], 'hbond_sc' : [],
            'dslf_fa13' : [], 'rama' : [],
            'omega' : [], 'fa_dun' : [],
            'p_aa_pp' : [], 'yhh_planarity' : [],
            'ref' : [], 'TotalScore' : [],
            'HLAScore' : [], 'TCRScore' : [],
            'BindingScore' : [], 'LoopRMSD' : []}
    
    for line in inFile:
        line = line.strip().split(' ')
        for i in range(0, len(line), 2):
            if i > 1:
                pose_data[line[i][:-1]].append(float(line[i+1]))
            else:
                pose_data[line[i][:-1]].append(line[i+1])
    
    inFile.close()
    
    pose_frame = pandas.DataFrame(data=pose_data)
    
    a=ggplot(pose_frame,aes(x="fa_sol",y="LoopRMSD"))
    print(a + geom_point()+ coord_cartesian() + theme_bw() + x + y + stat + title)
    return
def q3():
    #Q3
    #Pseudocode
    #import packages
    
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
    
    return

if __name__ == '__main__':
    i = 0
    prompt = 'Enter "q1" or "q2" or "q3" to evaluate these solutions. Enter "exit" to quit.\n'
    while True:
        user_in = raw_input(prompt)
        if user_in == 'q1':
            q1()
            sleep(2)

        elif user_in == 'q2':
            q2()
            sleep(2)

        elif user_in == 'q3':
            q3()
            sleep(2)

        elif user_in.lower() == 'exit':
            break

        i += 1

        if i >= 3:
            print("Maybe take a break for now.")
            break