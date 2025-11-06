# 과제 25
b = input().split()
x = input().split()
i = dict(zip(b,x))
i.pop('alpha')
i.pop('delta')

print (i)

# 과제 26
park = {'korean':94, 'english':91, 'mathematics':89, 'science': 83}
print (park['english'])
print (park['science'])

# 과제 27
kim = {'korean':94, 'english':91, 'mathematics':89, 'science': 83}

kim.update(korean=100, english=100, mathematics=100, science=100)

print (kim)

# 과제 28
lee = {'korean':94, 'english':91, 'mathematics':89, 'science': 83}

print ('english' in lee)

x = lee.pop('english')
print (lee)

# 과제 29
lim = {'korean':94, 'english':91, 'mathematics':89, 'science': 83}

for i, j in lim.items():
  print (i,j)

# 과제 30
choi = {'korean':94, 'english':91, 'mathematics':89, 'science': 83}

choi = {key for key, value in choi.items() if value > 90}
print (choi)

# 과제 31
yoo = {'korean':94, 'english':91, 'mathematics':89, 'science': 83}

b = yoo['korean']+yoo['english']+yoo['mathematics']+yoo['science']
x = b/4
print (x)