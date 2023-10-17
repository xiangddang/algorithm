# QUESTION:
# You are a travel enthusiast planning a road trip to visit multiple cities. 
# There are k cities in the region you want to explore. During each day, you can either stay in the city 
# you are currently in and explore its attractions, or you can choose to move to another city. 
# You are planning to travel for T days. You have access to a weather forecast for these days, and you also have 
# information about the cities you plan to visit, allowing you to predict your enjoyment and travel costs.
# On day number t, you can do one of the following:
# Stay in city i and enjoy attractions, gaining a satisfaction score of Sti.
# Move from city i to city j and incur a travel cost of Ctij (which depends on the weather and road conditions).
# Note that Sti and Ctij are provided in the input for all t, i, and j.
#Note also that the cost of traveling depends on the day (e.g., fuel costs and road conditions may vary based on the weather forecast).
# Your goal is to create a travel plan that maximizes your “overall enjoyment” during the trip, 
# where overall enjoyment is sum of the satisfaction scores you gain minus the costs paid during the travel. 
# Your plan should be of the form:
# 1. Day 1: Stay in city 5 and explore. 
# 2. Day 2: Stay in city 5 and explore. 
# 3. Day 3: Move from city 5 to city 1. 
# 4. Day 4: Stay in city 1, and so on.
# You can start your journey in any city on day 1 and finish in any city on day T, as it does 
# not affect your overall enjoyment. Design an algorithm that can find the optimal travel plan in O(k2T) time. 
# (Note that returning just the final overall enjoyment is not enough, and you have to return the plan as well.)

def travelEnthusiast(T, k, S, C):

    # Initilize a 2D array, the first attribute means the day, the second one means the city in the particular day
    enjoyment = [[0 for _ in range(k)] for _ in range(T)]
    # The travel_plan array to store the city stay in the yesterday if we want get the highest enjoyment in one day.
    travel_plan = [[0 for _ in range(k)] for _ in range(T)]
    for i in range(k):
        # Assume the 0th day and the first day stay in the same city, in other words, start in each day and explore the city
        enjoyment[0][i] = S[0][i]
        travel_plan[0][i] = i
    
    for t in range(1, T):
        for i in range(k):
            enjoyment[t][i] = enjoyment[t-1][i] + S[t][i]
            travel_plan[t][i] = i
            for j in range(k):
                if j != i:
                    ans = enjoyment[t-1][j] - C[t][j][i]
                    if ans > enjoyment[t][i]:
                        enjoyment[t][i] = ans
                        travel_plan[t][i] = j
    print(enjoyment)
    print(travel_plan)
    # Get the max enjoyment value
    max_enjoyment = max(enjoyment[T-1])
    # Get the travel plan
    plan = []
    city = enjoyment[T-1].index(max_enjoyment)
    plan.append(city)
    for t in range(T-1, 0, -1):
        city = travel_plan[t][city]
        plan.append(city)

    plan.reverse()
    plan_string = ""
    for t in range(T):
        if plan[t] == plan[t-1]:
            plan_string += f"{t + 1}. Day {t + 1}: Stay in City {plan[t] + 1} and explore."
        else:
            plan_string += f"{t + 1}. Day {t + 1}: Move from city {plan[t-1] + 1} to city {plan[t] + 1}."
        if t != T - 1:
            plan_string += "\n"
    return max_enjoyment, plan_string

T = 5
k = 2
S = [[5, 1], [1, 2], [1, 6], [1, 2], [7, 2]]
C = [
    [[0, 1], [2, 0]],
    [[0, 1], [2, 0]],
    [[0, 2], [2, 0]],
    [[0, 3], [1, 0]],
    [[0, 1], [1, 0]]
]

max_enjoyment, plan = travelEnthusiast(T, k, S, C)

print("Maximum Enjoyment:", max_enjoyment)
print("Travel Plan:")
print(plan)