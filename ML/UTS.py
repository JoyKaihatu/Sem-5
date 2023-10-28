import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet


df_train = pd.read_excel('Dataset.xlsx', sheet_name='Training')
df_test = pd.read_excel('Dataset.xlsx', sheet_name='Testing')
df_train = df_train.replace('nol', 0)
df_train = df_train.replace('satu', 1)

df_train.fillna(df_train.mean(), inplace=True)

X_train = df_train[['U', 'V', 'W', 'X']].to_numpy()
y_train = df_train['Z'].to_numpy()
X_test = df_test[['U', 'V', 'W', 'X']].to_numpy()
split_ratio = 0.8
split_index = int(len(X_train) * split_ratio)
X_training, X_validation = X_train[:split_index], X_train[split_index:]
y_training, y_validation = y_train[:split_index], y_train[split_index:]
alpha = 0.1
model = ElasticNet(alpha=alpha)

model.fit(X_training, y_training)

y_pred_test = model.predict(X_test)


df_test['Z'] = y_pred_test


nrp = "c14210176"
output_file = f"{nrp}.xlsx"

#Hapus openpyxl dari ExcelWriter
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    df_train.to_excel(writer, sheet_name='Training', index=False)
    df_test.to_excel(writer, sheet_name='Testing', index=False)

print(f"Hasil prediksi disimpan dalam file Excel: {output_file}")




