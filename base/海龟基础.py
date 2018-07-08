#trutle库的使用
'''
    turtle库的使用
    turtle绘窗体布局
    turtle空间坐标体系
    turtle角度坐标体系
    RGB色彩
'''
'''
    1.turtle库的使用
      ⑴turtle（海龟）库是turtle绘图系的Python实现
        Python计算生态 = 标准库 + 第三方库
      ⑵turtle的原理：海龟如画笔，原始为中间，游过留痕迹，大小颜色可控制
    2.turtle绘窗体布局
      ⑴坐标体系同安卓
        turtle.setup(width,height,startx,starty):其中前两个参数定义turtle画布
             的大小；后两个参数定义画布左上角的坐标点，可省略，默认为0.
    3.turtle空间坐标体系
      （1）绝对坐标：以画布为参照点，不随海龟变动
           turtle.goto(x,y)
      （2）海龟坐标：以海龟为参照点，随海龟变动
           turtle.bk(d):后退距离d
           turtle.fd(d):前进距离d
           turtle.circle(r,angle)：
    4.turtle角度坐标体系
      （1）绝对角度：以画布为参照点，不随海龟变动
           绝对角度体系同数学XY角度体系坐标(0/360度，90/-270度，180/-180度，270/-90度)
           turtle.seth(angle):只是改变海龟行进方向
      （2）海龟角度：以海龟为参照点，随海龟变动
           turtle.left(angle):海龟左转angle角度
           turtle.right(angle):海龟右转angle角度
    5.RGB色彩
      其他语言通用匹配模式,分整数模式(0~255)和小数模式(0~1)
      turtle.colormode(mode)
        
      
'''

#PythonDraw.py
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()#海龟悬空在画布上方
turtle.fd(-250)
turtle.pendown()#海龟趴在画布上
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()
