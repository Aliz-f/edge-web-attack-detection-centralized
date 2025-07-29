# import pandas as pd
# import pickle
#
# # Load the dataset
# df = pd.read_csv('../../Edge-IIoTset_DNN-112.csv')
#
# # Load selected features
# with open("selected_features_15class_mi.pkl", "rb") as f:
#     selected_features = pickle.load(f)
#
# top_k = 15  # Number of features to show
# core_features = selected_features[:top_k]
#
# # Select one example of each class
# example_rows = df.groupby('Attack_type').apply(lambda x: x.sample(1, random_state=1)).reset_index(drop=True)
#
# # Reorder columns: selected features first, then Attack_label and Attack_type
# ordered_cols = core_features + ['Attack_label', 'Attack_type']
# example_rows = example_rows[ordered_cols]
#
# import dataframe_image as dfi
# dfi.export(example_rows, "example_rows.png")

import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
import dataframe_image as dfi

# Load the dataset
df = pd.read_csv('Edge-IIoTset_DNN-112.csv')

# Load selected features
with open("selected_features_15class_mi.pkl", "rb") as f:
    selected_features = pickle.load(f)

top_k = 5  # Number of features to show
core_features = selected_features[:top_k]

# Fit scaler on full dataset (recommended way)
scaler = StandardScaler()
scaler.fit(df[core_features])

# Select one example of each class
example_rows = df.groupby('Attack_type').apply(lambda x: x.sample(1, random_state=1)).reset_index(drop=True)

# Apply standardization to selected features only
example_rows_scaled = example_rows.copy()
example_rows_scaled[core_features] = scaler.transform(example_rows[core_features])

# Reorder columns: selected features first, then Attack_label and Attack_type
ordered_cols = core_features + ['Attack_label', 'Attack_type']
example_rows_scaled = example_rows_scaled[ordered_cols]

# Export as image
dfi.export(example_rows_scaled, "example_rows_scaled.png")
