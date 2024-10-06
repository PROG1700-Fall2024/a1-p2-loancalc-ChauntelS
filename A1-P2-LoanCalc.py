#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Title
    print("Welcome! Let us calculate your weekly loan payment for you!")
    #Users input values
    #YearLength = int(input("Enter year length "))
    Loan = (float(input("Enter loan amount:")))
    IntrestRate = (float(input("Enter intrest rate in (%):")))
    YearLength = (int(input("Enter year length ")))
    #Value Math
    IntrestRateDecimal = (float(IntrestRate)/5200)
    LoanAmount = (float(IntrestRateDecimal*Loan)+(Loan))

    #Month = (YearLength/12)                            #<--
    #IntrestRateDecimal = (float(IntrestRate)/5200)     #   |- I left in all of my struggles as I'm scared if I delete anything it will no longer work.
    #IntrestAmount = (float(Loan*IntrestRateDecimal))   #<-- 

    Weeks= (YearLength*52)

    #Math
    #WeeklyPayment = (IntrestAmount/Weeks+Loan/Weeks)
    WeeklyPayment = (float(IntrestRateDecimal)/(1-(1+float(IntrestRateDecimal))**(-52*(int(YearLength))))*LoanAmount) #<--- The absolute struggle I had with this math is unreal!
    #WeeklyPayment = float(IntrestRate)/(1-(1+float(IntrestRate))**(-52*(float(Month))))*float(Loan)
    print('Weekly Calculated Payme:${0:.2f}'.format(float(WeeklyPayment)))
    #I can't for the life of me get this to calculate the exact answers of the "Other testing Values" but this is as close as I have been able to come.
    # YOUR CODE ENDS HERE

main()