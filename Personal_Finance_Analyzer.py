#22/12/25
def m_ean(exp):      #        sum of expenses
    n=len(exp)       #MEAN = ----------------
    if n==0:         #            N  
        return 0
    return sum(exp)/n
         
def dispersion(exp):#calculating Standard deviation 
    n=len(exp)                                      #           sum of (Xi-MEAN)^2
    var=sum([(exp[i]-MEAN)**2 for i in range(n)])/n #VARIANCE = -------------------  SD = (VARIANCE)^(1/2)
    return var**(1/2)                               #                  N      

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
    return m_ax(exp)-m_in(exp)

def s_ort(exp1):                          #Implemented bubble sort (Ascending order)
    for i in range(len(exp1)):
        for j in range(i+1,len(exp1)):
            if exp1[i]>exp1[j]:
                exp1[j],exp1[i]=exp1[i],exp1[j]
    return exp1
    
def med(exp1):
    n=len(exp1)                  #          (N/2+1)th value + (N/2)th value
    sorted_exp=s_ort(exp1)       # MEDIAN = ---------------------------------------------  if N is ODD
    if n%2==0:                   #                       2
        return ((sorted_exp[n//2-1])+(sorted_exp[n//2]))/2      #           N
    else:                                                       # MEDIAN= -----th value if N is SVEN
        return sorted_exp[n//2]                                 #            2

#input function here 
while(1):
    print("Enter 13 in month to terminate")
    month=input("Enter name of month : ")
    if month=='13':
        break
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
            days=28
            break
    
    else:
        print("\nEnter valid month/year")
        continue

for i in range(days):        
    expense[i]=float(input(f"Expense of {i+1} {month} {year} : "))
    
exp=list(expense.values())
exp1=exp.copy()

#storing all constant-calculated values in global variables to use them multiple times
MEAN = round(m_ean(exp),2)

SD=round(dispersion(exp),2)

mi_n=m_in(exp)

ma_x=m_ax(exp)

MEDIAN=med(exp)

RANGE=r_ange(exp)
report = (
        f"\n================ Monthly Expense Report ================\n"
        f"Month / Year        : {month} / {year}\n"
        f"--------------------------------------------------------\n"
        f"Total Expense       : {sum(exp)}\n"
        f"Average Expense     : {MEAN} per day\n"
        f"Median Expense      : {MEDIAN}\n"
        f"Standard Deviation  : {SD}\n"
        f"Minimum Expense     : {mi_n}\n"
        f"Maximum Expense     : {ma_x}\n"
        f"--------------------------------------------------------\n"
        f"Interpretation:\n"
        f"- 50% of daily expenses are ≤ {MEDIAN}\n"
        f"- Expenses varied between {mi_n} and {ma_x}\n"
        f"========================================================\n"
    )
print(report)
