import os
import re

def update_toc():
    designs_dir = 'designs'
    if not os.path.exists(designs_dir):
        print("Designs directory not found.")
        return

    # Fetch all .md files and sort them numerically
    files = [f for f in os.listdir(designs_dir) if f.endswith('.md')]
    files.sort()

    toc_lines = ["\n"]
    toc_lines.append("* [LICENSE.md](LICENSE.md)\n")
    toc_lines.append("* [BRAND.md](BRAND.md)\n")
    toc_lines.append("* [PHOEBE_TRUTH.md](PHOEBE_TRUTH.md)\n")
    toc_lines.append("* [GLOSSARY.md](GLOSSARY.md)\n")
    toc_lines.append("* [Designs](#designs)\n")

    for filename in files:
        # Create a clean display name (e.g., "01 G-Bike Utility")
        display_name = filename.replace('.md', '').replace('_', ' ')
        toc_lines.append(f"    * [{display_name}]({designs_dir}/{filename})\n")
    
    toc_lines.append("")
    toc_string = "".join(toc_lines)

    with open('README.md', 'r') as f:
        readme_content = f.read()

    # Regex to swap the content between the markers
    new_readme = re.sub(r'.*?', toc_string, readme_content, flags=re.DOTALL)

    with open('README.md', 'w') as f:
        f.write(new_readme)
    print("README.md Table of Contents updated.")

if __name__ == "__main__":
    update_toc()
