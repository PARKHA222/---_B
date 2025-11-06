# 과제 25
b = input().split()    
x = input().split()    
i = dict(zip(b,x))    
i.pop('alpha')    
i.pop('delta')    

print (i)    

**과제 설명에 따라 표준 입력을 이용해 키와 해당 값들을 각각 입력 받고    
pop으로 'alpha'와 'delta'를 삭제 한 뒤 출력하였습니다.**    

# 과제 26    
park = {'korean':94, 'english':91, 'mathematics':89, 'science': 83}    
print (park['english'])    
print (park['science'])    

**dictionary로 선언 후 english와 science 점수만 출력하였습니다.**    

# 과제 27    
kim = {'korean':94, 'english':91, 'mathematics':89, 'science': 83}    
kim.update(korean=100, english=100, mathematics=100, science=100)    

print (kim)    

**update를 이용해 모든 과목을 100점으로 수정 후 출력하였습니다.**    

# 과제 28    
lee = {'korean':94, 'english':91, 'mathematics':89, 'science': 83}    

print ('english' in lee)    

x = lee.pop('english')    
print (lee)    

**in 연산자를 이용해 dictionary에 english의 key가 있는지 체크하였고    
해당 key-value를 pop으로 삭제한 뒤 출력하였습니다.**    

# 과제 29    
lim = {'korean':94, 'english':91, 'mathematics':89, 'science': 83}    

for i, j in lim.items():    
  print (i,j)    

**반복문으로 dictionary의 key와 value를 모두 출력하였습니다**    

# 과제 30    
choi = {'korean':94,'english':91,'mathematics':89,'science': 83}    

choi = {key for key, value in choi.items() if value > 90}    
print (choi)    

**dictionary comprehension을 이용해 90점 이상인 과목들의 key만 출력하였습니다.**    

# 과제 31    
yoo = {'korean':94, 'english':91, 'mathematics':89, 'science': 83}    

b = yoo['korean']+yoo['english']+yoo['mathematics']+yoo['science']    
x = b/4    
print (x)    

**먼저 각 key의 value를 더해준 뒤 나누어 4과목의 평균을 출력하였습니다.**

**감사합니다**

