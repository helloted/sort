
#coding=utf-8

# 在要排序的一组数中，选出最小的一个数与第1个位置的数交换；
# 然后在剩下的数当中再找最小的与第2个位置的数交换，
# 依次类推，直到第n-1个元素和第n个元素（最后一个数）比较为止。




def select_sort(orgin_list):
    length = len(orgin_list)
    # 从list[0]开始遍历，进行外循环，list[i]作为基准位置比较数
    for i in range(length-1):
        mi = i
        for j in range(i,length):
            #找到最小的一个数的位置
            if orgin_list[j] < orgin_list[mi]:
                mi = j
        orgin_list[mi],orgin_list[i] = orgin_list[i],orgin_list[mi]
    return orgin_list



if __name__ == "__main__":
    orgin = [1, 3, 4, 2, 7, 4, 6, 8]
    print select_sort(orgin)
