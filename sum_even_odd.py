def list(my_list):
     
     my_list =[1,2,3,4,5,6,7,8,9,10]
     sum = 0
     sum1= 0
     for i in my_list:
     
       if i%2 ==0:
         sum =sum+i
       else:
         sum1 =sum1+i
     print("sum of even no",sum)    
     print("sum of odd num",sum1)


print(list)
