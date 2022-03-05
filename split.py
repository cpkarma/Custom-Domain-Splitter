import warnings
import sys
warnings.filterwarnings("ignore")
sys.tracebacklimit = 0
print "\nSplitter\n"
BeJCVf = input("Enter Split Number: ")
JxRuvs = None
with open(raw_input('Enter a filename: ')) as YFMivCY:
    for nvZpWq, line in enumerate(YFMivCY):
        if nvZpWq % BeJCVf == 0:
            if JxRuvs:
                JxRuvs.close()
            GrvFFu = 'split_{}.txt'.format(nvZpWq + BeJCVf)
            JxRuvs = open(GrvFFu, "w")
        JxRuvs.write(line)
    if JxRuvs:
        JxRuvs.close()