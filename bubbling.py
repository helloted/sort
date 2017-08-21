#coding=utf-8

def bubbling_sor(orgin_list):
    length = len(orgin_list)
    temp = 0

    # 从list[0]开始遍历，进行外循环，list[i]作为基准位置比较数
    for i in range(length):
        # 用之后的数值与基准位置的数进行比较，进行内循环
        for j in range(i+1,length):
            # 如果基准位置之后的数，比基准位置更小，就进行替换，这样一轮内循环，都能保证基准位置的数比其后面的数值更大
            if orgin_list[i] > orgin_list[j]:
                orgin_list[i],orgin_list[j] = orgin_list[j],orgin_list[i]
    return orgin_list





if __name__ == "__main__":
    orgin = [1, 3, 4, 2, 7, 4, 6, 8]
    print bubbling_sor(orgin)