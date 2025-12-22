#import pandas as pd
def m_ean(exp):
    n=len(exp)
    if n==0: 
        return 0
    mean=sum(exp)/n
    return mean 
    
def dispersion(exp):#calculating Standard deviation 
    n=len(exp)
    var=sum([(exp[i]-m_ean(exp))**2 for i in range(n)])/n
    return var**(1/2)

def m_ax(exp):
    n=len(exp)
    ma_x=exp[0]
    for i in range(n):
        if ma_x<=exp[i]:
            ma_x=exp[i]
    return ma_x       

def m_in(exp):
    n=len(exp)
    mi_n=exp[0]
    for i in range(n):
        if exp[i]<=mi_n:
            mi_n=exp[i]            
    return mi_n            
def r_ange(exp):
    return max(exp)-min(exp)

def s_ort(exp1):#Implemented bubble sort (Ascending order)
    for i in range(len(exp1)):
        for j in range(i+1,len(exp1)):
            if exp1[i]>exp1[j]:
                exp1[j],exp1[i]=exp1[i],exp1[j]
    return exp1
    
def med(exp1):
    n=len(exp1)
    sorted_exp=s_ort(exp1)
    if n%2==0:
        return ((sorted_exp[n//2-1])+(sorted_exp[n//2]))/2 
    else:
        return sorted_exp[n//2]  

#input function here 
while(1):
    month=input("Enter name of month : ")
    year=int(input("Enter Year : "))
    months_31=('JANUARY','MARCH','MAY','JULY','AUGUST','OCTOBER','DECEMBER')
    months_30=('APRIL','JUNE','SEPTEMBER','NOVEMBER')
    expense={}
    days=0
    if month.upper() in months_31:
        days=31
        break
    elif month.upper() in months_30:
        days=30
        break
    elif month.upper() == 'FEBRUARY':
        if (year%400==0) or (year%4==0 and year%100!=0):
            days=29
            break
    else:
        print("\nEnter valid month/year")
        continue
for i in range(days):        
    expense[i+1]=int(input(f"Expense of {i+1} {month} {year}"))  
#expense={1:20,2:30,3:40,4:50,5:60}

exp=list(expense.values())   
exp1=exp.copy()
MEAN = round(m_ean(exp),2)

SD=round(dispersion(exp),2)

MEDIAN=med(exp)

RANGE=r_ange(exp)
report = (
        f"\n================ Monthly Expense Report ================\n"
        f"Month / Year        : {month} / {year}\n"
        f"--------------------------------------------------------\n"
        f"Total Expense       : {total}\n"
        f"Average Expense     : {mean} per day\n"
        f"Median Expense      : {median}\n"
        f"Standard Deviation  : {sd}\n"
        f"Minimum Expense     : {min_exp}\n"
        f"Maximum Expense     : {max_exp}\n"
        f"--------------------------------------------------------\n"
        f"Interpretation:\n"
        f"- 50% of daily expenses are ≤ {median}\n"
        f"- Expenses varied between {min_exp} and {max_exp}\n"
        f"========================================================\n"
    )
print(report)
