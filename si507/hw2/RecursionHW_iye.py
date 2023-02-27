from math import *

def change(amount, coins, coinSelect=[], coinRecord=[]):
  '''determines the minimum number of coins needed for change

  given the change amount, available coin choises, returns the
  minimum number of coins needed

  Parameters
  ----------
  amount: int
      the amount of change
  coins: list
      the available coins choices
  coinSelect: list | default empty list
      each of the coin selected for the change
  coinRecord: list | default empty list
      record of number of coins 

  Returns
  -------
  int
      the minimum amount of coins needed for change
  '''
   
  if amount < 0 or type(amount) != int or amount % min(coins) != 0:
    return inf
  elif amount == 0:
    coinRecord.append(len(coinSelect))
  else:
    coinsSorted = sorted(coins, reverse=True)
    for coin in coinsSorted:
      if amount >= coin:
        change((amount-coin), coins, coinSelect+[coin], coinRecord)
    return min(coinRecord)

def giveChange(amount, coins, coinSelect=[], coinRecord=[], coinGather=[]):
  '''determines the minimum number of coins needed for change
  and the coin choices based on that minimum number

  given the change amount, available coin choises, returns the 
  minimum number of coins needed and coin choices

  Parameters
  ----------        
  amount: int
      the amount of change
  coins: list
      the available coins choices
  coinSelect: list | default empty list
      each of the coin selected for the change
  coinRecord: list | default empty list
      record of number of coins
  coinGather: list | default empty list
      all the possible coin choice combinations 

  Returns
  -------
  list
      consist of two elements: int, list
      int
          the minimum amount of coins needed for change
      list
          the list of coins chosen under minimum number of coins
  '''

  if amount < 0 or type(amount) != int or amount % min(coins) != 0:
    return [inf, []]
  elif amount == 0:
    coinRecord.append(len(coinSelect))
    coinGather.append(coinSelect)
  else:
    coinsSorted = sorted(coins, reverse=True)
    for coin in coinsSorted:
      if amount >= coin:
        giveChange((amount-coin), coins, coinSelect+[coin], coinRecord, coinGather)
    return [min(coinRecord), min(coinGather, key=len)]