def add_time(start, duration, dweek=str()):
  text=str()
  dfweek=str()
  sh=int(start.split(':')[0])
  sm=int(start.split(':')[1].split()[0])
  mer=start.split()[1]

  dh=int(duration.split(':')[0])
  dm=int(duration.split(':')[1].split()[0])

  em=(sm+dm)%60                       #ending minute value
  if em<10: em='0'+str(em)
  
  if (sm+dm>60):
    dh+=1

  eh= (sh+dh)%12                         #ending hour value
  if(eh==0): eh=12

  if (((sh+dh)//12==1 and mer=='PM') or ((sh+dh)//12==2 and mer=='AM')):
    text=' (next day)'

  if (mer=='AM'):
    days=((sh+dh)//12)//2
  else: days=((sh+dh)//12+1)//2

  if (((sh+dh)//12)%2==1):
    if (mer=='AM'): mer='PM'
    else: mer='AM'

  if (days>1):
    text=' ('+ str(days) +' days later)'

  weekdays=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

  if (dweek.lower() in weekdays):
    dfweek=', '+ weekdays[(weekdays.index(dweek.lower())+days)%7].capitalize()
  
  

  new_time=str(eh)+':'+str(em)+' '+mer+dfweek+text
    
  return new_time