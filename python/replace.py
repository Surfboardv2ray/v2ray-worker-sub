import re

with open('sub', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith('://'):
        line = 'vmess' + line
    line = re.sub(r'\bauto://\b', 'vmess://', line)
    line = re.sub(r'\bnone://\b', 'vmess://', line)
    new_lines.append(line)

with open('sub', 'w') as f:
    f.writelines(new_lines)
