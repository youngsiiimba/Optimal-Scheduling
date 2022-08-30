def optimal_scheduling(power, target_load):
  power_prod = power.copy()
  power_prod.sort()

  res = []

  def backtrack(cur, pos, target_load):
    if target_load <= 0:
      res.append(cur.copy())
    
    for i in range(pos, len(power_prod)):
      if power_prod[i] < 0:
        continue
      cur.append(power_prod[i])
      backtrack(cur, i+1, target_load - power_prod[i]) 
      cur.pop()
  
  backtrack([], 0, target_load)
  
  def minimum_power(res):
    out_power = float('inf')
    out_comb = []
    for comb in res:
      if sum(comb) < out_power:
        out_comb = comb
      
      out_power = min(sum(comb), out_power) 
      
    return out_power, out_comb
  return minimum_power(res)



def index2name(result, power):
  name = []
  indexes  = []

  [indexes.append(power.index(x)) for x in result]

  for indx in indexes:
    if indx == 0:
      name.append('Solar')
    elif indx == 1:
      name.append('Diesel')
    elif indx == 2:
      name.append('Battery')
    elif indx == 3:
      name.append('Wind')
    else: 
      name.append('Insufficient')
  
  return name
