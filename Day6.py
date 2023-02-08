
import re
from collections import Counter


def main():
    f=open('Day6.txt')
    signal=f.read()
    f.close()
    for i in range(13,len(signal)):
        j=Counter(signal[i-13:i+1])
        if len(j)==14:
            print(i+1)
            break
    
if __name__ == '__main__':
    main()
    
    