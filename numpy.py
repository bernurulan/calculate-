#Which type of data can be used while creating a series object in pandas?
import pandas as pd
import numpy as np
 #boolean,int,str(pandas)(any data type)

#2 Create a series having the month's number as data and assign name as their index values?

months = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]

}
ms = pd.Series(range(1, 13), index=months)
print(ms)

#3 Write a program to create a series object using the
# dictionary which store the number of students in fresh batch groups ( MatMIE, Mat DAIS, COMIE, COMEC)?
for_dic = {
    'MatMIE': 30,
    'MatDAIS': 25,
    'COMIE': 40,
    'COMEC': 35

for_dic= pd.Series(for_dic)

print(for_dic)

#4
exam_data_dataframe = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data_dataframe, index=labels)

print(df)
#5
result = df[df['attempts'] > 2]
print("Number of attempts in the examination is greater than 2:")
print(result)