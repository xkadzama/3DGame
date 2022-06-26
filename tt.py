def loadLand(filename):
   with open(filename) as file:
      y = 0
      for line in file:
         x = 0
         print(line)
         line = line.split(' ')
         print(line)
         for z in line:
            if z == '':
               x += 1
            else:
               for z0 in range(int(z)+1):
                  print(x, y, z0)
                  
            x += 1
         y += 1


loadLand('tg.txt')