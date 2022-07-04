def get_cart_prd(pools):
  result = [[]]
  for pool in pools:
    result = [x+[y] for x in result for y in pool]
  return result

mylists = [['a', 'b'],
    [1, 2, 3],[4,5,6]]
print(get_cart_prd(mylists))