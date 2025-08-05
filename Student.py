import matplotlib.pyplot as plt
import pandas as pd
import numpy as py
df=pd.read_excel("student.xlsx")
branch = df['branch']
students = df['students']
plt.figure(figsize=(10, 6))
plt.pie(students, labels=branch, autopct='%1.1f%%', startangle=140)
plt.title("branch wise students")
plt.axis('equal')
plt.show()