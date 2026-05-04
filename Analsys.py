import pandas as pd
data = pd.read_csv(r"C:\Users\hi\Desktop\student.csv")
print("student data :\n",data)

data["Total"]= data["Maths"]+ data["Science"]+data["English"]

data["Average"]= data["Total"]/3
print("Total data :\n",data)

top_student = data.loc[data["Total"].idxmax()]
print("Top student :\n",top_student)

failed = data[
    (data["Maths"]<50) |
    (data["Science"]<50)|
    (data["English"]< 50)
]
print("Faield data :\n",failed)