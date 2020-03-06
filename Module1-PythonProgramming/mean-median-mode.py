import math
# mean, median, mode adalah measurement of center

# measurement of spread:
# stdev_pop
# variance
# skewness
# excess kurtosis

# definisi:
# ----------
# mean
# median
# mode

# stdev_pop
# berapa banyak deviasi dari mean (mengetahui persebaran angka)
# math.sqrt(variance)

# variance
# nilai persebaran secara angka
# sum (Xi - mean)**2/N-1 (kalau sample)
# sum (Xi - mean)**2/N (kalau populasi)

# skewness
# (sum (Xi - mean)**3 / N) / stdev**3
# dibagi seluruh populasi

# excess kurtosis
# (sum (Xi - mean)**4 / N) / stdev**4
# dibagi seluruh populasi
# dikurangi 3 biar angka idealnya 0


# mean
# -- or average
# sum of all data divided by population number
mean = lambda data: sum(data) / len(data)

# median


# variance
def variance(data):
    data_ = data.copy()
    mean_ = mean(data_)
    variance = sum(list(map(lambda x: math.pow((x - mean_), 2), data_))) / len(data_)
    return variance

# stdev
stdev = lambda data: math.sqrt(variance(data))

# skewness
def skewness(data):
    data_ = data.copy()
    mean_ = mean(data_)
    stdev_ = stdev(data_)
    skewness = (sum(list(map(lambda  x: math.pow((x - mean_), 3), data_))) / len(data_)) / math.pow(stdev_, 3)
    return skewness

# excess kurtosis
def excessKurtosis(data):
    data_ = data.copy()
    mean_ = mean(data_)
    stdev_ = stdev(data_)
    excessKurtosis = (sum(list(map(lambda x: math.pow(x - mean_, 4)))) / len(data_)) / math.pow(stdev_, 4)
    # -3 itu menandakan excess nya agar normalnya = 0
    excessKurtosis -= 3
    return excessKurtosis

functionLists = {'mean': mean, 'variance': variance, 'skewness': skewness, 'excess kurtosis': excessKurtosis}

# statistic_sample = lambda data,funct : functionLists[funct](data)
def statistic_sample(data,funct):
    return functionLists[funct](data)

list_angka = [1,3,3,3,4,4,2,4,10]

print(statistic_sample(list_angka,'mean'))