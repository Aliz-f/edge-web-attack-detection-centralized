from sklearn.feature_selection import mutual_info_classif
import pandas as pd
import numpy as np
import pickle

# Load the preprocessed dataset
df = pd.read_csv('../../Edge-IIoTset_ML-112.csv')

# Creating a dictionary of Types
attacks = {'Normal': 0,
           'MITM': 1,
           'Uploading': 2,
           'Ransomware': 3,
           'SQL_injection': 4,
           'DDoS_HTTP': 5,
           'DDoS_TCP': 6,
           'Password': 7,
           'Port_Scanning': 8,
           'Vulnerability_scanner': 9,
           'Backdoor': 10,
           'XSS': 11,
           'Fingerprinting': 12,
           'DDoS_UDP': 13,
           'DDoS_ICMP': 14}

df['Attack_type'] = df['Attack_type'].map(attacks)
X = df.drop(columns=['Attack_label', 'Attack_type'])
y = df['Attack_label']

# Compute MI
mi_scores = mutual_info_classif(X, y, discrete_features='auto', random_state=42)

mi_df = pd.DataFrame({'feature': X.columns, 'score': mi_scores})
mi_df = mi_df.sort_values(by='score', ascending=False)


# Choose top-K
top_k = 30
selected_features = mi_df['feature'].tolist()[:top_k]

# Save feature list to a file
with open("selected_features_binary_mi.pkl", "wb") as f:
    pickle.dump(selected_features, f)
