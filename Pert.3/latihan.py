#pemungutan suara ketua HMIF

daftar_suara = ["enrinal","huda","ivena","enrinal","huda","enrinal","huda","enrinal"]

voting = {"enrinal": 0,"ivena": 0,"huda": 0}

for i in daftar_suara:
	if i == "enrinal":
		voting["enrinal"] += 1
	elif i == "huda":
		voting["huda"] += 1
	else:
		voting["ivena"] += 1

sort = []

for j in voting:
	sort.append(j)

sort.sort()

idx = 0
for i in voting:
	print(sort[idx] + " : "+str(voting[i]))
	idx += 1


# SORTING DICT
print(sorted(voting.items()))
