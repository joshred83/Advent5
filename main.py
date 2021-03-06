def bsp_parser (s, start=0, stop=128, lower_ch ='F', upper_ch='B'):
  if stop-start <= 2:
    #print('terms', s[0], start, stop)
    if s[0] == lower_ch:
      #print("F/L", start,s[1:])
      return start, s[1:]
    elif s[0] == upper_ch:
      #print("B/r", stop-1, s[1:])
      return stop - 1, s[1:]

  midpoint = (stop - start)//2
  #print(midpoint)
  if s[0] == lower_ch:
    #print(s[0], s[1:], start, stop - midpoint)
    return bsp_parser(s[1:], 
                      start=start, 
                      stop=stop - midpoint, 
                      lower_ch=lower_ch, 
                      upper_ch=upper_ch)
  elif s[0] == upper_ch:
    #print(s[0], s[1:], start + midpoint, stop)
    return bsp_parser(s[1:], 
                      start=start + midpoint, 
                      stop=stop,
                      lower_ch=lower_ch, 
                      upper_ch=upper_ch)


boarding_passes = set()
with open('boarding_passes') as f:
  for line in f:
    row, remainder = bsp_parser(line)
    seat, _ = bsp_parser(remainder, 0, 8, lower_ch='L', upper_ch='R')
    boarding_passes.add((row*8) + seat)


seats = set(range(min(boarding_passes), max(boarding_passes)))
missing = seats - boarding_passes
print(missing)

