#第五章 --函数--

# 5.1 函数的定义域调用**
'''
1.函数的定义
def  函数名(参数1 参数2 参数3):
    
    [函数体]

1.括号里面的参数为形式参数，实际调用的时候运用的参数叫做实际参数 形参不需要你去声明 python自动会识别
2.可以使用return语句返回函数代码的执行结果 返回值可以一个或者多个 若没有则默认返回None
3.
4.
5.
'''
# 一个简单示例2
def my_add(x,y):
    '''add function'''
    s = x+y
    return s

#这样子可以显示你的注释
print(my_add.__doc__)   
print(help(my_add))

print(my_add(1,2))
print(my_add("hello","world"))

# 5.2函数参数
'''
位置参数是最常用的一种参数形式
    调用函数时实参和形参的数量必许相同，且位置必须是一致的
'''
def my_add2(x,y):
    '''add function'''
    print("x="+str(x),"y="+str(y))
    s = x+y
    return s
# 5.3变量作用域

# 5.4Lambda表达式**

# 5.5递归函数

# 5.6函数综合应用