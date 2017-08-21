#coding=utf-8


def sub_solt(orgin,l,high):
    key = orgin[l]
    while l < high:
        while l < high and orgin[high] >= key:
            high -= 1
        while l < high and orgin[high] < key:
            orgin[l] = orgin[high]
            l += 1
            orgin[high] = orgin[l]
    orgin[l] = key
    return l


def quick_solt(orgin,l,high):
    if l < high:
        # 分治法找到分治点，左边为小于分治数，右边为大于分治数
        key_index = sub_solt(orgin,l,high)
        # 分别进行排序
        quick_solt(orgin,l,key_index)
        quick_solt(orgin,key_index+1,high)


if __name__ == "__main__":
    orgin = [5, 3, 4, 2, 7, 4, 6, 8]
    quick_solt(orgin,0,len(orgin)-1)