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
            city, N, S, E, W = line.split()
            print city
        else:
        # Store Border City
        #city, N
            city, P1, P2, P3 = line.split()
            print 'Border City', city
        
#for n range 10000:

#create monsters
     user_input = raw_input("Generate How many monsters?")
     print 'You have generated', user_input, 'Monsters.'
    
    
