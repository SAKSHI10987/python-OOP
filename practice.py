class Computation:
  def Factorial(self,n):
    i=1
    fact=1
    while(i<=n):
      fact*=i
      i+=1
    return fact

  def naturalSum(self,n):
    i=0
    sum=0
    while(i<=n):
      sum+=i
      i+=1
    return sum

  def testPrime(self,n):
    flag=0
    for i in range(2,n):
      if(n%i==0):
        flag=1
    if(flag==0):
      return "prime"
    else:
      return "not prime"

  def testPrims(self,n1,n2):
    dn1=[]
    for i in range(1,n1):
      if(n1%i==0):
        dn1.append(i)
    dn2=[]
    for i in range(1,n2):
      if(n2%i==0):
        dn2.append(i)
    
    count=0
    for i in range(0,len(dn1)):

      for j in range(0,len(dn2)):
        if(dn1[i]==dn2[j]):
          count+=1
    if(count==1):
      return "numbers are prime between them"
    else:
      return "numbers are not prime between them"

  def tableMul(self,n):
    for i in range(1,11):
      print(f"{n}*{i}= {n*i}")

  def allTableMul(self):
    for i in range(1,10):
      for j in range(1,11):
        print(f"{i}*{j}= {i*j}")
      print() 

  def listDiv(self,n):
    ldiv=[]
    for i in range(1,n+1):
      if(n%i==0):
        ldiv.append(i)
    return ldiv
  
  def listDivPrim(self,n):
    ldiv=[]
    for i in range(1,n+1):
      if(n%i==0):
        ldiv.append(i)
    

    lpdiv=[]
    for i in ldiv:
      flag=0
      for j in range(2,i):
        if(i%j==0):
          flag=1
      if(flag==0):
        lpdiv.append(i)
    return lpdiv

c1=Computation()

c=c1.Factorial(5)
c2=c1.naturalSum(5)
print(c2)
print(c1.testPrime(6))
print(c1.testPrims(6,9))
c1.tableMul(5)
c1.allTableMul()
print(c1.listDiv(6))
print(c1.listDivPrim(6))

print(c)
          

  


