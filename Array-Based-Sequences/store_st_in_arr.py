names = ['Rane', 'Joseph', 'Janet', 'Jonas', 'Helen']

my_fav = names[0:4]
print(names[1], names[2])
print(names[3], names[4])
print(my_fav)

backup = list(names)
print(backup)

counters = [0] * 8
print(counters)
counters[2] += 1
print(counters)

extras = [5, 6, 7]
counters.extend(extras)
print(counters)


array =[2, 3, 5, 7, 11, 13, 17, 19]
primes = array('i', [2, 3, 5, 7, 11, 13, 17, 19])
print(primes)