import random

weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
classes_per_week = 3
cost_per_class = cost_per_week/classes_per_week
print("Cost per week:", cost_per_week)
print("Cost per class:", cost_per_class)

vars = [weeks, classes, tuition, cost_per_week, classes_per_week, cost_per_class]
for i in vars:
    print(i, type(i))

my_list = ["hi", 5, 1.0, 3.2, "4"]
choice = random.choice(my_list)
print(choice)
