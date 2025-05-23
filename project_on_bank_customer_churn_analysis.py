# -*- coding: utf-8 -*-
"""Project on Bank customer churn Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ugOn7EbnQlI7Cj5LC8g02rrRhGyM3eI3

# Project Title : Bank Customer Churn Analysis
"""

#Import the library
import pandas as pd
df=pd.read_csv("/content/Customer-Churn-Records.csv") # Load Bank datasets with path

#11 Check the percentage of missing data and handle accordingly.
missing_count=df.isna().sum() #finding missing values
print(missing_count)

percentage_missing_count=df.isna().sum()/len(df)*100  #finding percenatge of missing data values
print(percentage_missing_count)

"""In the above data sets we couldn't find any missing values"""

# 12.How many rows and columns are there in the dataset?
Rows,cols=df.shape #find rows and columns present in the datasets

print(f"The dataset has {Rows} rows and {cols} columns.")

# 13.What is the distribution of churned vs. non-churned customers? Method-1
churned_customer=df[df['Exited']==1].shape[0]   #finding churn customer
Non_churn_customer=df[df['Exited']==0].shape[0] #finding Non churn customer

Total_customer= df.shape[0]                  #Total customer inthe datasets
percentage_churned_customer=(churned_customer/Total_customer)*100 #fining percentage of churn customer
percentage_Non_churn_customer=(Non_churn_customer/Total_customer)*100 ##fining percentage of Non churn customer

print(f"Distribution of churned_customer: {percentage_churned_customer}%")
print(f"Distribution of Non_churn_customer: {percentage_Non_churn_customer}%")

churn_count = df['Exited'].value_counts() # Method-2
Total_customer= df.shape[0]
percentage_churn_count= (churn_count/Total_customer)*100
print(f"Churn distribution: {percentage_churn_count}%")

"""Here in the above code, 0= percenatge of Non Churn customer values and 1= percenatge of churn customer values which shows distribution among both customers and Below are graphical representation"""

#plot bar chart
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Exited',palette='Set2',hue="Exited")
plt.title('Distribution of Churned vs. Non-Churned Customers')
plt.xlabel('Exited')
plt.ylabel('Number of Customers')
plt.show()

# 14.What is the distribution of EstimatedSalary of churned and retained Customers?

Churned_customer= df[df['Exited']==1]['EstimatedSalary'] # calculate churned customer
Retained_customer=df[df['Exited']==0]['EstimatedSalary'] # calculate Retained customer

print(f"Distribution of Churned Customers EstimatedSalary:{Churned_customer}\n")
print(f"Distribution of Retained Customers EstimatedSalary:{Retained_customer}\n")

"""In the above code you can see numerical represenatation of Estimated salary of Churned and Retained Customer.
Now below you can see graphical represenatation :
"""

#plot the histogram
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='EstimatedSalary', hue='Exited', kde=True, bins=30, palette={0: 'green', 1: 'red'})
plt.title('Distribution of EstimatedSalary for Churned and Retained Customers')
plt.xlabel('Estimated Salary')
plt.ylabel('Count')
plt.legend(title='Exited', labels=['Retained (0)', 'Churned (1)'])
plt.grid(True)
plt.show()

# 15.How do churn rates vary by Gender, Geography, and IsActiveMember?

Churn_customer=df[df['Exited']==1].shape[0] # churned customer
Total_customer=df.shape[0]                  # Total Customer
churn_rate=(Churn_customer/Total_customer)*100 # calculate churn customer

churn_rate_summary = df.groupby(['Gender', 'Geography', 'IsActiveMember'])['Exited'].agg(['count', 'sum'])
print(f"Churn rates vary by Gneder, Geography,IsActiveMember :{churn_rate_summary}")

# 16.What is the average CreditScore, Balance, and EstimatedSalary of churned vs. retained customers?

Average_churned__creditscore= df[df['Exited']==1]['CreditScore'].mean() #finding average of churn creditscore

Average_churned_Balance= df[df['Exited']==1]['Balance'].mean() # finding avaerage of churn balance

Average_churned_Estimatedsalary= df[df['Exited']==1]['EstimatedSalary'].mean() #finding avaerage of churn estimatedsalary

Average_Retained__creditscore= df[df['Exited']==0]['CreditScore'].mean()  #finding average of Retained creditscore

Average_Retained__Balance= df[df['Exited']==0]['Balance'].mean() #finding average of Retained Balance

Average_Retained__EstimatedSalary= df[df['Exited']==0]['EstimatedSalary'].mean() #finding average of Retained Estimatedsalary

print(f"Average churned customer creditscore Vs Average Retained customer CreditScore : {Average_churned__creditscore} vs {Average_Retained__creditscore}")

print(f"Average churned customer Balance Vs Average Retained customer Balance : {Average_churned_Balance} vs {Average_Retained__Balance}")

print(f"Average churned customer EstimatedSalary Vs Average Retained customer EstimatedSalary : {Average_churned_Estimatedsalary} vs {Average_Retained__EstimatedSalary}")

# 18.Is there any correlation among numeric features like CreditScore, Balance, and EstimatedSalary?

Correlation = df[['CreditScore','Balance','EstimatedSalary']].corr() #calculate Correlation amoung numeric features

print(f"Correlation amoung the numeric features is:{Correlation}")

"""IN the above code it shows numerical correlation representation amoung features and Below Shows Graphical represenatation"""

# Plot heatmap
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
sns.heatmap(Correlation, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation Matrix of Numeric Features")
plt.show()

# 19.What does a heatmap reveal about feature interactions with churn?

Churn_Correlation=df[['Exited']].corr() # Calculate churn correlation
print(f"The Feature Churn Correlation is :{Churn_Correlation} ")

"""In the above code is churn numeric correlation and Below are the Graphical representation"""

# Plot heatmap of features correlated with churn
plt.figure(figsize=(6, 8))
sns.heatmap(Churn_Correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1, cbar=True, linewidths=0.5)
plt.title('Feature Correlations with Churn')
plt.show()

# 22.Are customers with only one product (NumOfProducts = 1) more likely to churn than those with multiple?

Churn_rate_one_product= df[df['NumOfProducts']==1]['Exited'].mean()

Churn_rate_multiple_products=df[df['NumOfProducts']>1]['Exited'].mean()

print(f"The Churn rate with one product:{Churn_rate_one_product:.2%}")

print(f"The Churn rate with Multiple product:{Churn_rate_multiple_products:.2%}")

"""Yes,Customer with only one product is more likely to churn than with multiple products"""

