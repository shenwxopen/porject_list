from pyc8 import Human

class  Myclass_student(Human):
    # sum = 0
    def __init__(self, sch, name, age):
        self.sch = sch
        # Human.__init__(self, name, age)   #调用父类变量,必须传入self  （普通方法调用）
        super(Myclass_student,self).__init__(name, age)
    #     self.__score = 0
    #     self.__class__.sum += 1
    
    def do_homework(self):   #父类出现self必须有参数传入
        print('English homework')
