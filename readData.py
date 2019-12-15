#输入为调用的文件
#输出为需要取匹配的字典
#相当于爬虫数据和可视化之间的接口，然后可以调用该字典取匹配

temCity = dict()
def translateFileToDict(file_path):
    with open(file_path) as file_object:
        lines = file_object.readlines()
        #定义城市温度/湿度等字典

        numbers = []
        letter2 = []
    for line in lines:
        string = line.rstrip()
        letters = str.split(string)
        for letter in letters:
            if letter.isalpha() == True:
                letter2.append(letter)
            else:
                numbers.append(letter)

        # 将列表中的字符串转为数字
    new_numbers = []
    for n in numbers:
        new_numbers.append(float(n))
    numbers = new_numbers
        # 将奇数项元素置为0
    for i in range(len(numbers)):
        if (i % 2 == 0):
            numbers[i] = 0
        # 删除列表中的非零元素
    while 0 in numbers:
        numbers.remove(0)
        # 此处成功获取有用的数字值

        # 同理删除字符串中的偶数项
    for i in range(len(letter2)):
        if (i % 2 != 0):
            letter2[i] = 0

    while 0 in letter2:
        letter2.remove(0)

        # 下面获取需要的字典
    for i in range(len(numbers)):
        a = letter2[i]
        b = numbers[i]
        temCity[a] = b
    return temCity
#返回最后需要的字典
#最后读取该字典，然后得到匹配结果
def readCity(file_path,City):
    a = translateFileToDict(file_path)[City]
    return a