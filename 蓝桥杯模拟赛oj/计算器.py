# def solve(eq,var='x'):
#     eq1 = eq.replace("=","-(")+")"
#     eq1 = eq1.replace("x","*x")
#     eq1 = eq1.replace("+*x","+x")
#     eq1 = eq1.replace("-*x","-x")
#     eq1 = eq1.replace("(*x","(x")
#     if eq1[0] == '*':
#         eq1 = eq1[1:]
#     c = eval(eq1,{var:1j})
#     if c.real!=0:
#         return -c.real/c.imag
#     else:
#         return 0
# test = input()
# ch = 'x'
# for i in range(len(test)):
#     if 97 <= ord(test[i]) <= 122:
#         ch = test[i]
#         test = test.replace(test[i],'x')
#         break
# print("%s=%.3lf"%(ch,solve(test)))

s=input()
for i in s:
    if 97<=ord(i)<122:#取出未知数字母
        x=i
s=s.replace(x,'x')#把未知数字母替换成x
#表达式变形 如-5+2x=-10 -> -5+2*x-(-10)
s=s.replace('=','-(')+')'
s=s.replace('x','*x')
s=s.replace('+*x','+x')
s=s.replace('-*x','+x')
s=s.replace('(*x','(x')
#合并表达式，要用到复数,-5+2*x-(-10) -> (5+2j)
value=eval(s,{'x':1j})
print('%s=%.3f'%(x,-value.real/value.imag))#5+2j=0,j就是未知数