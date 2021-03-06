#!/usr/bin/python3
# INPUT: a file with Burmese sentences in each line.
# OUTPUT: segmentation results to the terminal output (with two double spaces between words)
import os
from subprocess import call, check_output
import sys
import re

def segment(inputF):
    with open(inputF, 'r') as f:
        for line in f:
            if line == '\n':
                continue
            #if cnt > MAX:
            #    continue

            #print("Sentence:", line)

            ####################### using segmenter ###################################
            output = check_output(["./segment" + " burmese2.fst '" + line + "'"], shell=True)
            outStr = output.decode('utf-8')
            outStr = outStr.replace(" ", "|")
            outStr = outStr.replace("၊", "|၊|")
            outStr = outStr.replace("။", "|။")
            outStr = re.sub(r"(?P<punc>[\(\)\-\"\'])","|\g<punc>|", outStr)
            outStr = re.sub(r"(?P<eng>[0-9a-zA-Z]+)","|\g<eng>|", outStr)
            outStr = re.sub(r"(?P<bur_digits>[၀-၉,\.]+)","|\g<bur_digits>|", outStr)
            outStr = outStr.replace("||", "|")
            outStr = outStr.replace("|", "  ")
            outStr = outStr.replace("\n", '')
            ####################### end using segmenter
            print(outStr)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        segment(sys.argv[1])
    else:
        print("Please provide an input file.")
