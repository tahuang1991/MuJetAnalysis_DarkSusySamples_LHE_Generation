## edit lines 8 and 11
## run as: python replace_lifetime_in_LHE.py > someOutputFile.py

import array, os, re, math, random, string, sys
from math import *

## set your new ctau value here
#ctau_mean_mm = 5.0
ctau_mean_mm = float(sys.argv[1])
## set input file name

#filename = "DarkSUSY_mH_125_mGammaD_2000_ctauExp_0_13TeV-madgraph452_bridge224_events80k.lhe"
filenamefull = sys.argv[2]
filename = "DarkSUSY_mH_125_mGammaD_20_14TeV_cT_%.0f_madgraph452_bridge224_events50k.lhe"%(ctau_mean_mm)
print "original file ",filenamefull
print "after ctau replacement ",filename
os.system("cp %s %s"%(filenamefull, filename))
f = open(filenamefull, 'r')
event_begin = False
event_end = True

for line in f:
        if line == '<event>\n':
                event_begin = True
                event_end = False
        if line == '</event>\n':
                event_begin = False
                event_end = True
        new_line = ''
        if event_begin == True and event_end == False:
                word_n = 0
                for word in line.split():
                        if word == '3000022' or word_n > 0:
                                word_n = word_n + 1
                                if word_n < 13:
                                        if word_n == 12:
                                          ctau_mm = '%E' % random.expovariate(1.0/ctau_mean_mm) # exponential distribution                                                                                                                                                     
                                          #print "ctau (mm) mean: ", ctau_mean_mm, " actual: ", ctau_mm                                                                                                                                                                         
                                          new_line = new_line + ctau_mm + '   '
                                        else:
                                                new_line = new_line + word + '   '
                                else:
                                        new_line = new_line + word + '\n'
                                        word_n = 0
        if new_line == '':
                print line.rstrip('\n')
        else:
                print new_line.rstrip('\n')

f.close()





