"""
Exercise 7
By: Kathleen Nicholson and Grant Keller

** import statements go at the top of a (Python) script during
    global declarations. That way, they're availabe to all modules.
"""

import pandas
from plotnine import *
from time import sleep

FASCFILE = 'HCV1406_scan.fasc'
XVAR = "fa_sol"
YVAR = "LoopRMSD"
FASTAFILE = "Lecture11.fasta"

def q1():
    """
    Pulls info from FASTAFILE (declared above). Stores sequnce ID, sequence length,
    % GC content, and melting temp. if sequence length is 14 or less.
    Constructs and displays histograms of sequence length and GC content.
    """
    inFile=open(FASTAFILE,"r")
    #create lists for storing information about sequences
    sequenceID=[]
    sequenceLength=[]
    percentGC=[]
    meltingTemp=[]
    
    # loop through each line of fasta file to process sequences
    for line in inFile:
        # remove newline character from file line
        line=line.strip()
        # if a sequence record
        if '>' in line:
            # add the sequence ID to the sequenceID list
            sequenceID.append(line[4:])
        # if a sequence line
        else:
            # get the number of characters in the sequence and convert to a float to avoid integer division
            seqLen=float(len(line))
            # count the number of G's and C's
            nG=line.upper().count("G")
            nC=line.upper().count("C")
            
            # if the sequence is 14 or fewer bases calculate melting temperature
            if seqLen <= 14:
                Tm = 2*(nG+nC)+2*seqLen
            else:
                Tm = -9999
            
            # append values to the lists
            sequenceLength.append(seqLen)
            percentGC.append((nG+nC)/seqLen*100)
            meltingTemp.append(Tm)
    # close file
    inFile.close()
    
    # combine lists into dataframe
    seqDF = pandas.DataFrame(list(zip(sequenceID,sequenceLength,percentGC,meltingTemp)),columns=['sequenceID','sequenceLength','percentGC','meltingTemp'])
    # creates histogram of sequence length, binned by 5
    a1 = ggplot(seqDF,aes(x="sequenceLength"))
    # creates histogram of % GC content, binned by 5
    a2 = ggplot(seqDF,aes(x="percentGC"))
    xl1 = xlab("Sequence Length (nt)")
    xl2 = xlab("GC Content (%)")
    y = ylab("Frequency")
    # displays both histograms
    print(a1+geom_histogram(binwidth=5)+theme_classic()+xl1+y)
    print(a2+geom_histogram(binwidth=5)+theme_classic()+xl2+y)
    return
def q2():
    """
    Imports Rosetta .fasc file and creates a scatter plot of calculated pose energy
    parameters. Parameters (XVAR & YVAR) and file (FASCFILE) are specified in global
    declarations above.
    NOTE: Several of the paramters included in the pose_data instantiation are unique,
    namely: TotalScore, HLAScore, TCRScore, BindingScore. LoopRMSD may be formatted differently,
    or not included in other .fasc files as well. Modify these sections as necessary.
    Trendline is linear fit, which may not be appropriate for your data.
    """
    
    inFile = open(FASCFILE, 'r')
    
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
    # reads FASCFILE line-by-line and extracts information to pose_data
    for line in inFile:
        line = line.strip().split(' ')
        for i in range(0, len(line), 2):
            if i > 1:
                pose_data[line[i][:-1]].append(float(line[i+1]))
            else:
                pose_data[line[i][:-1]].append(line[i+1])
    
    inFile.close()
    # instantiates pandas DataFrame object based on pose_data
    pose_frame = pandas.DataFrame(data=pose_data)
    # labels for x and y axes
    xl = xlab("Full Atom Solvation Energy (Rosetta Energy Units)")
    yl = ylab("CDR Loop RMSD (Angstrom)")
    # plot title
    title = ggtitle("HCV1406 alpha Q100 Single aa Scan")
    # trendline model
    stat = stat_smooth(method="lm")
    # instantiate ggplot object
    b = ggplot(pose_frame,aes(x=XVAR,y=YVAR))
    # spits plot to screen -- point plot, cartesian coords, white bg w/ markers
    print(b + geom_point()+ coord_cartesian() + theme_bw() + stat + xl + yl + title)
    return
def q3():
    #read in .txt file
    data=pandas.read_csv("data.txt", sep=',')
    #This code creates a graph of means observations for each region.
    c1=ggplot(data)+theme_classic()+xlab("regions")+ylab("observation mean")
    x = "factor(region)"
    y = data.observations
    print(c1+geom_bar(aes(x=x),y=y, stat="summary", fun_y=numpy.mean))
    
    #This code creates a scatterplot of observations and uses jitter to make the points
    #     more readable
    c2=ggplot(data,aes(x="region",y="observations"))
    print(c2+geom_point()+coord_cartesian()+geom_jitter())
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

        if i >= 8:
            print("Maybe time to take a break.")
            break