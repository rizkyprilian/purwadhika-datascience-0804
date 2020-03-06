import math

initialPopulation = 1000
growthFactor = 1.02
immigrantsPerYear = 50

# using loop
# but this requires series of loop calculation
def calculatePopulationAfterNYear(pop0,growthPercent,immigrants,years):
    growthRatio = growthPercent/100
    lastPopulation = pop0
    for n in range(years):
        lastPopulation += int((growthRatio*lastPopulation) + immigrants)
    return lastPopulation

# the population growth is exponential
# the results is not exactly identical as above function though :(
# there is less than 1% deviation in results
def calculatePopulationAfterNYearV2(pop0,growthPercent,immigrants,years):
    growthRatio = (growthPercent/100) + 1
    return int((math.pow(growthRatio,years)*pop0) + (immigrants*years))

# p0 : initial population
# pn : population to surpass >=
# i've tried to inverse above math function but sadly my math is rusty
# i will update this later
def nbYear(p0,growthPercent,immigrants,pn):
    yearCounter = 0
    lastPopulation = p0

    while(lastPopulation<pn):
        yearCounter += 1
        lastPopulation = calculatePopulationAfterNYearV2(p0, growthPercent, immigrants, yearCounter)
    
    return yearCounter


def nbYear2(p0,growthPercent,immigrants,pn):
    yearCounter = 0
    lastPopulation = p0
    growthRatio = growthPercent/100
    while(lastPopulation<pn):
        yearCounter += 1
        lastPopulation += int((growthRatio*lastPopulation) + immigrants)
    
    return yearCounter

print(calculatePopulationAfterNYear(1000,2,50,5))
print(calculatePopulationAfterNYearV2(1000,2,50,5))
print(nbYear(1000,2,50,1300))
print(nbYear(1500,5,100,5000))
print(nbYear2(1500,5,100,5000))
