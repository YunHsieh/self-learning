"""
規則:
1、遇到1 則輪流輸出 1, -1
2、遇到0 則直接輸出0
3、遇到連續4個0 輪流輸出 1001, 0001，但1的輸出跟第1條規則相同 -1則輸出-1

target:
11000010000

result:
1, -1, (-1, 0, 0, -1), 1, (0, 0, 0, 1)
"""
li_num = "1100001000010000"

def scrambler(li_num):
    # rule for Scramble
    counter1, converter1 = (1, ['1','-1'])
    counter2, converter2 = (1, ['1001','0001'])
    
    result = []
    li_tmp = []
    for _num in li_num:
        if _num == '1':
            counter1 = (counter1+1) % len(converter1)
            li_tmp.append(int(converter1[counter1]))
            result.extend(li_tmp)
            li_tmp = []
        else:
            li_tmp.append(int(_num))
            if len(li_tmp) == 4:
                counter2 = (counter2+1) % len(converter2)
                li_tmp = [[int(i)*int(int(converter1[counter1])) for i in converter2[counter2]]]
                result.extend(li_tmp)
                li_tmp = []
    result.extend(li_tmp)
    return result
  
print(scrambler(li_num))