import numpy as np

n = 6
theta = 1/2
poisson_lambda = 3
days = 5000
inventory_a = 30
cost_a = 0
inventory_b = 30
cost_b = 0
max_inventory = 30

class ItemOrder:
    def __init__(self, arrival_time, ordered_units):
        self.arrival_time = arrival_time
        self.ordered_units = ordered_units

ItemOrders_a = []
ItemOrders_b = []
out_of_stock_a = 0
extra_inventory_a = 0
# a) Order each 8 days untill 30 items in inventory
for i in range(days):
    demand_per_day = np.random.binomial(n, theta) # returns int of demand per day
    inventory_a -= demand_per_day
    for j in range(len(ItemOrders_a)):
        ItemOrders_a[j].arrival_time -= 1
        if(ItemOrders_a[j].arrival_time == 0):
            inventory_a += ItemOrders_a[j].ordered_units

    if inventory_a > 0:
        cost_a += (inventory_a * 1)
        extra_inventory_a += inventory_a
    else:
        cost_a += abs(inventory_a * 10)
        out_of_stock_a += inventory_a

    if (i % 8 == 0 and inventory_a < 30):
        arrival_time = np.random.poisson(poisson_lambda, 1) # returns int of arrival time
        ordered_units = 30 - inventory_a
        cost_a += 50
        ItemOrders_a.append(ItemOrder(arrival_time, ordered_units))

print ("Cost a: ", cost_a)
print ("Out of stock: ", abs(out_of_stock_a)) # Total items that where requested but the store wasn't able to provide
print ("Extra inventory: ", extra_inventory_a) # Total of extra inventory
print ("----------------------")
out_of_stock_b = 0
extra_inventory_b = 0
# b) Order each time inventory < 10
for i in range(days):
    demand_per_day = np.random.binomial(n, theta) # returns int of demand per day
    inventory_b -= demand_per_day

    for j in range(len(ItemOrders_b)):
        ItemOrders_b[j].arrival_time -= 1
        if(ItemOrders_b[j].arrival_time == 0):
            inventory_b += ItemOrders_b[j].ordered_units

    if inventory_b > 0:
        cost_b += (inventory_b * 1)
        extra_inventory_b += inventory_b
    else:
        cost_b += abs(inventory_b * 10)
        out_of_stock_b += inventory_b

    if (inventory_b <= 10):
        arrival_time = np.random.poisson(poisson_lambda, 1) # returns int of arrival time
        ordered_units = 30 - inventory_b
        cost_b += 50
        ItemOrders_b.append(ItemOrder(arrival_time, ordered_units))

print ("Cost b: ", cost_b)
print ("Out of stock: ", abs(out_of_stock_b)) # Total items that where requested but the store wasn't able to provide
print ("Extra inventory: ", extra_inventory_b) # Total of extra inventory


#NOTE: Following the first policy is better in terms of costs. With policy b you rarely go out of stock, however, you
# are left with way too much inventory after a day, which adds up in the long run
