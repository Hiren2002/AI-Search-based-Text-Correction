import random
import json

conf_file = "data/conf_matrix.json"
with open(conf_file, 'r') as fp:
    conf_matrix = json.load(fp)

f = open("data/input.txt", "rt")
outF = open("data/synth_text.txt", "wt")
for line in f:
    indices = [i for i in range(len(line)) if line[i] in conf_matrix]
    changeIndices = random.sample(indices, k=max(1, len(line)//20))
    l = list(line)
    for i in changeIndices:
        l[i] = random.choice(conf_matrix[l[i]])
    outF.write(''.join(l))
f.close()
outF.close()