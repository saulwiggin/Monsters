# Monsters game 

print 'Loading Map...'
with open('map.txt') as f:
  
     print 'Loading Cities...'
     citylist = []
     for line in f:     
         #print 'load data into city, N, S, E and W'
         num = len(line.split()) 
         if (num == 5):
             P0, P1, P2, P3, P4 = line.split()
             citylist.append([P0,P1, P2, P3, P4])
         elif (num == 4):
            P0, P1, P2, P3 = line.split()
            citylist.append([P0,P1, P2, P3])
            #print 'Border City'
         else: 
            P0, P1, P2 = line.split()
            citylist.append([P0,P1, P2])
           #print 'corner city#
            #print citylist
     print 
# print 'create monsters'
     #user_input = raw_input("Generate How many monsters?")
user_input = 5
print 'You have generated', user_input, 'Monsters.'
    
# Assign monsters starting location randomly
import random
monster_city = []
for N in xrange(user_input):
    #print 'Placing monsters',`
    monster_city = random.choice(citylist)
    monster_city.append([monster_city])
    print 'Monster', N, ' spawned to', monster_city[0]
    #monster_city = N, 'in city', monster_starting_city
    
print ' Moving monsters'
for Nr in range (10,000):
    move = random.choice(['north', 'south', 'east', 'west'])
    print 'Monster move', move
    #print 'city location now', monster_city2

    #print 'new monster position', monster_city[1]
    #for i in xrange(3):
    #   print move
     #   print directionmap[0]
    #print [monster_city for monster_city in citylist[0] if move in monster_city]
    for i in range (4):
        test = monster_city[i].find(move)
        #print test
        if (test == 0):
            if (move == 'north'):
                new_monster_city = monster_city[i].lstrip('north=')
                monster_city.append(new_monster_city)
                print 'The new monster location is', new_monster_city
            if (move == 'south'):
                new_monster_city = monster_city[i].lstrip('south=')
                print 'The new monster location is', new_monster_city
                monster_city.append(new_monster_city)
            if (move == 'east'):
                new_monster_city = monster_city[i].lstrip('east=')
                print 'The new monster location is', new_monster_city
                monster_city.append(new_monster_city)
            if (move == 'west'):
                new_monster_city = monster_city[i].lstrip('west=')
                print 'The new monster location is', new_monster_city
                monster_city.append(new_monster_city)
        #elif (test == -1):
       #     print 'move blocked'
 #  print 'Monster move to', monster_city
        
    print 'Commense monster battle'
    if (all_same(monster_city) == false):
         print monster_city, 'has been destroyed by monster', N, 'and ',N 
         #del monster_city[i]
         #del city_list.find(monster_city)
         
print 'printing remaining city list to .txt file'


    
