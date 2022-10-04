py = [11,14,16,17,19]

out = [i for i in range(11,max(py)+1) if i not in py]

print(out)



x = list(set(range(11,max(py)+1)) - set(py))
print(x)