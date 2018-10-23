import re, reprlib

# \w+匹配非字母数字及下划线,+表示匹配一个或者多个
re_word = re.compile('\w+')


# print(re_word.findall('liu hu ai na_na'))
# ['liu', 'hu', 'ai', 'na_na']

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = re_word.findall(text)

    # 实现切片索引操作，让实例对象为可迭代对象，
    # 若注销__getitem__方法，则变成不可迭代对象
    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    # reprlib.repr这个实用函数用于生成大型数据结构的简略字符串表示形式
    # 使用reprlib.repr 函数生成的字符串最多有 30 个字,待定啊
    def __repr__(self):
        return 'sentence {0}'.format(reprlib.repr(self.text))


s = Sentence('"The time has come," the Walrus said,"now let\'s go to school,only '
             'ten minutes left,come on ,my dear,do you want to be late ? i hope you run quickly,ha_ha "')

print(list(s), len(list(s)))
for i in s:
    print(i)

# s为可迭代对象
