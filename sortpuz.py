import random

n=7
ar=list()


for i in range(n):
    number =random.randint(1,100)
    ar.append (number)
print ("Not sorted:")
print (ar)
print ("------------")



def puz(arr):
 
 is_sorted = False
 right_index=n-1
 left_index=0


 while is_sorted==False:
  while right_index!=0:
          min_index=left_index
          for k in range (min_index+1, right_index):
            if arr[k]<arr[min_index]:
               min_index=k
          print(arr[min_index])    
          print("==============")
          if arr[left_index]==arr[min_index]: 
             left_index+=1   
          else:
              pass
          f=0
          for j in range(left_index, right_index):
            left=arr[j]
            right=arr[j+1]
            if left>right:
              is_sorted==False
              temp=arr[j]
              arr[j]=arr[j+1]
              arr[j+1]=temp
              print(arr)
              f+=1
          if f==0:
            is_sorted=True
            print ("Spisok uze otsortirovan")
            break    
          right_index-=1
print (puz(ar))

 
