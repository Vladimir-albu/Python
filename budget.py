class Category:
  
  def __init__(self, description):
    self.description=description
    self.ledger=[]
    self.balance=0

  def deposit(self, value, description=str()):
    self.ledger.append({'amount': value, 'description': description})
    self.balance+=value

  def withdraw(self, minu, description=str()):
    if self.balance>=minu:
     self.ledger.append({'amount': -1*minu, 'description': description})
     self.balance-=minu
     return True
    else: return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, cat):
    if self.balance>=amount:
        self.withdraw(amount, ('Transfer to {}'.format(cat.description)))
        cat.deposit(amount, ('Transfer from {}'.format(self.description)))
        return True
    else: return False

  def check_funds(self, amount):
    if self.balance>=amount: return True
    else: return False

  def __repr__(self):
    header=self.description.center(30, '*') + '\n'
    for i in self.ledger:
          newdesc='{:.23}'.format(str(i['description']))
          deamm='{:.2f}'.format(i['amount'])
          header += '{:<23}'.format(newdesc) + '{:>7}'.format(deamm) + '\n'
    total='Total: {:.2f}'.format(self.balance)
    return header+total

def create_spend_chart(categories):
  barchart=('Percentage spent by category\n')
  total={}
  percentage={}
  everything=0
  maxlen=0
  count=0
  for i in categories:
    total[i]=0
    count+=1
    for b in i.ledger:
      if b['amount']<0: total[i]+=b['amount']
    if len(i.description)>maxlen: maxlen=len(i.description)
    everything+=total[i]
  for i in categories:
    try: percentage[i]=int(total[i]/everything*10)*10
    except: percentage[i]=0
  for x in range(11):
    ind=100-x*10
    barchart+="{:>3}| ".format(str(ind))
    for i in categories:
      if percentage[i]>=ind: barchart+='{}  '.format('o')
      else: barchart+='   '
    barchart+='\n'
  
  barchart+='    {}\n'.format('-'*(count*3+1))

  for x in range(maxlen-1):
    barchart+='     '
    for i in categories:
      if len(i.description)>x:
        barchart+=list(i.description)[x] + '  '
      else: barchart+='   '
    barchart+='\n'
  barchart+='     '
  for i in categories:
    if len(i.description)>maxlen-1:
      barchart+=list(i.description)[maxlen-1] + '  '
    else: barchart+='   '
  
  return barchart
      
    
    
   