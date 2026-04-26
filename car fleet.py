def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    cars = sorted( zip(position , speed) , reverse = True )  # returns 2d list with position speed paired. cars ahead come first
    N , fleet = len(cars) , len(cars)
    # print(cars)
    for i in range(N-1):
        time1 = ( target - cars[i][0] ) / cars[i][1]
        time2 = ( target - cars[i+1][0] ) / cars[i+1][1] # CAR behind in position
        # print(i,cars[i+1] , time2 , time1)
        if time2<=time1: # car behind catches up
            fleet-=1
            # now we have to update speed of car behind as they will both go at slower pace allowing others cars to catch up
            # udpate speed by replace whole tuple at cars[n+1]
            # cars[i+1] = ( cars[i+1][0] , cars[i][1]) # updated the car behind with same position but speed of slower car
            # print('fleet caught up', cars , i)
    return print(fleet)

# Test 1 - Basic
carFleet(12, [10,8,0,5,3], [2,4,1,1,3])  # Expected: 3

# Test 2 - Single car
carFleet(10, [3], [3])  # Expected: 1

# Test 3 - All same speed, different positions
carFleet(10, [4,2,0], [2,2,2])  # Expected: 3

# Test 4 - All merge into one fleet
carFleet(10, [6,8], [3,2])  # Expected: 1 — wait, does the car at 8 catch the one at 6?

# Test 5 - Reverse order positions
carFleet(100, [0,2,4], [4,2,1])  # Expected: 1