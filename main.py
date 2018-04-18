flag = 0


def sol(dic, letter):
    for x in dic:
        flag = True
        for i in range(5):
            if (x[i] not in letter[i]):
                flag = False
        if flag:
            print(x)


dic = {"about", "after", "again", "below", "could",
       "every", "first", "found", "great", "house",
       "large", "learn", "never", "other", "place",
       "plant", "point", "right", "small", "sound",
       "spell", "still", "study", "their", "there",
       "these", "thing", "think", "three", "water",
       "where", "which", "world", "would", "write"}

letter = [set(), set(), set(), set(), set()]

print("Bomb暗号破解程序 Beta 1.0 启动。。。")
print("使用方法：{a,b,c,d,e}+字母")
print("cabc 表示第三个格字母有abc")
print("暂无修改功能，如果输入有误需要重新启动")

while (flag == 0):
    order = input()
    letter[ord(order[0]) - ord('a')].update(order[1:])
    print(letter)
    sol(dic, letter)
