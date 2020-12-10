import numpy as np

def calculate(lis):
  try:
    a=np.array(lis).reshape(3,3)
  except:
    raise ValueError("List must contain nine numbers.")
  
  mean=[list(np.mean(a,axis=0)),list(np.mean(a,axis=1)),np.mean(a)]
  variance=[list(np.var(a,axis=0)),list(np.var(a,axis=1)),np.var(a)]
  sd=[list(np.std(a,axis=0)),list(np.std(a,axis=1)),np.std(a)]
  maxi=[list(np.amax(a,axis=0)),list(np.amax(a,axis=1)),np.amax(a)]
  mini=[list(np.amin(a,axis=0)),list(np.amin(a,axis=1)),np.amin(a)]
  sumation=[list(np.sum(a,axis=0)),list(np.sum(a,axis=1)),np.sum(a)]

  calculations={
  'mean': mean,
  'variance': variance,
  'standard deviation':sd,
  'max': maxi,
  'min': mini,
  'sum': sumation
  }
  return calculations