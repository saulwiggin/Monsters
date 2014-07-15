# Monsters game 

#read in world map containing cities
print 'Loading Map...'
with open('map.txt') as f:
  
     import time
     #time.sleep(1)
     print 'Loading Cities...'
     for line in f:     
        # load line into city, N, S, E and W
        num = line.split() 
        if (num == 5):
            city, N, S, E, W = line.split()
        else:
        # Store Border City
        #city, N
            print line
        
#for n range 10000:

#create monsters
     user_input = raw_input("Generate How many monsters?")
     print 'You have generated', user_input, 'Monsters.'
    
    
