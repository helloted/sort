
#coding=utf-8

def shell_sort(orgin_list):
    length = len(orgin_list)
    # 从list[0]开始遍历，进行外循环，list[i]作为基准位置比较数
    for i in range(length-1):
        # 拿有序的数组之后的一个数，往里面插
        for j in range(i+1,0,-1):
            if orgin_list[j] > orgin_list[j-1]:
                break
            orgin_list[j], orgin_list[j-1] = orgin_list[j-1], orgin_list[j]
    return orgin_list


def shellSort(nums):
    # 设定步长
    step = len(nums)/2
    while step > 0:
        for i in range(step, len(nums)):
            # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
            while i >= step and nums[i-step] > nums[i]:
                nums[i], nums[i-step] = nums[i-step], nums[i]
                i -= step
        step = step/2
    return nums

if __name__ == "__main__":
    orgin = [1, 3, 4, 2, 7, 4, 6, 8]
    print shellSort(orgin)
