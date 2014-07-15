# Monsters game 

print 'Loading Map...'
with open('map.txt') as f:
  
     print 'Loading Cities...'
     citylist = []
     directionmap = []
     for line in f:     
         #print 'load data into city, N, S, E and W'
         num = len(line.split()) 
         if (num == 5):
             P0, P1, P2, P3, P4 = line.split()
             citylist.append([P0])
             directionmap.append([P1, P2, P3, P4])
         elif (num == 4):
            P0, P1, P2, P3 = line.split()
            citylist.append([P0])
            directionmap.append([P1, P2, P3])
            #print 'Border City'
         else: 
            P0, P1, P2 = line.split()
            citylist.append([P0])
            directionmap.append([P1, P2])
           #print 'corner city'

# print 'create monsters'
     #user_input = raw_input("Generate How many monsters?")
user_input = 20
print 'You have generated', user_input, 'Monsters.'
    
# Assign monsters starting location randomly
import random
monster_city = []
for N in xrange(user_input):
    #print 'Placing monsters',
    monster_city = random.choice(citylist)
    monster_city.append([monster_city])
    print 'Monster spawned in', monster_city
    #monster_city = N, 'in city', monster_starting_city
    
#print ' Moving monsters'
    move = random.choice(['North', 'South', 'East', 'West'])
    print 'Move to', move

#print 'Commense monster battle'



    
