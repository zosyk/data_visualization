from die import Die
from operator import itemgetter
import pygal

# Create two D6 and D10

die_1 = Die()
die_2 = Die(10)

# Make some roles, and store results in a list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result + 1):
    frequencies.append(results.count(value))

# frequencies.sort(key=itemgetter(1), reverse=True)
# print(frequencies)


# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling two D6 50 000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
