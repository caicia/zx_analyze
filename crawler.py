#爬取函数

import zlib
import requests
import os

def get_content(url):
    bulletold = requests.get(url).content  # 二进制内容
    return zipdecode(bulletold)

def zipdecode(bulletold):
    decode = zlib.decompress(bytearray(bulletold)).decode('utf-8')
    return decode

def one_step(short, long, count):

    for x in range(1, 11):
        # x是从1到11，11怎么来的，这一集总共46分钟，爱奇艺每5分钟会加载新的弹幕,46除以5向上取整
        # https://cmts.iqiyi.com/bullet/54/00/7973227714515400_60_19_87ad0a0d.br
        try:
            url = 'https://cmts.iqiyi.com/bullet/'+short+'/00/'+long+'_300_' + str(x) + '.z'
            xml = get_content(url)
            # 把编码好的文件分别写入个xml文件中（类似于txt文件），方便后边取数据
            if not os.path.exists('./lyc/zx/'):
                os.mkdir('./lyc/zx/')
            with open('./lyc/zx/' + str(count) + '_' + str(x) + '.xml', 'a+', encoding='utf-8') as f:
                f.write(xml)
        except zlib.error:
            break
        else:
            pass

if __name__=='__main__':
    step_short = [
        '54', '57', '37', '77', '46', '48',
        '98', '94', '47', '46', '08', '59',
        '43', '38', '93', '29', '71', '39',
        '31', '58', '83', '21', '80', '37',
        '32', '11', '48', '08', '06', '37',
        '14', '14', '69', '02', '73', '46',
    ]

    step_long = [
        '7973227714515400', '4779805474835700', '1016845483273700', '8679935826337700', '7197533339804600', '8042213977424800',
        '2262609044749800', '1699488619659400', '1805374511564700', '1933721047194600', '7232026471250800', '8982352350925900',
        '4702797553454300', '2151107991923800', '8357465155589300', '2071693573022900', '4646645944127100', '1182091647913900',
        '7711721648193100', '2099769377685800', '3042314248738300', '2889100571832100', '3374410909698000', '4335405595243700',
        '5215381530163200', '2379725258541100', '4872856713204800', '1488519001760800', '1118720545970600', '2127043016523700',
        '6799659079391400', '5792940940511400', '5095858818866900', '6806076406160200', '1601624386277300', '5310839266044600',
    ]

    for index, item in enumerate(zip(step_short, step_long)):
        one_step(item[0], item[1], index+1)
        print(str(index+1)+'已经爬取完成')

