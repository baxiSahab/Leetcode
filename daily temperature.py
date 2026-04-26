def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    n , stack_days = len(temperatures) , [] # index_answer = 0


    for i in range(n):
        new_day = temperatures[i]
        # stack_days.append( new_day ) # we add our day and check if it is higher than the first one

        while stack_days and temperatures[stack_days[-1]] < new_day:# we check new days againt the prev day, if its warmer we pop the prev day and keep poping until we are done. store index to get length
             
            j = stack_days.pop()
            answer[j] = i-j
            # print(stack_days , answer)
        stack_days.append(i)


        # if new_day > stack_days[0]: # if we hit a warmer day we remove the first day from our list,calc days in between and add to answers
        #     answer[index_answer] = len(stack_days)-1
        #     stack_days = stack_days[1:]  # slicing — creates a new list without the first element
        #     i=index_answer # we update this ebfore adding 1 as for loop will add one anyway
        #     index_answer+=1
        #     # stack_days = []
        #     print(f'flag , {len(stack_days)} , {index_answer} , {stack_days}')
    return answer

# --- Test Harness ---
def run_tests():
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60],                  [1, 1, 1, 0]),
        ([30, 60, 90],                      [1, 1, 0]),
        ([90, 80, 70, 60],                  [0, 0, 0, 0]),  # strictly decreasing
        ([50],                              [0]),           # single element
    ]
    for i, (temps, expected) in enumerate(test_cases):
        result = dailyTemperatures(temps)
        status = "✅" if result == expected else "❌"
        print(f"Test {i+1}: {status} | Input: {temps} | Expected: {expected} | Got: {result}")

run_tests() 