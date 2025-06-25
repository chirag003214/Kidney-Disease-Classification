import shutil
import os

# Create target directory if it doesn't exist
os.makedirs("prediction_model", exist_ok=True)

# Move and rename model
shutil.copy("artifacts/training/model.h5", "prediction_model/model.h5")

print("✅ model.h5 moved to prediction_model/")