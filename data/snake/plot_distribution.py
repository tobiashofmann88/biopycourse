import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import csv
import seaborn as sns
sns.set(color_codes=True)

def plot_distribution_two_lists(path,output):
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        reader = list(reader)
        fastq1 = reader[0]
        fastq2 = reader[1]
        fastq1 = np.asarray(fastq1)
        fastq1 = fastq1.astype(float)
        fastq2 = np.asarray(fastq2)
        fastq2 = fastq2.astype(float)
        plotted = sns.distplot(fastq1)
        plotted = sns.distplot(fastq2)
        plotted.figure.savefig(output)

#path = '/Users/tobias/GitHub/biopycourse/data/snake/merged.txt'
#plot_distribution_two_lists(path,'/Users/tobias/Desktop/test_plot.png')