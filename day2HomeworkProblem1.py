N, M = map(int, input().split())
L = list(map(int, input().split()))
start = 0
end = max(L)
while start <= end:
  cutter = (start + end) // 2
  cut_sum = 0
  for i in L:
    cut = i - cutter
    if cut < 0:
      continue
    else:
      cut_sum += cut
  if cut_sum >= M:
    answer = cutter
    start = cutter + 1
  else:
    end = cutter - 1
print(answer)