# -*- coding: utf-8 -*-
#######################################
#
#   user_module.py
#   ユーザ定義関数用のmodule
#
#######################################


class user_module_demo():

    """ 呼び出しテストクラス
    """

    def __init__(self, txt='== user_module_demo =='):
        self.txt = txt
        self.init()

    def init(self):
        self.func_print(self.txt)

    def func_print(self, s):
        # print s
        pass


def user_module_func(txt='== user_module_func =='):
    # print txt
    pass

if __name__ == '__main__':
    user_module_demo()
    user_module_func()
