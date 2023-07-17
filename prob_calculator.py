import copy
import random
# Consider using the modules imported above.

class Hat:
    
  def __init__(self, **kwargs):
    self.contents = []
    for bila, num in kwargs.items():
      for i in range(num):
        self.contents.append(bila)
              
  def draw(self, x):
    self.scadere=copy.copy(self.contents)
    self.bilescoase=[]
    if x>len(self.scadere): return self.contents
    else: 
      for i in range(x):
          ind=random.randint(0,len(self.scadere)-1)
          self.bilescoase.append(self.scadere[ind])
          del self.scadere[ind]
    return(self.bilescoase)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
 
  tinta=[]
  m=0
  
  for bila, num in expected_balls.items():
      for i in range(num):
        tinta.append(bila)

  for i in range(num_experiments):
      check=0
      bilesc=hat.draw(num_balls_drawn)
      bilesc2=copy.copy(bilesc)
      for x in tinta: 
        if x in bilesc:
            check+=1
            bilesc.remove(x)
      if(len(tinta)==check):  
            m+=1

  return(m/num_experiments)
  
  