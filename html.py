import csv

import pandas


def convertToHtml(result, title):
    # 将数据转换为html的table
    # result是list[list1,list2]这样的结构
    # title是list结构；和result一一对应。titleList[0]对应resultList[0]这样的一条数据对应html表格中的一列
    d = {}
    index = 0
    for t in title:
        d[t] = result[index]
        index = index + 1
    print(d)
    df = pandas.DataFrame(d)
    print(df)
    df = df[title]
    print(df)
    haa = df.to_html(index=False)

    return haa


def str_to_list(text):
    text = text.strip('[').strip(']').replace('\'', '').strip()
    # print(text)
    text_list = text.split(',')
    # for i in range(0, len(text_list)-1):
    #     text_list[i] = text_list[i].strip('\'')
    # print(text_list)

    # for text_item in text_list:
    #     text_item = text_item.strip('\'')
    # print(text_list)

    return text_list


if __name__ == '__main__':
    with open('school_number.csv') as fp:
        reader = csv.reader(fp)

        city = []
        number = []
        centers = []

        for line in reader:
            # print(line)
            city.append(line[1])
            number.append(line[2])

            center_list = str_to_list(line[3])

            centers.append(center_list)

        fp.close()

        print(city)
        print(number)
        print(centers)

        # centers_dict = {'centers': centers}
        # ccc = pandas.DataFrame(centers_dict)
        # print(ccc)

        # content = {'city': city, 'number': number, 'centers': ccc}
        #
        # aaa = pandas.DataFrame(content)
        # print(aaa)
        # bbb = aaa.to_html(index=False)

        with open('aaa.html', 'w') as fc:
            fc.write(bbb)
            fc.close()

    # result = [[u'2016-08-25',u'2016-08-26',u'2016-08-27'],[u'张三',u'李四',u'王二']]
    # title = [u'日期',u'姓名']
    # # print(convertToHtml(result, title))
    #
    # with open('aaa.html', 'w') as fp:
    #     fp.write(convertToHtml(result, title))
    #     fp.close()
