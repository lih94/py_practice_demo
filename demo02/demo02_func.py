"""
说明：
1.当位置数据的时间一致，但位置不一致，以时间最新的位置为准
2.data.txt记录存在位置变更的号码及相关的位置数据信息；
  export_source_data.txt记录所有号码的位置信息（规整后的），因为可能存在同一时间不同位置的数据被规整，因此条数可能会略少；
  phone_number.txt记录所有存在位置变更的号码
3.路径说明：
 input_data_file_name = 'data/data.txt'：原始数据存放路径
 export_data_file_name = 'export/data.txt'：输出data.txt文件路径
 export_source_data_file_name = 'export/export_source_data.txt'：输出export_source_data.txt文件路径
 phone_number_file_name = 'export/phone_number.txt'：输出phone_number.txt文件路径
"""
import datetime


def get_number(input_data_list):
    """
    获取原始数据中的手机号码
    :param input_data_list:原始数据
    :return: 返回手机号码列表
    """
    number_list = []
    for i in range(len(input_data_list)):
        number_list.append(input_data_list[i].strip().split(' ')[0])
    return set(number_list)


def list_to_dict(input_data_list, number_list):
    """
    将原始数据按照手机号码进行规整
    :param input_data_list: 原始数据
    :param number_list: 手机号码列表
    :return: 返回规整后的列表，列表以字典组成，每个字典包含每个手机号的所有位置、时间记录
    """
    new_list = []
    for number in number_list:
        my_dict = {}
        for i in range(len(input_data_list)):
            number_from_list = input_data_list[i].strip().split(' ')[0]
            if number == number_from_list:
                if "手机号码" not in my_dict:
                    my_dict['手机号码'] = number_from_list
                data_time_from_list = input_data_list[i].strip().split(' ')[1] + ' ' + input_data_list[i].strip().split(' ')[2]
                data_time = datetime.datetime.strptime(data_time_from_list, "%Y-%m-%d %H:%M:%S")
                my_dict[data_time] = input_data_list[i].strip().split(' ')[3]
        new_list.append(my_dict)
    return new_list


def get_result(data_dict):
    """
    将列表中的字典提取出来，并按时间进行排序
    :param data_dict: 从列表提取的字典
    :return: 返回排序完成后的列表
    """
    time_from_data_dict = []
    for key in data_dict.keys():
        if key == '手机号码':
            continue
        else:
            time_from_data_dict.append(key)
    time_from_data_dict = sorted(time_from_data_dict)
    result_data = []
    for time in time_from_data_dict:
        for key, value in data_dict.items():
            if time == key:
                result_data.append(time.strftime("%Y-%m-%d %H:%M:%S") + '：' + value)
    return result_data


input_data_file_name = 'data/data.txt'
export_data_file_name = 'export/data.txt'
export_source_data_file_name = 'export/export_source_data.txt'
phone_number_file_name = 'export/phone_number.txt'
export_data = open(export_data_file_name, 'w+', encoding='utf-8')
phone_number = open(phone_number_file_name, 'w+', encoding='utf-8')
export_source_data = open(export_source_data_file_name, 'w+', encoding='utf-8')
with open(input_data_file_name, 'r', encoding='utf-8') as input_data_file:
    input_data = input_data_file.readlines()

my_number = get_number(input_data)
my_data = list_to_dict(input_data, get_number(input_data))
export_data.write('共有{}个手机号码，出现过位置变更的号码结果如下：'.format(len(my_number)) + '\n')
export_data.write('==========================================================' + '\n')
count = 1
phone_number.write('出现位置变更的手机号如下：' + '\n')
for number1 in my_number:
    count_data = 1
    count_data_hit = 1
    export_source_data.write('手机号码:' + number1 + '，有效位置数据如下：\n')
    for i in range(len(my_data)):
        for value1 in my_data[i].values():
            if number1.strip() == value1.strip():
                my_result = get_result(my_data[i])
                for my_result_tmp in my_result:
                    export_source_data.write(str(count_data) + '.' + my_result_tmp.strip() + '\n')
                    count_data += 1
                if len(my_result) >= 2:
                    export_data.write('手机号码：' + number1 + ':\n')
                    phone_number.write(str(count) + '.' + number1 + '\n')
                    count += 1
                    export_data.write('此号码有效位置数据共{}个，忽略相邻时间之间位置一致的位置数据，结果如下：'.format(str(len(my_result))) + '\n')
                    for t in range(len(my_result)):
                        if t < len(my_result) - 2:
                            if my_result[t].split('：')[1] != my_result[t+1].split('：')[1]:
                                export_data.write(str(count_data_hit) + '.' + my_result[t] + '\n')
                                count_data_hit += 1
                        elif t == len(my_result) - 2:
                            if my_result[t].split('：')[1] != my_result[t+1].split('：')[1]:
                                export_data.write(str(count_data_hit) + '.' + my_result[t] + '\n')
                                count_data_hit += 1
                                export_data.write(str(count_data_hit) + '.' + my_result[t+1] + '\n')
                                count_data_hit += 1
                                break
                            else:
                                export_data.write(str(count_data_hit) + '.' + my_result[t+1] + '\n')
                                count_data_hit += 1
                                break


export_data.close()
export_source_data.close()
phone_number.close()
