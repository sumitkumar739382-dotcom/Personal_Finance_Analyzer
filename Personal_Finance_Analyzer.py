import sys
def Mean(A):       #        sum of values in A
    n=len(A)       #MEAN = -------------------
    if n==0:       #             N  
        return 0
    return sum(A)/n
         
def dispersion(A,m):                           #calculating Standard deviation 
    n=len(A)                                   #           sum of (Xi-MEAN)^2
    var=sum([(A[i]-m)**2 for i in range(n)])/n #VARIANCE = -------------------  SD = (VARIANCE)^(1/2)
    return var**(1/2)                          #                  N      

def Max(exp):
    n=len(exp)
    if n==0:
        return 0
    ma_x=exp[0]
    for i in range(n):
        if ma_x<=exp[i]:
            ma_x=exp[i]
    return ma_x       

def Min(exp):
    n=len(exp)
    if n==0:
        return 0 
    mi_n=exp[0]
    for i in range(n):
        if exp[i]<=mi_n:
            mi_n=exp[i]            
    return mi_n 

def Sort(A):                        #Implemented SELECTION sort (Ascending order)
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                A[j],A[i]=A[i],A[j]
    return A
    
def med(A):
    n=len(A)
    if n==0:
        return 0                    #          (N/2+1)th value + (N/2)th value
    sorted_exp=Sort(A.copy())       # MEDIAN = --------------------------------  if N is ODD
    if n%2==0:                      #                       2
        return ((sorted_exp[n//2-1])+(sorted_exp[n//2]))/2      #           N
    else:                                                       # MEDIAN= -----th value if N is SVEN
        return sorted_exp[n//2]                                 #            2

def rxy(exp,wh,MEAN_X,MEAN_Y,SD_X,SD_Y):
    if len(exp)!=len(wh):
        return 0
    elif SD_X == 0 or SD_Y == 0:
        return 0
    n=len(exp)    
    dev_x=[(x-MEAN_X) for x in exp] 
    dev_y=[(y-MEAN_Y) for y in wh]
    sum_devx=0
    for i in range (n):
        sum_devx+=(dev_x[i]*dev_y[i])
    Covariance=sum_devx/n  
    return Covariance/(SD_X*SD_Y)    

def c_moment(exp,MEAN_X):
    central={}
    n=len(exp)
    for i in range(5):                                     #         SUM( (Xi-MEAN)^R )
        central[i]=sum([(x-MEAN_X)**i for x in exp])/n     #Mu_R  = ----------------------
    return central                                         #                 N

    
#input function here 
while(1):
    month=input("Enter name of month : ")
    if month=='13':
        sys.exit()
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
#------------DATA COLLECTION-------------#
for i in range(days):  
    expense[i]=[]
    raw_e=input(f"Expense on  {i+1} {month} {year} : ")
    raw_w=input(f"working hour on {i+1} {month} {year} : ")
    e=float(raw_e) if raw_e!="" else 0.0
    w=float(raw_w) if raw_w!="" else 0.0
    
    expense[i].append(e)
    expense[i].append(w)
#------------DATA EXTRACTION-------------#
exp=list(expense[i][0] for i in range(days))
wh=list(expense[i][1] for i in range(days))

#------CALCULATION---------#
#storing all constant-calculated values in global variables to use them multiple times
MEAN_X= Mean(exp)
MEAN_Y= Mean(wh)

SD_X=dispersion(exp,MEAN_X)
SD_Y=dispersion(wh,MEAN_Y)
mi_n=Min(exp)

ma_x=Max(exp)

MEDIAN_X=med(exp)
MEDIAN_Y=med(wh)
MOMENT_C=c_moment(exp,MEAN_X)
R=rxy(exp,wh,MEAN_X,MEAN_Y,SD_X,SD_Y)
relation = (
    "strongly positively" if R >= 0.5 else
    "strongly negatively" if R <= -0.5 else
    "weakly"
)
report = (
        f"\n============= Monthly Work-Expense Report ==============\n"
        f"Month / Year        : {month} / {year}\n"
        f"--------------------------------------------------------\n"
        f"Total Expense           : {sum(exp)} Rs\n"
        f"Total Work hour         : {sum(wh)} hour\n" 
        f"Average Expense         : {MEAN_X} Rs per day\n"
        f"Average work hour       : {MEAN_Y} hour per day\n"
        f"Median Expense          : {MEDIAN_X} Rs\n"
        f"Median work hour        : {MEDIAN_Y} hour\n"
        f"Standard Deviation(exp) : {SD_X}\n"
        f"Minimum Expense         : {mi_n} Rs\n"
        f"Maximum Expense         : {ma_x} Rs\n"
        f"Correl. Coeff.(rxy)     : {R}\n"
        f"Skewness(beta1)         : {(MOMENT_C[3]**2)/(MOMENT_C[2]**3)}\n"
        f"Kurtosis(gamma2)        : {(MOMENT_C[4])/(MOMENT_C[2]**2)-3}\n"
        f"--------------------------------------------------------\n"
        f"Interpretation:\n"
        f"- 50% of daily expenses are ≤ {MEDIAN_X} Rs\n"
        f"- You have worked ≤ {MEDIAN_Y} hours in 50% of month.\n"
        f"- Expenses varied between {mi_n} Rs and {ma_x} Rs\n"
        f"- Expenses are {relation} dependent on work hours\n"
        f"- "
        f"========================================================\n"
    )
print(report)
