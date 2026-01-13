names = ["Femboy", "Rei", "Rayen"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]

Femboytotal_steps = sum(steps[0])
Reitotal_steps = sum(steps[1])
Rayentotal_steps = sum(steps[2])

Highest_steps = max(Femboytotal_steps, Reitotal_steps, Rayentotal_steps)
Lowest_steps = min(Femboytotal_steps, Reitotal_steps, Rayentotal_steps)
print(max(Femboytotal_steps, Reitotal_steps, Rayentotal_steps))
print(Highest_steps-Lowest_steps)