# -*- coding: utf-8 -*-

import urllib,re
import xlwt

#打开网页，获取源码
def get_content():
    url = 'http://search.51job.com/list/020000,000000,0000,00,9,99,Python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    a = urllib.urlopen(url) #打开网址
    html = a.read() #读取所有源代码
    html = html.decode('gbk')
    return html
#从源码中获取想要的内容
def get():
    html = get_content()
    reg = re.compile(r'.*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',re.S)
    items = re.findall(reg,html)
    print items
    return items


#创建excel
def excel_write():
    newtable = '51job.xls'
    wb = xlwt.Workbook(encoding='utf-8')#创建Excel
    ws = wb.add_sheet('python1')#创建表格
    headdata = ['招聘职位','公司','地址','薪资','日期']
    for colnum in range(0,5):
        ws.write(0,colnum,headdata[colnum],xlwt.easyxf('font:bold on'))#行，列

    index = 1

    for item in items:
        for i in range(0,5):
            print item[i]
            ws.write(index,i,item[i])
        index +=1
        wb.save(newtable)

if __name__ == "__main__": #判断文件入口
    items = get()#获取职位信息
    excel_write()