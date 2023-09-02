# 1)swapig numbers
x=7
y=5
x,y
x,y=y,x
x,y

# 2)Area of Rectangle
length=4
breadth=6
Area=length*breadth
Area

#3)Celsius to Fahrenheit,
cel=36.5
far=cel*(9/5)+32
far

#4)string as input and prints
s_str=str(input())
len(s_str)



#5)counts vowels
s_st=str(input())
vw_ct=0
vw_ct = vw_ct+s_st.count('a')
vw_ct = vw_ct+s_st.count('e')
vw_ct = vw_ct+s_st.count('i')
vw_ct = vw_ct+s_st.count('o')
vw_ct = vw_ct+s_st.count('u')
vw_ct = vw_ct+s_st.count('A')
vw_ct = vw_ct+s_st.count('E')
vw_ct = vw_ct+s_st.count('I')
vw_ct = vw_ct+s_st.count('O')
vw_ct = vw_ct+s_st.count('U')
print('Total number of vowels = ',vw_ct)

s_str=str(input())
vowels='aeiouAEIOU'
v=set(vowels)
v_ct=0
for i in v:
    if i in s_str:
        v_ct = v_ct+1
print('Total number of vowels = ',v_ct)


#6)reversed string
s_st=str(input())
s_st[::-1]


#7)palindrome
s_st=str(input())
s_st==s_st[::-1]


#8)modified string without spaces
my_str=str(input())
my_str.replace(' ','')