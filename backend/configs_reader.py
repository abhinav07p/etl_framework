import yaml
import os

# Path to the config file
config_path = os.path.join(os.path.dirname(__file__), "configs", "db_config.yaml")

# Read the YAML file
with open(config_path, "r") as file:
    config = yaml.safe_load(file)

# Print the whole config
print("Full Config:")
print(config)

# Optional: print sources and target separately
print("\nSources:")
for source in config.get("sources", []):
    print(f"- {source['name']} ({source['type']})")
    for table in source.get("tables", []):
        print(f"  Table: {table['name']}, Joins: {table.get('joins', [])}, Filters: {table.get('filters', [])}")

print("\nTarget:")
target = config.get("target", {})
print(f"{target.get('type')} database at {target.get('host')}, DB Name: {target.get('dbname')}")

print("\nThreading:")
print(f"Max threads: {config.get('threading', {}).get('max_threads', 1)}")
