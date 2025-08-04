#main.py
import os
import sys

# Add 'src' directory to Python's path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

import util1

# Main function to call functions defined in util1.py for demonstration
def main():
    print(util1.intToRoman(55))
    print(util1.romanToInt('XIV'))   
    print(util1.lengthOfLongestSubstring('sellffhhelp'))
    print(util1.reflect(util1.transpose([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])))
    print(util1.maxArea([1,8,6,2,5,4,8,3,7]))
    print(util1.pallindrome("malalam"))   

if __name__ == "__main__":
    main()
