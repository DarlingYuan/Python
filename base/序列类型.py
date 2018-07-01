#序列类
''' 定义
    处理函数及方法
    元组类型及操作
    列表类型及操作
    应用场景'''
'''
 1.  序列是具有先后关系的一组元素，元素间由序号引导，序号有正向和反向两种
    序列类型：字符串类型、元组类型、列表类型
 2.  序列处理函数及方法
    x in s、x not in s、s+t、s*n或n*s、s[i]、s[i:j]或
    s[i:j:k]切片，返回序列s中第i到j以k为步长的元素子序列
 3.  序列类型通用函数和方法
    len(s)/min(s)/max(s)/
    s.index(x)/s.index(x,i,j):返回序列s从i开始到j位置第一次出现元素x的位置
    s.count(x):序列中出现x的次数
 4.元组类型定义：
   元组是一种序列类型，一旦创建就不能被修改
   使用小括号()或tuple()创建，元素间用逗号,分隔
   可以使用或不使用小括号
 5.列表类型定义：
   使用[]或list()创建，元素间用逗号,分隔
   元素类型可以不同，无长度限制

 6.列表类型操作函数和方法：
   ls[i] = x:替换列表ls第i元素为x
   ls[i:j:k] = lt:用列表lt替换ls切片后所对应元素子列表
   del ls[i]:删除列表ls中第i元素
   del ls[i:j:k]:删除列表ls中第i到第j以k为步长的元素
   ls += lt:更新列表ls,将列表lt元素增加到列表ls中
   ls *= n:更新列表ls，其元素重复n次

   ls.append(x)
   ls.clear()
   ls.copy()
   ls.insert(i,x)
   ls.pop(i)
   ls.remove(x)
   ls.reverse()
    
    
'''

ls = ["python",123,".io"]
print(ls[::-1])
s = "python123.io"
print(s[::-1])

print(len(ls))
print(min(s))
print(s.index("o"))
print(s.count("o"))

creature = "cat","dog","tiger","human"
print(creature)
print(creature[::-1])
color = (0x001100, "blue", creature)
print(color[-1][-2])

ls = ["cat","dog","tiger",1024]
print(ls)
lt = ls
print(lt)

ls[1:2] = [1,2,3,4]
print(ls)

del ls[::3]
print(ls)

ls *= 2
print(ls)
