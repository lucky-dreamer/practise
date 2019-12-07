import numpy as np
def main():
    try:
        x=input("是否退出程序？（退出请输入y，否则输入任意值继续：）")
        while x != "y":
            i=eval(input('请按行输入您要计算的第一个矩阵，然后用中括号[]括住，每行之间用逗号隔开。例如:[1,2],[3,4]''\n'))
            b=eval(input('请按上述格式继续输入第二个矩阵''\n'))
            s=np.array(i)
            d=np.array(b)
            print("                                           ")
            print('您输入的矩阵1为:''\n',s)
            print('您输入的矩阵2为:''\n',d)
            print("                                            ")
            g=np.dot(s,d)
            print('经过运算，得出的结果为:''\n',g)
            print("*******************************************************************************")
            x=input("是否退出程序？（退出输入y,不退出输入n:）")
        print("程序已退出")
    except:
        print("""
        
                
                
                
                
                
                
                您的输入格式有误哦
                
                
                
                
                
                
                ^-^我先溜啦^-^
                
                
                
                
                
                
                
                
                
                
                """)
if __name__=='__main__':
    main()