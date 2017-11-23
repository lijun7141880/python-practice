#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 把数据和对数据的操作用一种叫做“对象”的东西包裹起来。这种被成为“面向对象”的编程。
# todo 面向对象编程最主要的两个概念就是：类（class）和对象（object）
# todo 类是一种抽象的类型，而对象是这种类型的实例。

# todo 一个类可以有属于它的函数，这种函数被称为类的“方法”。
# todo 一个类/对象可以有属于它的变量，这种变量被称作“域”。
# todo 域根据所属不同，又分别被称作“类变量”和“实例变量”。
# todo 域和方法被合称为类的属性。

# todo python是一种高度面向对象的语言，它其中的所有东西其实都是对象。所以我们之前也一直在使用着对象。
s = 'how are you' #s被赋值后就是一个字符串类型的对象
l = s.split() #split是字符串的方法，这个方法返回一个list类型的对象，l是一个list类型的对象

# todo 通过dir()方法可以查看一个类/变量的所有属性：
dir(s)
dir(list)

# todo 创建一个类。
# todo 关键字class加上类名用来创建一个类。之后缩进的代码块是这个类的内部。在这里，我们用pass语句，表示一个空的代码块。
class MyClass:
    pass
# todo 类名加圆括号()的形式可以创建一个类的实例，也就是被称作对象的东西。我们把这个对象赋值给变量mc。于是，mc现在就是一个MyClass类的对象。
mc = MyClass()
# todo 这个意思就是说，mc是__main__模块中MyClass来的一个实例（instance），后面的一串十六进制的数字是这个对象的内存地址。
print mc #<__main__.MyClass instance at 0x7fd1c8d01200>

# todo 我们给MyClass类增加了一个类变量name，并把它的值设为'Sam'。然后又增加了一个类方法sayHi：
# todo 调用类变量的方法是“对象.变量名”。mc.name，你可以得到它的值，也可以改变它的值。
# todo 注意到，类方法和我们之前定义的函数区别在于，第一个参数必须为self。而在调用类方法的时候，通过“对象.方法名()”。mc.sayHi()，格式进行调用，而不需要额外提供self这个参数的值。self在类方法中的值，就是你调用的这个对象本身。
class MyClass:
    name = 'Sam'
    def sayHi(self):
        print 'Hello %s' % self.name
mc = MyClass()
print mc.name
mc.name = 'Lily'
mc.sayHi()

# todo 假设我们有一辆汽车，我们知道它的速度(60km/h)，以及A、B两地的距离(100km)。要算出开着这辆车从A地到B地花费的时间。

# todo 面向过程的方法：
speed = 60.0
distance = 100.0
time = distance / speed
print time

# todo 面向对象的方法：
class Car:
    speed = 0
    def drive(self, distance):
        time = distance / self.speed
        print time

car = Car()
car.speed = 60.0
car.drive(100.0)

# todo 假设我们又有了一辆更好的跑车，它的速度是150km/h，然后我们除了想从A到B，还要从B到C（距离200km）。要求分别知道这两种车在这两段路上需要多少时间。
# todo 面向过程的方法：
speed1 = 60.0
distance1 = 100.0
time1 = distance1 / speed1
print time1

distance2 = 200.0
time2 = distance2 / speed1
print time2

speed2 = 150.0
time3 = distance1 / speed2
print time3

time4 = distance2 / speed2
print time4

# todo 面向对象的方法：
class Car:
    speed = 0
    def drive(self, distance):
        time = distance / self.speed
        print time

car1 = Car()
car1.speed = 60.0
car1.drive(100.0)
car1.drive(200.0)

car2 = Car()
car2.speed = 150.0
car2.drive(100.0)
car2.drive(200.0)

# todo 对比两种方法，面向过程把数据和处理数据的计算全部放在一起，当功能复杂之后，就会显得很混乱，且容易产生很多重复的代码。而面向对象，把一类数据和处理这类数据的方法封装在一个类中，让程序的结构更清晰，不同的功能之间相互独立。这样更有利于进行模块化的开发方式。

# todo 仍然是从A地到B地，这次除了有汽车，我们还有了一辆自行车！
# todo 自行车和汽车有着相同的属性：速度（speed）。还有一个相同的方法（drive），来输出行驶/骑行一段距离所花的时间。但这次我们要给汽车增加一个属性：每公里油耗（fuel）。而在汽车行驶一段距离的方法中，除了要输出所花的时间外，还要输出所需的油量。
# todo 面向过程的方法，你可能需要写两个函数，然后把数据作为参数传递进去，在调用的时候要搞清应该使用哪个函数和哪些数据。有了面向对象，你可以把相关的数据和方法封装在一起，并且可以把不同类中的相同功能整合起来。这就需要用到面向对象中的另一个重要概念：继承。

# todo Vehicle类被称为基本类或超类，Car类和Bike类被成为导出类或子类。
class Vehicle:
    def __init__(self, speed): #__init__函数会在类被创建的时候自动调用，用来初始化类。它的参数，要在创建类的时候提供。于是我们通过提供一个数值来初始化speed的值。
        self.speed = speed

    def drive(self, distance):
        print 'need %f hour(s)' % (distance / self.speed)

class Bike(Vehicle): #class定义后面的括号里表示这个类继承于哪个类。Bike(Vehicle)就是说Bike是继承自Vehicle中的子类。Vehicle中的属性和方法，Bike都会有。
    pass

class Car(Vehicle): #Car类中，我们又重新定义了__init__和drive函数，这样会覆盖掉它继承自Vehicle的同名函数。但我们依然可以通过“Vehicle.函数名”来调用它的超类方法。以此来获得它作为Vehicle所具有的功能。
    def __init__(self, speed, fuel): #多了一个fuel属性
        Vehicle.__init__(self, speed) #调用vehicle的初始化方法，对speed初始化
        self.fuel = fuel #对fuel初始化

# todo 注意，因为是通过类名调用方法，而不是像之前一样通过对象来调用，所以这里必须提供self的参数值。在调用超类的方法之后，我们又给Car增加了一个fuel属性，并且在drive中多输出一行信息。
    def drive(self, distance):
        Vehicle.drive(self, distance)
        print 'need %f fuels' % (distance * self.fuel)

b = Bike(15.0)
c = Car(80.0, 0.012)
b.drive(100.0)
c.drive(100.0)