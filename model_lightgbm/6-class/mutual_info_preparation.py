from sklearn.feature_selection import mutual_info_classif
import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('../../Edge-IIoTset_ML-112.csv')

df['Attack_type'] = df['Attack_type'].str.replace('DDoS_TCP', 'DDoS')
df['Attack_type'] = df['Attack_type'].str.replace('DDoS_UDP', 'DDoS')
df['Attack_type'] = df['Attack_type'].str.replace('DDoS_HTTP', 'DDoS')
df['Attack_type'] = df['Attack_type'].str.replace('DDoS_ICMP', 'DDoS')

df['Attack_type'] = df['Attack_type'].str.replace('Port_Scanning', 'Scanning')
df['Attack_type'] = df['Attack_type'].str.replace('Fingerprinting', 'Scanning')
df['Attack_type'] = df['Attack_type'].str.replace('Vulnerability_scanner', 'Scanning')

df['Attack_type'] = df['Attack_type'].str.replace('MITM', 'MITM')

df['Attack_type'] = df['Attack_type'].str.replace('XSS', 'Injection')
df['Attack_type'] = df['Attack_type'].str.replace('SQL_injection', 'Injection')
df['Attack_type'] = df['Attack_type'].str.replace('Uploading', 'Injection')

df['Attack_type'] = df['Attack_type'].str.replace('Backdoor', 'Malware')
df['Attack_type'] = df['Attack_type'].str.replace('Password', 'Malware')
df['Attack_type'] = df['Attack_type'].str.replace('Ransomware', 'Malware')

# Creating a dictionary of Types
attacks = {
    'Normal': 0,
    'DDoS': 1,
    'Scanning': 2,
    'Injection': 3,
    'MITM': 4,
    'Malware': 5
    }
df['Attack_type'] = df['Attack_type'].map(attacks)

X = df.drop(columns=['Attack_label', 'Attack_type'])
y = df['Attack_type']

# Compute MI
mi_scores = mutual_info_classif(X, y, discrete_features='auto', random_state=42)

mi_df = pd.DataFrame({'feature': X.columns, 'score': mi_scores})
mi_df = mi_df.sort_values(by='score', ascending=False)


# Choose top-K
top_k = 50
selected_features = mi_df['feature'].tolist()[:top_k]

# Save feature list to a file
with open("selected_features_6class_mi.pkl", "wb") as f:
    pickle.dump(selected_features, f)
