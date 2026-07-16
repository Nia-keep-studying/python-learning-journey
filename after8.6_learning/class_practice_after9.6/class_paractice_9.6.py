#9.13 骰子

# ============================================================
# ❌ 原来的写法（已修正）
# ============================================================
# import random
# class Die:
#     def __init__(self, side):
#         self.point = random.randint(1, side)       # 只在创建时算一次
#
#     def shake_die(self):
#         print(f"骰子的点数为{self.point}")          # 只打印，不重新摇
#
# die1 = Die(6)                                      # 原代码漏了参数
# for i in range(1, 11):
#     die1.shake_die()                               # 10次都是同一个数
#
# 问题 1: shake_die() 没重新生成随机数 → 属性永远不变
# 问题 2: sides 没存到 self.sides → shake_die 拿不到面数
# ============================================================

# ============================================================
# ✅ 修正后的写法
# ============================================================
import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides                            # 存下面数，后面摇的时候要用
        self.point = random.randint(1, self.sides)

    def shake_die(self):
        self.point = random.randint(1, self.sides)    # 重新随机，属性就变了
        print(f"骰子的点数为{self.point}")


# die1 = Die(20)
# for i in range(1, 11):
#     die1.shake_die()

#9.14 彩票
# class CaiPiao:
#     def __init__(self,number=[random.randint(1,10)],word=("a","b","c","d","e")):
#         self.number = number
#         self.word = word

#     def ZhongJiang(self,number,word):
#         print(f"本期的中奖号码为{self.number} {self.word}")

# caipiao_number = CaiPiao()
# caipiao_number.ZhongJiang()

"""
完整的彩票代码，我打算再重新写一个更简洁的
import random

numbers_list = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
numbers_list_01 = numbers_list[:]
win_number = []

def choice_win_number(pool):
    for i in range(4):
        picked_number = random.choice(pool)
        pool.remove(picked_number)
        win_number.append(picked_number)
    print(win_number)

#9.15 彩票分析

count = 1
active = True
def choice_my_number(pool):
    global active, count
    while active:
        my_ticket = []
        pool_1 = pool[:]
        for i in range(4):
            picked_number = random.choice(pool_1)
            pool_1.remove(picked_number)
            my_ticket.append(picked_number)
        if sorted(my_ticket,key=str) == sorted(win_number,key=str):
            print(f"你赢了，花费了{count}次,中奖号码为{my_ticket}")
            active = False
        else:
            count += 1
        
choice_win_number(numbers_list_01)
choice_my_number(numbers_list)       # ← 用原始完整池子，别用被抽过的
print(count)
"""

# import random

# list_number = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
# def pick_number(pool:list):
#     picked_number = []
#     pool_demo = pool[:] 
#     for i in range(4):
#         pick_number = random.choice(pool_demo)
#         pool_demo.remove(pick_number)
#         picked_number.append(pick_number)    # ← 追加的是抽到的值，不是列表
#     return picked_number

# win_pick_number = pick_number(list_number)
# print(win_pick_number)

# not_win = True
# my_ticket = pick_number(list_number)
# count = 0
# while sorted(my_ticket,key=str) != sorted(win_pick_number,key=str):
#     my_ticket = pick_number(list_number)
#     count += 1
# print(count)
# print(my_ticket)


# ============================================================
# ✅ 优化版（你的知识范围内，用你学过的工具）
# 优化点：
#  1. 变量名更清晰 — result / drawn 不会搞混
#  2. 删掉没用的 not_win
#  3. 用 while True + break 消除重复调用
#  4. 加 docstring + 注释解释 key=str
#  5. 加 MAX_TRIES 防止死循环
# ============================================================
# import random
#
# TICKET_POOL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
#
#
# def draw_ticket(pool):
#     """从奖池中随机抽取 4 个不重复的号码，返回中奖列表。
#        不修改原始奖池（内部用副本操作）。
#     """
#     result = []
#     pool_copy = pool[:]                  # 副本保护原始数据
#     for _ in range(4):                   # _ 表示"循环变量用不到"
#         drawn = random.choice(pool_copy)
#         pool_copy.remove(drawn)
#         result.append(drawn)
#     return result
#
#
# # ----- 开奖 -----
# winning = draw_ticket(TICKET_POOL)
# print(f"中奖号码：{winning}")
#
# # ----- 买彩票直到中奖 -----
# count = 0
# MAX_TRIES = 100_000                      # 安全阀：10万次没中就停
#
# while True:
#     my_ticket = draw_ticket(TICKET_POOL)
#     count += 1
#     if sorted(my_ticket, key=str) == sorted(winning, key=str):
#         break                             # 中了，退出
#     if count >= MAX_TRIES:
#         print(f"抽了 {MAX_TRIES} 次都没中，放弃。")
#         break
#
# print(f"抽了 {count} 次")
# print(f"你的号码：{my_ticket}")
# # ============================================================

