import matplotlib.pyplot as plt

from die import Die


die = Die()

results = []
for _ in range(5000):
    result = die.roll()
    results.append(result)

all_sides = range(1, die.num_sides+1)
frequencies = []
for value in all_sides:
    frequency = results.count(value)
    frequencies.append(frequency)

fig, ax = plt.subplots()
ax.bar(all_sides, frequencies)
ax.set_title('Results of Rolling a D6 Dice Many Times.')
ax.set_xlabel('dice sides')
ax.set_ylabel('times rolled')
plt.show()