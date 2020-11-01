import numpy as np
import scipy.stats

def testStatistic( data, mu ) : 
  # Your code to compute the testStatistic that is described
  # in the text on the right should be calculated here
  
  
def pvalue( data, mu ) :
  T = testStatistic(data, mu )
  # You should add code here that uses the T value that is returned from 
  # testStatistic to determine the p-value for the hypothesis test.
  

# The code from here should not need to be modified
data = np.array([9.85008797, 7.82650698, 8.42464614, 5.84667192, 10.10269628, 8.20009795])
print("The null hypothesis is that the data is a set of samples from a distribution")
print("with an expectation of 7")
print("The alternative hypothsis is that the data is a set of samples from a distribution")
print("with an expectation that not equal to 7")
print("The p-value for this hypothesis test is", pvalue(data, 7) )
