def parse_bsp (s, start=0, stop=128):
  if stop-start <= 2:
    #print('terms', s[0], start, stop)
    if s[0] in ('F','L'):
      #print("F/L", start,s[1:])
      return start, s[1:]
    elif s[0] in ('B','R'):
      #print("B/r", stop-1, s[1:])
      return stop - 1, s[1:]

  midpoint = (stop - start)/2
  #print(midpoint)
  if s[0] in ('F','L'):
    #print(s[0], s[1:], start, stop - midpoint)
    return parse_bsp(s[1:], start=start, stop=stop - midpoint)
  elif s[0] in ('B','R'):
    #print(s[0], s[1:], start + midpoint, stop)
    return parse_bsp(s[1:], start=start + midpoint, stop=stop)
  
  
with open(boarding_passes) as file:
  for line in file:
    pass
