import pymongo

# Making Database and database tables

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["BusinessDB"]
sales = mydb["sales"]
credit=mydb["credit"]
cash=mydb["cash"]

# Taking all the inputs from the user

print("Enter sales of Product A")
ProductA_Sales=list(map(int,input().split()))
print("Enter sales of Product B")
ProductB_Sales=list(map(int,input().split()))
print("Enter sales of Product C")
ProductC_Sales=list(map(int,input().split()))
print("Enter sales of Product D")
ProductD_Sales=list(map(int,input().split()))
print("Enter credit Percentage")
CreditPercent=list(map(int,input().split()))

# Appending inputs to database tables

SalesData={"Product A" : ProductA_Sales,
           "Product B" : ProductB_Sales,
           "Product C" : ProductC_Sales,
           "Product D" : ProductD_Sales
           }
CreditData={"Percentage":CreditPercent}

x=sales.insert_one(SalesData)
y=credit.insert_one(CreditData)

# Processing inputs

ProductA_Cash=[0,0,0,0,0,0,0,0,0,0,0,0]
ProductB_Cash=[0,0,0,0,0,0,0,0,0,0,0,0]
ProductC_Cash=[0,0,0,0,0,0,0,0,0,0,0,0]
ProductD_Cash=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(12-len(CreditPercent)):
    for j in range(0,len(CreditPercent)):
        ProductA_Cash[i+j]+=ProductA_Sales[i]*CreditPercent[j]/100
        ProductB_Cash[i + j] += ProductB_Sales[i] * CreditPercent[j] / 100
        ProductC_Cash[i + j] += ProductC_Sales[i] * CreditPercent[j] / 100
        ProductD_Cash[i + j] += ProductD_Sales[i] * CreditPercent[j] / 100

# Appending output to database table

CashData={"Product A" : ProductA_Cash,
           "Product B" : ProductB_Cash,
           "Product C" : ProductC_Cash,
           "Product D" : ProductD_Cash
           }
z=cash.insert_one(CashData)
print("Sucessfull")