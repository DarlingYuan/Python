#集合：用{}表示或set(),建立空集合，必须用set()
#无序且每个元素唯一
#集合间操作：并 |、交 &、差 -、补^、
#集合操作符：包含关系;< <= > >=、|=、&=、-=、^=
#集合处理方法;
''' A.add(x)     ---->如果x不在集合A中，将x增加到A
    S.discard(x) ---->移除S中元素x，x不存在也不包错
    S.remove(x)  ---->移除S中元素x，x不存在，产生KeyError异常
    S.clear()    ---->移除S中所有元素
    S.pop()      ---->随意返回并移除S中一个元素，并更新S，若S为空，产生KeyError异常
    S.copy()     ---->返回集合S的一个副本
    len(S)       ---->返回S的元素个数
    x in S       ---->判断x元素是否在集合S中
    x not in S   ---->判断x元素不在集合S中
    set(S)       ---->将其它类型变量x转变为集合类型'''
    
A = {"p","y",123}
B = set("python123")
C = A - B
print(C)
D = A & B
print(D)
E = A | B
print(E)
F = A ^ B
print(F)
G = B - A
print(G)

for item in A:
    print(item, end="\n")
print(A)

try:
    while True:
        print(A.pop(),end="")
except:
    pass
print(A)

print("p" in A)
print(A >= B)

ls = ["p","p","y","y",123]
print(ls)
s = set(ls)
print(s)
lt = list(s)
print(lt)
