a = int(input()) # 216
for i in range(1, a+1):
  sum = 0
  sum += i
  k = str(i)
  for j in k:
    sum += int(j)
  if sum == a:
    print(i)
    break
  elif i == a:
    print(0)
  else:
    continue
