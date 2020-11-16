def prima(bilangan):
  

  for i in range (2,bilangan):
      if bilangan % i == 0:
          print(bilangan,' bukan prima')
          break
  else:
      print(bilangan,' adalah prima')
bilangan = int(input('masukan bilangan '))  
prima(bilangan)