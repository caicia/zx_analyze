#分析主函数

import zlib
import xlwt


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',}



def excel_label():    #写入excel标签
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')

    worksheet.write(0, 0, label='uid')
    worksheet.write(0, 1, label='content')
    worksheet.write(0, 2, label='linkCount')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    excel_label()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
