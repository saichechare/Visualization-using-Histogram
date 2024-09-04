import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Employees.csv")

# creating numpy array
monthly_salary = np.array(data["Monthly Salary"].head(10))
annualy_salary = np.array(data["Annual Salary"].head(10))

# getting the name of emp
name_emp = data["First Name"].head(10) + data["Last Name"].head(10)

# creating the histogram
plt.bar(name_emp,monthly_salary, label="monthly")
plt.bar(name_emp,annualy_salary,label="annuly",alpha=0.7,color="red" )
plt.title("salary data of emp")
plt.tight_layout()
plt.show()