def intToRoman(num):
  """This function will take an integer and convert it to Roman numeral"""
  roman=''
  romchar=[(1000,'M'), (900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
  for number, symbol in romchar:
      while(num-number >=0):
          roman+=symbol
          num=num-number
  return roman  


def romanToInt(s):
  """This function will take a roman number and convert it to integer"""
  s=s[::-1]
  romchar={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

  prev=romchar.get(s[0])
  intnum=prev

  for i in range(1,len(s)):
    cur=romchar.get(s[i])

    if cur<prev:
        intnum=intnum-cur
    else:
        intnum=intnum+cur
    prev=cur
    
  return intnum



def lengthOfLongestSubstring(s):
  """This function returns the longest substring in the given string till a repeating letter occurs"""
  chars=[0]*128
  left=right=0
  result=0

  while (right<len(s)):
    r=s[right]
    chars[ord(r)]+=1
    
    while(chars[ord(r)]>1):
        l=s[left]
        chars[ord(l)]-=1
        left+=1
    
    result=max(result,right-left+1)
    right+=1
  return result
 

def transpose(matrix):
  """Transponse a matrix"""
  for i in range(0,len(matrix)):
    for j in range(i,len(matrix)):
      temp=matrix[i][j]
      matrix[i][j]=matrix[j][i]
      matrix[j][i]=temp
  return matrix

def reflect(matrix):
  """Refelct a matrix on the primary diagonal"""
  for i in range(0,len(matrix)):
    for j in range(0,len(matrix)//2):
      temp=matrix[i][j]
      matrix[i][j]=matrix[i][len(matrix)-j-1]
      matrix[i][len(matrix)-j-1]=temp
  return matrix 


def maxArea(height):
  area=0
  left=0
  right=len(height)-1
  currentarea=0
  while(left<right):
      #print('Right ',height[right], 'left', height[left])
      currentarea=min(height[left],height[right])*(right-left)
      #print(currentarea)
      area=max(area,currentarea)
      if (height[left]<height[right]):
          left+=1
      else:
          right-=1
  return area


def pallindrome(inp):
  flag=0
  start=0
  end=len(inp)-1
  while(start!=end):
    
    if(inp[start]==inp[end]):
        start=start+1
        end=end-1
        flag=1
        
    else:
        flag=0
        break
    
  if flag==1:
    return 'Pallindrome'
  else:
    return 'Not Pallindrome'