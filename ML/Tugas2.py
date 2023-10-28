import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import numpy as np

Bulan = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']



df1 = pd.read_excel("tugas2.xlsx",sheet_name="Sales_Profit",header=0,index_col=0)
df2 = pd.read_excel("tugas2.xlsx",sheet_name="Popular_Product",header=0,index_col=0)


# Data_frame = pd.DataFrame(df)
# df1_index =

Data_frame11 = pd.DataFrame(df1,index=df1.index)

Data_frame12 = Data_frame11.tail(1)
print(Data_frame12)
Data_frame12.index = ['']

df1 = df1.dropna()
df1 = df1.drop(['Average'])



Data_frame1 = pd.DataFrame(df1,index=df1.index)


Data_frame2 = pd.DataFrame(df2,index=df2.index)
Data_frame2.columns=['']
print()

print(df1)
print()
print(df2)

print(Data_frame1)

figure, axis = plt.subplots(2,2)

# Plot 1
plot1 = Data_frame1.plot(ax=axis[0,0], title='Profit Sales Bulanan',figsize=(12,7))
plot1.set_ylabel('Ribu Rupiah')
plot1.set_xlabel('Bulan')

# Plot 2
plot2 = Data_frame1.boxplot(ax=axis[1,0])
plot2.set_title('Variasi Profit per Sales')
# plot2.set_ylabel('Ribu Rupiah')

# Plot 3
plot3 = Data_frame2.plot(kind="pie",subplots=True,ax=axis[1,1],legend=True)
# plot3.legend(bbox_to_anchor=(1,1.02),loc='upper left')

# plot3.set_title('Popularitas Produk')
# plot3.set_ylabel('Ribu Rupiah')

# Plot 4
plot4 = Data_frame12.plot.bar(ax=axis[0,1])
plot4.set_title('Rata-Rata Profit Sales')
# Data_frame1.plot.area()


# Data_frame1.plot.bar()
# Data_frame1.plot.bar(stacked=True)

figure.tight_layout()


plt.show()