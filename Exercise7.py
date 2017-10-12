"""
Exercise 7
By: Kathleen Nicholson and Grant Keller

** import statements go at the top of a (Python) script during
    global declarations. That way, they're availabe to all modules.
"""

from time import sleep
import pandas
from plotnine import *

FASCFILE = 'HCV1406_scan.fasc'
XVAR = "fa_sol"
YVAR = "LoopRMSD"
FASTAFILE = "Lecture11.fasta"

def q1_solution():
    """
    Pulls info from FASTAFILE (declared above). Stores sequnce ID, sequence length,
    % GC content, and melting temp. if sequence length is 14 or less.
    Constructs and displays histograms of sequence length and GC content.
    """
    in_file = open(FASTAFILE, "r")
    #create lists for storing information about sequences
    seq_id = []
    seq_len = []
    percent_gc = []
    mel_temp = []

    # loop through each line of fasta file to process sequences
    for line in in_file:
        # remove newline character from file line
        line = line.strip()
        # if a sequence record
        if '>' in line:
            # add the sequence ID to the sequenceID list
            seq_id.append(line[4:])
        # if a sequence line
        else:
            # get the number of characters in the sequence
            seq_len.append(len(line))
            # count the number of G's and C's
            n_gc = line.upper().count("G") + line.upper().count("C")

            # if the sequence is 14 or fewer bases calculate melting temperature
            if seq_len[-1] <= 14:
                mel_temp.append(2*(nG+nC)+2*seq_len[-1])
            else:
                mel_temp.append(-9999)

            # append values to the lists
            percent_gc.append((n_gc)/float(seq_len[-1])*100)
    # close file
    in_file.close()

    # combine lists into dataframe
    headers = ['sequenceID', 'sequenceLength', 'percentGC', 'meltingTemp']
    seq_df = pandas.DataFrame(list(zip(seq_id, seq_len, percent_gc, mel_temp)), columns=headers)
    # creates histogram of sequence length, binned by 5
    a1_plot = ggplot(seq_df, aes(x="sequenceLength"))
    # creates histogram of % GC content, binned by 5
    a2_plot = ggplot(seq_df, aes(x="percentGC"))
    xl1 = xlab("Sequence Length (nt)")
    xl2 = xlab("GC Content (%)")
    y_label = ylab("Frequency")
    # displays both histograms
    print a1_plot + geom_histogram(binwidth=5) + theme_classic() + xl1 + y_label
    print a2_plot + geom_histogram(binwidth=5) + theme_classic() + xl2 + y_label
    return
def q2_solution():
    """
    Imports Rosetta .fasc file and creates a scatter plot of calculated pose energy
    parameters. Parameters (XVAR & YVAR) and file (FASCFILE) are specified in global
    declarations above.
    NOTE: Several of the paramters included in the pose_data instantiation are unique,
    namely: TotalScore, HLAScore, TCRScore, BindingScore. LoopRMSD may be formatted differently,
    or not included in other .fasc files as well. Modify these sections as necessary.
    Trendline is linear fit, which may not be appropriate for your data.
    """

    in_file = open(FASCFILE, 'r')

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
    for line in in_file:
        line = line.strip().split(' ')
        for i in range(0, len(line), 2):
            if i > 1:
                pose_data[line[i][:-1]].append(float(line[i+1]))
            else:
                pose_data[line[i][:-1]].append(line[i+1])

    in_file.close()
    # instantiates pandas DataFrame object based on pose_data
    pose_frame = pandas.DataFrame(data=pose_data)
    # labels for x and y axes
    x_label = xlab("Full Atom Solvation Energy (Rosetta Energy Units)")
    y_label = ylab("CDR Loop RMSD (Angstrom)")
    # plot title
    title = ggtitle("HCV1406 alpha Q100 Single aa Scan")
    # trendline model
    stat = stat_smooth(method="lm")
    # instantiate ggplot object
    b_plot = ggplot(pose_frame, aes(x=XVAR, y=YVAR))
    # spits plot to screen -- point plot, cartesian coords, white bg w/ markers
    print b_plot + geom_point()+ coord_cartesian() + theme_bw() + stat + x_label + y_label + title
    return
def q3_solution():
    """
    From the data contained in data.txt, generates a barplot of four population
    means (north, south, east, west), then generates a scatter plot of ALL observations.
    """
    #read in .txt file
    data = pandas.read_csv("data.txt", sep=',')
    #This code creates a graph of means observations for each region.
    c1_plot = ggplot(data)+theme_classic()+xlab("regions")+ylab("observation mean")
    x_ax = "factor(region)"
    y_ax = data['observations']
    print c1_plot + geom_bar(aes(x=x_ax), y=y_ax, stat="summary", fun_y=numpy.mean)

    #This code creates a scatterplot of observations and uses jitter to make the points
    #     more readable
    c2_plot = ggplot(data, aes(x="region", y="observations"))
    print c2_plot + geom_point() + coord_cartesian() + geom_jitter()
    return

if __name__ == '__main__':
    i = 0
    PROMPT = 'Enter "q1" or "q2" or "q3" to evaluate these solutions. Enter "exit" to quit.\n'
    while True:
        USER_IN = raw_input(PROMPT)
        if USER_IN.lower() == 'q1':
            q1_solution()
            sleep(2)

        elif USER_IN.lower() == 'q2':
            q2_solution()
            sleep(2)

        elif USER_IN.lower() == 'q3':
            q3_solution()
            sleep(2)

        elif USER_IN.lower() == 'exit':
            break

        i += 1

        if i >= 8:
            print "Maybe time to take a break."
            break
