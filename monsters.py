# Monsters game 

#read in world map containing cities
print 'Loading Map...'
with open('map.txt') as f:
  
     import time
     #time.sleep(1)
     print 'Loading Cities...'
     for line in f:     
        # load line into city, N, S, E and W
        num = len(line.split()) 
        if (num == 5):
            city, P1, P2, P3, P4 = line.split()
           # print city
        elif (num == 4):
        # Store Border City
        #city, N
            city, P1, P2, P3 = line.split()
            #print 'Border City', city
        else: 
            city, P1, P2 = line.split()
            print 'corner city'
#for n range 10000:

#create monsters
     user_input = raw_input("Generate How many monsters?")
     print 'You have generated', user_input, 'Monsters.'
    
# Assign monsts starting location randomly
     import random
     for N in Xrange(user_input): 
         print ' Placing monster in home'
    
