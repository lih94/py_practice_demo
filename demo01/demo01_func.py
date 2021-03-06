from mimesis import Address
from mimesis import Business
from mimesis import Datetime
from mimesis import Person


def init_message(*args):
    """
    初始化数据字典
    :param args: 需要生成的字段名称，目前支持生成person_name,person_address,person_business,person_datetime,根据需要选择即可
    :return: 返回数据字典
    """
    init_person = Person('zh')
    init_address = Address('zh')
    init_business = Business('zh')
    init_datetime = Datetime('zh')
    person_name = init_person.full_name(reverse=True)
    person_address = init_address.province() + init_address.city() + init_address.street_name() + init_address.\
        street_suffix() + init_address.street_number() + '号'
    person_business = init_business.company() + init_business.copyright()
    person_datetime = init_datetime.formatted_datetime(start=2018, end=2018)
    person = {}
    for person_key in args[0]:
        if person_key == 'person_name':
            person['person_name'] = person_name
        elif person_key == 'person_address':
            person['person_address'] = person_address
        elif person_key == 'person_business':
            person['person_business'] = person_business
        elif person_key == 'person_datetime':
            person['person_datetime'] = person_datetime
        else:
            print('error input!')
    return person


def create_list(len_list, *args):
    """
    生成数据列表
    :param len_list:需要生成的数据条数
    :param args: 需要生成的数据字段名称，同init_message函数的args
    :return:返回数据列表
    """
    count_list = 0
    data_list = []
    need_mesaage = args
    while count_list < len_list:
        data_list.append(init_message(need_mesaage))
        count_list += 1
    return data_list


def export_to_txt(filename, data):
    """
    将数据列表输出至txt文件
    :param filename: txt文件路径及名称
    :param data: 数据列表名称
    :return: 返回将原列表中字典转换为列表后的新数据列表
    """
    file = open(filename, 'w+', encoding='utf-8')
    init_data = []
    # 将数据字典转换为列表
    for data_tmp in data:
        dist_to_list = []
        for dist_from_data in data_tmp.values():
            dist_to_list.append(dist_from_data.replace(',', ''))
            # 将字典中的逗号替换为空值
        init_data.append(dist_to_list)
    # 将数据列表输出至txt文件
    for i in range(len(init_data)):
        s = str(init_data[i]).replace('[', '').replace(']', '')
        s = s.replace("'", '') + '\n'
        file.write(s)
    file.close()
    return init_data


my_message = create_list(5, 'person_name', 'person_business', 'person_address')
export_to_txt('F:/python培训/code/github/py_practice_demo/demo01/export/test.txt', my_message)
