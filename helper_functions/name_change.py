import os

directory = "data/2021"#change for each year 
old_format = "usdm_%Y%m%d.json"
new_format = "%Y%m%d.json"

for filename in os.listdir(directory):
    if filename.startswith("usdm_") and filename.endswith(".json"):
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, filename.replace("usdm_", "").replace("-", ""))
        os.rename(old_path, new_path)
        print(f"Renamed {old_path} to {new_path}")