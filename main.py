# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
import copy
import math
if __name__ == '__main__':
    # a=[[1,2,3],[1,4,5],[1,2,7]]
    # b=[i for i in a if sum(i)==10]
    a=[1,2]
    b=[]
    b.append(copy.deepcopy( a ))
    a.pop()
    # for i in range(len(a)):
    #     b.append(a.pop())
    # print_hi(1/2)
    # print_hi(1 // 2)
    # print_hi(math.ceil(1/2))
    # print_hi(math.floor(1 / 2))
    # str="lwq"
    #字符串转换成列表
    # print_hi(len(str))
    # print_hi(list(str))
    # list1=[1,2,3]
    # st="".join(('%s' %id for id in list1))
    # print_hi(st)
    # import collections
    # d = collections.deque("abcdefg")
    # print(d)
    # print(d[0])
    # d.remove('c')
    # print(d)
    # d.extend(range(2))
    # print(d)
    # d.append(2)
    # print(d)
    # d.extendleft('h')
    # print(d)
    # d.appendleft('i')
    # print(d)
    # d.pop()
    # print(d)
    # d.popleft()
    # print(d)
    str="abc"
    b=[]
    b.append(str)
    print(str[1:3])



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
