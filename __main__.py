import pandas as pd

"""
Column Name | % Null
MMSI                        0.000000
datetime_utc                0.000000
lat                         0.000000
lon                         0.000000
speed_over_ground_knots     0.000000
course_over_ground_deg      0.000000
heading_deg                 0.000000
vessel_name                 0.000000
imo_number                 36.038359
call_sign                  17.305887
vessel_type_code           13.746126
status                     38.027169
length_m                   18.879829
width_m                    24.343390
draft_depth_m              71.965078
cargo_type_code            81.910967
transceiver_class           0.000000
datetime_hst                0.000000
vessel_class                0.184398
distances_km                0.019843
comput_speed_knots          0.043022
incident_num               99.932073
"""


df = pd.read_csv('hawaii_data/Hawaii_2020_12.csv')

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. Define your Features (X) and Target (y)
# We select the columns that describe movement
features = ['lat', 'lon', 'speed_over_ground_knots', 'course_over_ground_deg', 'heading_deg']

X = df[features]

# We create a binary target: 1 if it has an incident number, 0 if not
y = df['incident_num'].notnull().astype(int)

# 2. Split the data
# We keep 20% of the data hidden to test the model later
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training on {len(X_train)} rows...")

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# --- Step 1: Initialize the Model ---
# We use 'class_weight="balanced"' because incidents are very rare (0.07%).
# This forces the model to treat missing an incident as a serious error.
rf_model = RandomForestClassifier(
    n_estimators=100,         # Create 100 decision trees
    class_weight='balanced',  # Crucial for your imbalanced data
    n_jobs=-1,                # Use all CPU cores to speed this up
    random_state=42           # Ensures you get the same results every time
)

# --- Step 2: Train (Fit) the Model ---
print("Training the model... (this might take a moment)")
rf_model.fit(X_train, y_train)
print("Training complete!")

# --- Step 3: Test (Predict) ---
# We ask the model to predict incidents on the data it has never seen (X_test)
y_pred = rf_model.predict(X_test)

# --- Step 4: Grade the Results ---
print("\n--- Model Evaluation ---")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

pass