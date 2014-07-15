# Monsters game 
import re
import csv
import random
def all_same(items):
    return all(x == items[0] for x in items)

print 'Loading Map...'
with open('map.txt') as f:
  
     print 'Loading Cities...'
     citylist = []
     for line in f:     
        # print 'load data into city, N, S, E and W'
         num = len(line.split()) 
         if (num == 5):
             P0, P1, P2, P3, P4 = line.split()
             citylist.append([P0,P1, P2, P3, P4])
         elif (num == 4):
            P0, P1, P2, P3 = line.split()
            citylist.append([P0,P1, P2, P3])
          #  print 'Border City'
         else: 
            P0, P1, P2 = line.split()
            citylist.append([P0,P1, P2])
           # print 'corner city'
            #print citylist 
     print 'create monsters'
     user_input = int(raw_input("Generate How many monsters?"))

     print 'You have generated', user_input, 'Monsters.'
     print 'Placing monsters'
# Assign monsters starting location randomly

monster_city = []
for j in range(user_input): 
    monster_city.append(random.choice(citylist))
    #monster_city.append([monster_city])
    print 'Monster', user_input, ' spawned to', monster_city[j]
    #monster_city = N, 'in city', monster_starting_city    
  #  print 'monster', j, 'spawned in ', monster_city[j]
print ' Moving monsters'
for Nr in range (1, 10000):
   # print 'timestep', Nr

    for N in xrange(user_input):
        
        move = random.choice(['north', 'south', 'east', 'west'])
      #  print 'Monster move', move
        #print 'city location now', monster_city2

        #print 'new monster position', monster_city[1]
        #for i in xrange(3):
        #   print move
         #   print directionmap[0]
        #print [monster_city for monster_city in citylist[0] if move in monster_city]
       # for N in range (user_input):
        for i in range (len(monster_city[N])):
            test = monster_city[N][i].find(move)
            #print test
            if (test == 0):
                if (move == 'north'):
                    new_monster_city = monster_city[N][i].lstrip('north=')
                    #monster_city.append(new_monster_city)
                    #print 'The new monster location is', new_monster_city
                if (move == 'south'):
                    new_monster_city = monster_city[N][i].lstrip('south=')
                    #print 'The new monster location is', new_monster_city
                    #monster_city.append(new_monster_city)
                if (move == 'east'):
                    new_monster_city = monster_city[N][i].lstrip('east=')
                    #print 'The new monster location is', new_monster_city
                    #monster_city.append(new_monster_city)
                if (move == 'west'):
                    new_monster_city = monster_city[N][i].lstrip('west=')
                    #print 'The new monster location is', new_monster_city
                    #monster_city[N][i].append(new_monster_city)
                # eval (test == -1):
                # print 'move blocked
                
                #print 'move', N, 'from', monster_city[N][0], 'to', new_monster_city 
        #print 'Monster', N, 'from', monster_city, 'goes', move, 'to', new_monster_city
        
        for i in range (1,len(citylist),5):
            if (citylist[i][0] == new_monster_city):
                print 'monster battle', i
                monster_city[N] = new_monster_city
               # print 'error message, city info not found for ', new_monster_city
   #    print 'Monster move to', monster_city
                
   # print 'Test for monster battle'
    #print monster_city
    for i in range (0, user_input*5-1, 5):
        if (all_same(monster_city[N][0]) == False):
    #    print 'monster battle'
         #    print monster_city, 'has been destroyed by monster', N, 'and ',N 
                 
                 del citylist[i][0:5]
             #del city_list.find(monster_city)
          
print 'printing remaining city list to .txt file'
csvfile = "Final_map.txt"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(citylist)


    
