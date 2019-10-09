import csv


def str_to_list(text):
    text = text.strip('[').strip(']').replace('\'', '').strip()
    # print(text)
    text_list = text.split(',')
    return text_list


def gen_html_table(text_dict):
    header_body = """
    <tr style="text-align: left;">
        <th>city</th>
        <th>number</th>
        <th>centers</th>
    </tr>
    """

    content_body = ""

    for i in range(0, len(text_dict['city'])):
        centers_body = ""

        for j in range(0, len(text_dict['centers'][i])):
            centers_body = centers_body + """
                <td>
                    {}
                </td>
                """.format(text_dict['centers'][i][j])

        content_body = content_body + """
        <tr>
            <td>{}</td>
            <td>{}</td>
            {}
        </tr>
        """.format(text_dict['city'][i], text_dict['number'][i], centers_body)

    table_body = """
    <table border="1" class="dataframe">
        <thead>
            {}
         </thead>
         <tbody>
            {}
         </tbody>
    </table>
    """.format(header_body, content_body)

    return table_body


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

        content = {'city': city, 'number': number, 'centers': centers}
        bbb = gen_html_table(content)
        # aaa = pandas.DataFrame(content)
        # print(aaa)
        # bbb = aaa.to_html(index=False)

        with open('ccc.html', 'w') as fc:
            fc.write(bbb)
            fc.close()
