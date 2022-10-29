l = []
for i in range(5):
  l.append(float(input()))
maximum = max(l)
minimum = min(l)
for i in range(len(l)):
  if l[i] == maximum:
    l[i] = minimum
  elif l[i] == minimum:
    l[i] = maximum
print(l)