def arithmetic_arranger(problems, test=False):
  top=str()
  bot=str()
  lines=str()
  result=str()
  calc=0
  maxim=0
  
  if len(problems)>5:
      return("Error: Too many problems.")
  else:
      for i in problems:
        i=i.split()
        if (i[1]=='*' or i[1]=='/'):
          return("Error: Operator must be '+' or '-'.") 
          break
        elif not(i[0].isnumeric() and i[2].isnumeric()): 
          return("Error: Numbers must only contain digits.") 
          break
        elif (len(i[0])>4 or len(i[2])>4):
          return("Error: Numbers cannot be more than four digits.") 
          break
        else:
          maxim=max(len(i[0]),len(i[2]))
          
          top+=("  "+" "*(maxim-len(i[0])) +i[0]+ " "*4)
          bot+=(i[1]+" "+" "*(maxim-len(i[2])) + i[2] + " "*4)
          lines+=("-"*(maxim+2)+" "*4)
          if (i[1]=='+'):
            calc=str(int(i[0])+int(i[2]))
          if (i[1]=='-'):
            calc=str(int(i[0])-int(i[2]))
          result+=(" "*(maxim+2-len(calc))+calc+ " "*4)
      top=top.rstrip() + ('\n')
      bot=bot.rstrip() + ('\n')
      lines=lines.rstrip()
      result=result.rstrip()
      if(test==True):
        lines+=('\n')
        arranged_problems=top+bot+lines+result
      else:
        arranged_problems=top+bot+lines
  
      return arranged_problems