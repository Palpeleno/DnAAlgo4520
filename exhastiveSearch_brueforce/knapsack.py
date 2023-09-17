import itertools

def knapsack_bruteforce(values, weights,capacity):
    num_items = len(values)
    best_value = 0
    best_combo = None

    # generate all possible solution of cominations of items(power set 2^n)
    for combo in itertools.product([0,1],repeat=num_items):
        print(combo)
        total_weight = sum(combo[i] * weights[i] for i in range(num_items) )
        total_value = sum(combo[i] * values[i] for i in range(num_items) )

        #conditional combo checker if the combo is valid and has a higher value 
        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_combo = combo

    return best_value,best_combo

#driver functions

values = [60,120,130]
weight = [10,30,40]
capacity = 50

best_value, best_combo = knapsack_bruteforce(values, weight, capacity)

print("Best Value :",best_value)
print("Best Combination (0/1) Knapsack) :", best_combo)