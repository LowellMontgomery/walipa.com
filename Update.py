import os
import re

def update_toc():
    designs_dir = 'designs'
    # Ensure designs directory exists
    if not os.path.exists(designs_dir):
        return

    designs = sorted([f for f in os.listdir(designs_dir) if f.endswith('.md')])
    
    toc = "\n"
    toc += "* [LICENSE.md](LICENSE.md)\n"
    toc += "* [BRAND.md](BRAND.md)\n"
    toc += "* [PHOEBE_TRUTH.md](PHOEBE_TRUTH.md)\n"
    toc += "* [GLOSSARY.md](GLOSSARY.md)\n"
    toc += "* [Designs](#designs)\n"
    
    for design in designs:
        # Clean up the name for display
        display_name = design.replace('_', ' ').replace('.md', '')
        # Handle the numbering properly
        if display_name[0:2].isdigit():
            display_name = f"{display_name[0:2]} {display_name[2:].strip()}"
        
        toc += f"    * [{display_name}]({designs_dir}/{design})\n"
    
    toc += ""
    
    with open('README.md', 'r') as f:
        content = f.read()
    
    # Replace the existing TOC block
    new_content = re.sub(r'.*?', toc, content, flags=re.DOTALL)
    
    with open('README.md', 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    update_toc()
