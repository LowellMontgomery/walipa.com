import os
import re

def plant_seeds():
    master_file = 'MASTER_DESIGNS.md'
    if not os.path.exists(master_file):
        print("No Master Seed file found.")
        return

    with open(master_file, 'r') as f:
        content = f.read()

    # Regex to find [FILENAME.md] and the content following it
    seeds = re.findall(r'### \[(.*?)\]\n(.*?)(?=\n### \[|$)', content, re.DOTALL)

    if not os.path.exists('designs'):
        os.makedirs('designs')

    for filename, body in seeds:
        filepath = os.path.join('designs', filename.strip())
        with open(filepath, 'w') as f:
            f.write(body.strip() + '\n')
        print(f"Planted: {filename}")

    # Remove the master file after processing
    os.remove(master_file)

if __name__ == "__main__":
    plant_seeds()
