#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 12 hour and 24 hour

s = input()
a = s.split(':')   

if (s == '12:00:00AM'):
    print('00:00:00')
    
elif (s == '12:00:00PM'):
    print('12:00:00')

elif (bool(a[0] == '12') & s.endswith('AM')):
    d = a[2].rsplit('AM')
    print(f'00:{a[1]}:{d[0]}')

elif (bool(a[0] == '12') & s.endswith('PM')):
    d = a[2].rsplit('PM')
    print(f'12:{a[1]}:{d[0]}')
    
else:    
    if(s.endswith('PM')):
        for i in range(0,1):
            ai = int(a[i])
        
        ai = ai+12
        b = a[2].rsplit('PM')

        print(f'{ai}:{a[1]}:{b[0]}')
        
    else:
        c = a[2].rsplit('AM')
        print(f'{a[0]}:{a[1]}:{c[0]}')


   


# In[36]:


Range = list(map(int, input().rstrip().split()))

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))
m = 66174 
n = 14084
a = 23751  
b = 92846 
i = []
j = []
count = 0
count1 = 0
for l in range(Range[0], Range[1]+1):
    R.append(l)
    
for k in range(m):
    x = a+apples[k]
    i.append(x)
print(i)
for k in range(n):
    x = b+oranges[k]
    j.append(x)
print(j)

for p in R:
    for q in i:
        if(p == q):
            count = count+1

for r in R:

    for s in j:
        
        if(r == s):
            count1 = count1+1
    
print(count)
print(count1)


# In[45]:


## Apples and Oranges

R = []
Range = list(map(int, input().rstrip().split()))

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))
m = 3 
n = 2
a = 2  
b = 12 
i = []
j = []
count = 0
count1 = 0
for l in range(Range[0], Range[1]+1):
    R.append(l)
print(R)    
for k in range(m):
    x = a+apples[k]
    i.append(x)
print(i)
for k in range(n):
    x = b+oranges[k]
    j.append(x)
print(j)

for p in R:
    for q in i:
        if(p == q):
            count = count+1

for r in R:
    for s in j:
        if(r == s):
            count1 = count1+1
    
print(count)
print(count1)


# In[1]:


## Kangaroos

k1 = 2564+5393
k2 = 5121+2836
v1 = 5393
v2 = 2836
cnt = 0
cnt1 = 0

if(k1 == k2):
    print('YES')
    exit()
    
for i in range(100000):
    k1 = k1+v1
    cnt = cnt+1
    k2 = k2+v2
    cnt1 = cnt1+1 
    
    if(k1 == k2) and (cnt == cnt1) == True:
        break
    
if (k1 == k2) and (cnt == cnt1) == True:
    print('YES')
    quit()
  
else:
    print('NO')


# In[154]:


## Between Two sets

n = 2
m = 2
arr = [3, 4]
brr = [24, 48] 
str1 = []
str2 = []
str3 = []
str4 = []
x = []
R = []

x = (x + [0] * m)

for l in range(arr[n-1], brr[0]+1):
    R.append(l)
    
B = [[(i%j) for j in arr] for i in R]

for i in range(len(R)):
    if(B[i] == [0, 0]):
        str1.append(i)        

for i in str1:
    str2.append(R[i])

C = [[(j%i) for j in brr] for i in str2] 

for i in range(len(C)):
    if(C[i] == x):
        str3.append(i)

for i in str3:
    str4.append(str2[i])
       
print(str4)


# In[155]:


## Score Board, Maria Basketball

n = 10
scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

cnth = 0
cntl = 0
h = scores[0]
l = scores[0]

for i in range(len(scores)):
    if h < scores[i]:
        cnth = cnth+1
        h = scores[i]
        
    elif scores[i] < l:
        cntl = cntl+1
        l = scores[i]
        
    else:
        pass

print(cnth, cntl)


# In[157]:


## Birthday Chocolate

n = int(input().strip())

s = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])

for i in range(m):
    x = s[i] + s[i+1]
    print(x)
        


# In[60]:


x = 6
k = 3

s = [29, 97, 52, 86, 27, 89, 77, 19, 99, 96]
sub = []
subList1 = [s[0:n:n-1] for n in range(2, len(s)+1)]
subList2 = [s[1:n:n-2] for n in range(3, len(s)+1)]
subList3 = [s[2:n:n-3] for n in range(4, len(s)+1)]
subList4 = [s[3:n:n-4] for n in range(5, len(s)+1)]
subList5 = [s[4:n:n-5] for n in range(6, len(s)+1)]

n = 0
cnt = 0
for m in range(0, len(s)+1):
    subList1 = [s[m:n:n-(m+1)] for n in range((m+2), len(s)+1)]
    sub.append(subList1)


for m in range(len(s)):

    for i in sub[m]:
        j = sum(i)
        if (j%k == 0):
            cnt = cnt+1
print(cnt)   


# In[ ]:





# In[111]:


arr_count = 73966

count = []
arr = list(map(int, input().rstrip().split()))

arr = sorted(arr)
for i in arr:
    cnt = arr.count(i)
    count.append(cnt)

x = []   
dic = {}

for i in range(0, arr_count):
    dic.update({arr[i]:count[i]})  
    
import operator
rr = max(dic.items(), key=operator.itemgetter(1))[0]
print(rr) 


# In[7]:


n = 4
grade = []

for _ in range(n):
    scores = int(input())
    grade.append(scores)
print('\n')    
for i in grade:
    if (i<38):
        print(i)
        
    else:
        if (i%5 == 0):
            print(i)
        else:
            if ((i+2)%5 == 0):
                print(i+2)
            elif ((i+1)%5 == 0):
                print(i+1)
            else:
                print(i)


# In[ ]:




