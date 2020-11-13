###########################
# Leetcode 146. LRU缓存机制
###########################
import collections


class LRUCache(object):

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v       # key as the newest one
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:   # self.dic is full
                self.dic.popitem(last = False)
        self.dic[key] = value

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))       # 返回  1
    cache.put(3, 3)    # 该操作会使得关键字 2 作废
    print(cache.get(2))       # 返回 -1 (未找到)
    cache.put(4, 4)    # 该操作会使得关键字 1 作废
    print(cache.get(1))       # 返回 -1 (未找到)
    print(cache.get(3))       # 返回  3
    print(cache.get(4))       # 返回  4

