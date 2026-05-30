#*****************************************************************************#
# Water Jug Problem                                                           #
# The objective of this project is to develop a program that                  #
# can solve the problem of 2 kids fetching 4 gallons of water from a stream,  #
# using only an unmarked 3-gallon bucket, and an unmarked 5-gallon bucket,    #
# in less than 15 steps.                                                      #
#                                                                             #
# This program will take each step of the process of empyting and filling the #
# jugs and will print out the steps taken to reach the target amount of 4     #
# gallons.                                                                    #
#                                                                             #                                      
#*****************************************************************************#

#library used for adding and removing items in a queue
from collections import deque

def water_jugs(jug_a, jug_b, target):
    start = (0, 0) #no water in either jug at the start
    visited = set() #keeps track of visited jug states
    queue = deque([(start, [])]) #state and path/action, initial empty state and empty list

    while queue:
        
        (a,b), path = queue.popleft()#each iteration will pop the oldest state from the queue. a=3 gallon jug, b=5 gallon jug

        #check if we reached the target, then exit if we are done
        if a == target or b == target:
            if a == target:
                final_state = (a, 0) #Emptying other jug to match the exact goal amount
                final_action = "Emptying other jug to match the exact goal amount"
            else:
                final_state = (0, b) #empty the other jug to match the exact goal amount
                final_action = "Emptying other jug to match the exact goal amount"

            return path + [(final_state, final_action)] #return the path to the solution with the final step included
        
        #checks if we have already visited this state, if so we skip it to avoid loops
        if (a,b) in visited:
            continue
        visited.add((a,b))

        #list of possible actions
        actions = []

        #Fill
        actions.append(((jug_a, b),"Fill 3-gallon jug")) #fill jug A
        actions.append(((a, jug_b),"Fill 5-gallon jug")) #fill jug B

        #Empty
        actions.append(((0, b), "Empty 3-gallon jug")) #empty jug A
        actions.append(((a, 0), "Empty 5-gallon jug")) #empty jug B

        #pouring a to b
        #takes the min because we can't pour more than what is in jug A, and we can't pour more than the remaining capacity of jug B.
        pour = min(a, jug_b - b) #amount to pour from A to B
        actions.append(((a - pour, b + pour), "Pour from 3-gallon jug to 5-gallon jug"))

        #pouring b to a
        pour = min(b, jug_a - a) #amount to pour from B to A    
        actions.append(((a + pour, b - pour), "Pour from 5-gallon jug to 3-gallon jug"))

        #add new states to the queue if they haven't been visited
        for state, action in actions:
            if state not in visited:
                queue.append((state, path + [(state, action)]))

    return None #no solution found


# Code Test
solution = water_jugs(3, 5, 4)


#printing the steps, enumerate is used to get the step number starting from 1, and it prints the action taken and the resulting state of the jugs after that action.
for i, (state, action) in enumerate(solution, 1):
    print(f"Step {i}: {action} -> Resulting state: {state}")
