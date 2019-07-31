import re
with open("./fichier", "r") as sources:
    lines = sources.readlines()
with open("./output", "w") as sources:
    for line in lines:
        sources.write(re.sub(r'ours', 'canard', line))
