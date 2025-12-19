def m_ean(exp):
    n=len(exp)
    if n==0:
        return 0
    mean=sum(exp)/n
    return mean 
def dispersion(exp):
    n=len(exp)
    var=sum([(exp[i]-MEAN)**2 for i in range(n)])/n
    return var**(1/2)
def med(exp):
    n=len(exp)
    sorted_exp=sorted(exp)
    if n%2 == 0:
        med=((sorted_exp[n//2-1])+(sorted_exp[n//2]))/2
    else:
        med=sorted_exp[(n+1)//2]
    return med    
month=input("Enter name of month : ")
year=int(input("Enter Year : "))
months=('JANUARY','MARCH','MAY','JULY','AUGUST','OCTOBER','DECEMBER')
expense={}
if month.upper() in months: 
    for i in range (1,32):
        expense[i]=int(input(f"Expense of {i} {month} {year}"))
elif month.upper() != 'FEBRUARY':
    for i in range (1,31):
        expense[i]=int(input(f"Expense of {i} {month} {year}"))
elif month.upper() == 'FEBRUARY' and year%4 == 0:
    for i in range (1,30):
        expense[i]=int(input(f"Expense of {i} {month} {year}"))
elif month.upper() == 'FEBRUARY' and year%4 != 0:
    for i in range (1,29):
        expense[i]=int(input(f"Expense of {i} {month} {year}"))
else:
    print("Enter valid month!!!!!")
exp=list(expense.values())   
MEAN = m_ean(exp)
SD=dispersion(exp)
MEDIAN=med(exp)
print(MEAN,SD,MEDIAN)
