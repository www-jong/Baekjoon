def get_cart_prd(pools):
  result = [[]]
  for pool in pools:
    result = [x+[y] for x in result for y in pool]
