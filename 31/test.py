# a = 'tim'
# b = a
# a += 'e'
# print(b)
# c = ['t', 'i', 'm']
# d = c
# c += ['e']
# print(d)


# def foo(a_int, b_list, c_list):
#     tmp = 1
#     # a_int 操作
#     a_int += tmp
#     # b_list 操作
#     b_list.append(tmp)
#     # c_list 操作
#     # 局部变量
#     c_list = [5]
#     c_list.append(tmp)
#     print(a_int, b_list, c_list)
#
#
# a_int = 5
# b_list = [5]
# c_list = [5]
# foo(a_int, b_list, c_list)
# # foo 函数内输出内容：6 [5, 1] [5, 1]
# print(a_int, b_list, c_list)
# # print 输出内容：5 [5, 1] [5]

# def foo(a, b='commit', *c, **d):
#     print(a, b, c, d)
# foo(1, z='merge', b='clone', x=6, y=7)
# foo(1, 2, 'push', 5, x='pull', y='chekcout')


# def get_word_count(sentence: str) -> int:
#     return len(sentence.split(","))
#
# sentence = 'Hi,,,,,I’m,,,,a,ca t.'
# sum = get_word_count(sentence)
# print(sum)


class Parent(object):
    x = 1


class Child1(Parent):
    def __str__(self):
        return str(self.x * 2)


class Child2(Parent):
    def __str__(self):
        return str(len(self))
    def __len__(self):
        return self.x * 3


c1 = Child1()
c2 = Child2()
print(Parent.x, Child1.x, Child2.x, c1, c2)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x, c1, c2)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x, c1, c2)
