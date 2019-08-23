def median(x):
 i = len(x) // 2
 if len(x) % 2 == 0:
  return (x[i] + x[i-1]) / 2
 return x[i]

def mean(x):
 return sum(x) / len(x)

def variance(x):
 m = mean(x)
 i = 0
 v = 0
 n = len(x)
 while i < n:
  v += (x[i] - m)**2
  i += 1
 v /= n - 1
 return v
 
def deviation(x):
 return variance(x)**0.5
  
def Q1(x):
 n = len(x) // 2
 x = x[:n]
 return median(x)
 
def Q3(x):
 n = len(x) // 2
 x = x[n+1:]
 return median(x)

def IQR(x):
 return Q3(x) - Q1(x)
 
def outliers(nums):
 iqr = IQR(nums)
 iqr *= 1.5
 q1 = Q1(nums)
 min = q1 - iqr
 q3 = Q3(nums)
 max = q3 + iqr
 res = []
 for num in nums:
  if num < min or num > max:
   res.append(num)
 if len(res) == 0:
  return 0
 return res
 
def FNS(x):
 minimum = min(x)
 q1 = Q1(x)
 mid = median(x)
 q3 = Q3(x)
 maximum = max(x)
 print("Minimum: ", minimum, "\nQ1: ", q1, "\nMedian: ", mid, "\nQ3: ", q3, "\nMaximum: ", maximum)
 
def stemLeafToList(x, n):
 i = 0
 y = []
 while i < len(x):
  for j in x[i]:
   y.append(i*n+int(j,10))
  i += 1
 return y
 
 class StemPlot:
  y = []
  
  def __init__(self, plot):
   self.y = spFromList(plot)
   
  def spFromList(plot):
   i = 0
   while i < len(x):
    for j in x[i]:
     self.y.append(i*n+int(j,10))
    i += 1
    
  def toList():
   return self.y