import re
from urllib import request
class Spider():
    url ='http://www.weather.com.cn/'
    url2='http://www.weather.com.cn/weather/101010100.shtml'
    url3='http://www.weather.com.cn/weather/101010300.shtml'
    url4='http://www.weather.com.cn/weather/101010200.shtml'
    url5='http://www.weather.com.cn/weather/101010900.shtml'
    root_pattern ='<li class="on">([\w\W]*?)</ul>'
    root_pattern2='<ul class="t clearfix">([\w\W]*?)</ul>'
    def __fetch_content(self):
        r=request.urlopen(Spider.url)
        htmls=r.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls
    def __fetch_content2(self):
        r = request.urlopen(Spider.url2)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls
    def __fetch_content3(self):
        r = request.urlopen(Spider.url3)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls
    def __fetch_content4(self):
        r = request.urlopen(Spider.url4)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls
    def __fetch_content5(self):
        r = request.urlopen(Spider.url5)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls
    def temprature(self,string1):
        filename='temprature.txt'

        m=0
        string1_pattern = '<span class="ord">([\w\W]*?)<span class="wdTime">'
        root_string1 = re.findall(string1_pattern, string1)
        index_pattern = '<i>([\w\W]*?)</i>'
        city_pattern = '"_blank">([\w\W]*?)</a></span><span class="prov">'
        prov_pattern = '"_blank">([\w\W]*?)</a></span><span class="wd">'
        wd_pattern = '"wd">([\w\W]*?)℃'
        temp_rank = []
        for i in root_string1:  # 将天气温度排行写入文本文件
            a = re.findall(index_pattern, i)
            b = re.findall(city_pattern, i)
            c = re.findall(prov_pattern, i)
            d = re.findall(wd_pattern, i)
            # infor=a[0]+b[0]+c[0]+d[0]
            k = '[\u4E00-\u9FFF]{2,6}'
            e = re.findall(k, c[0])
            infor = a[0] + ' ' + e[0] + ' ' + e[1] + ' ' + d[0]
            # m=re.findall( city_pattern,i)
            temp_rank.append(infor)
            with open(filename, 'w') as file_object:
                for i in temp_rank:
                    file_object.write(i)
                    file_object.write('\n')


    def wencha(self, string2):
        filename = 'wencha.txt'

        m = 0
        string2_pattern = '<span class="ord">([\w\W]*?)</span></li><li>'
        root_string2 = re.findall(string2_pattern, string2)
        index_pattern = '<i>([\w\W]*?)</i>'
        city_pattern = '"_blank">([\w\W]*?)</a></span><span class="prov">'
        prov_pattern = '"_blank">([\w\W]*?)</a></span><span class="wd">'
        wd_pattern = '"wd">([\w\W]*?)℃'
        temp_rank = []
        for i in root_string2:  # 将天气温度排行写入文本文件
            a = re.findall(index_pattern, i)
            b = re.findall(city_pattern, i)
            c = re.findall(prov_pattern, i)
            d = re.findall(wd_pattern, i)
            # infor=a[0]+b[0]+c[0]+d[0]
            k = '[\u4E00-\u9FFF]{2,6}'
            e = re.findall(k, c[0])
            infor = a[0] + ' ' + e[0] + ' ' + e[1] + ' ' + d[0]
            # m=re.findall( city_pattern,i)
            temp_rank.append(infor)
            with open(filename, 'w') as file_object:
                for i in temp_rank:
                    file_object.write(i)
                    file_object.write('\n')


    def rain(self,string3):
        filename = 'rain.txt'

        m = 0
        string3_pattern = '<span class="ord">([\w\W]*?)</span></li><li>'
        root_string3 = re.findall(string3_pattern, string3)
        index_pattern = '<i>([\w\W]*?)</i>'
        city_pattern = '"_blank">([\w\W]*?)</a></span><span class="prov">'
        prov_pattern = '"_blank">([\w\W]*?)</a></span><span class="wd">'
        wd_pattern = '"wd">([\w\W]*?)mm'
        rain_rank = []
        for i in root_string3:  # 将天气温度排行写入文本文件
            a = re.findall(index_pattern, i)
            b = re.findall(city_pattern, i)
            c = re.findall(prov_pattern, i)
            d = re.findall(wd_pattern, i)
            # infor=a[0]+b[0]+c[0]+d[0]
            k = '[\u4E00-\u9FFF]{2,6}'
            e = re.findall(k, c[0])
            infor = a[0] + ' ' + e[0] + ' ' + e[1] + ' ' + d[0]
            # m=re.findall( city_pattern,i)
            rain_rank.append(infor)
            with open(filename, 'w') as file_object:
                for i in rain_rank:
                    file_object.write(i)
                    file_object.write('\n')
        a = 1


    def __analysis(self,htmls):

        root_html=re.findall(Spider.root_pattern,htmls)
        string1=root_html[0]
        string2=root_html[1]
        string3=root_html[2]
        self.temprature(string1)
        self.wencha( string2)
        self.rain(string3)
    def seven_day(self,htmls2):
        filename = 'senvendays.txt'
        root_html = re.findall(Spider.root_pattern2, htmls2)  # 获取未来七天的天气
        future_7days_pattern = '<li class=([\w\W]*?)</li>'
        future_7days = re.findall(future_7days_pattern, root_html[0])
        date_pattern = '<h1>([\w\W]*?)</h1>'
        wea_pattern = '"wea">([\w\W]*?)</p>'
        time_pattern = '<span>([\w\W]*?)</span>'
        temp_pattern = '<i>([\w\W]*?)</i>'
        sevendays_rank = []
        for i in future_7days:
            a = re.findall(date_pattern, i)
            b = re.findall(wea_pattern, i)
            q = re.findall(time_pattern, i)
            c=[]
            c.append('None')
            if len(q)>0:
                c[0]=q[0]

            d = re.findall(temp_pattern, i)
            m = a[0] + ' ' + b[0]  + ' '+c[0] +' '+ d[0]
            sevendays_rank.append(m)
        with open(filename, 'w') as file_object:
            for i in sevendays_rank:
                file_object.write(i)
                file_object.write('\n')

    def seven_day_chaoyang(self, htmls3):
        filename = 'senvendayschaoyang.txt'
        root_html = re.findall(Spider.root_pattern2, htmls3)  # 获取未来七天的天气
        future_7days_pattern = '<li class=([\w\W]*?)</li>'
        future_7days = re.findall(future_7days_pattern, root_html[0])
        date_pattern = '<h1>([\w\W]*?)</h1>'
        wea_pattern = '"wea">([\w\W]*?)</p>'
        time_pattern = '<span>([\w\W]*?)</span>'
        temp_pattern = '<i>([\w\W]*?)</i>'
        sevendays_rank = []
        for i in future_7days:
            a = re.findall(date_pattern, i)
            b = re.findall(wea_pattern, i)
            q = re.findall(time_pattern, i)
            c = []
            c.append('None')
            if len(q) > 0:
                c[0] = q[0]

            d = re.findall(temp_pattern, i)
            m = a[0] + ' ' + b[0] + ' ' + c[0] + ' ' + d[0]
            sevendays_rank.append(m)
        with open(filename, 'w') as file_object:
            for i in sevendays_rank:
                file_object.write(i)
                file_object.write('\n')
    def seven_day_haidian(self, htmls4):
        filename = 'senvendayshaidian.txt'
        root_html = re.findall(Spider.root_pattern2, htmls4)  # 获取未来七天的天气
        future_7days_pattern = '<li class=([\w\W]*?)</li>'
        future_7days = re.findall(future_7days_pattern, root_html[0])
        date_pattern = '<h1>([\w\W]*?)</h1>'
        wea_pattern = '"wea">([\w\W]*?)</p>'
        time_pattern = '<span>([\w\W]*?)</span>'
        temp_pattern = '<i>([\w\W]*?)</i>'
        sevendays_rank = []
        for i in future_7days:
            a = re.findall(date_pattern, i)
            b = re.findall(wea_pattern, i)
            q = re.findall(time_pattern, i)
            c = []
            c.append('None')
            if len(q) > 0:
                c[0] = q[0]

            d = re.findall(temp_pattern, i)
            m = a[0] + ' ' + b[0] + ' ' + c[0] + ' ' + d[0]
            sevendays_rank.append(m)
        with open(filename, 'w') as file_object:
            for i in sevendays_rank:
                file_object.write(i)
                file_object.write('\n')
    def seven_day_fengtai(self, htmls5):
        filename = 'senvendaysfengtai.txt'
        root_html = re.findall(Spider.root_pattern2, htmls5)  # 获取未来七天的天气
        future_7days_pattern = '<li class=([\w\W]*?)</li>'
        future_7days = re.findall(future_7days_pattern, root_html[0])
        date_pattern = '<h1>([\w\W]*?)</h1>'
        wea_pattern = '"wea">([\w\W]*?)</p>'
        time_pattern = '<span>([\w\W]*?)</span>'
        temp_pattern = '<i>([\w\W]*?)</i>'
        sevendays_rank = []
        for i in future_7days:
            a = re.findall(date_pattern, i)
            b = re.findall(wea_pattern, i)
            q = re.findall(time_pattern, i)
            c = []
            c.append('None')
            if len(q) > 0:
                c[0] = q[0]

            d = re.findall(temp_pattern, i)
            m = a[0] + ' ' + b[0] + ' ' + c[0] + ' ' + d[0]
            sevendays_rank.append(m)
        with open(filename, 'w') as file_object:
            for i in sevendays_rank:
                file_object.write(i)
                file_object.write('\n')
    #def three_day_temp(self,htmls2):
    #    three_days_pattern='<script>([\w\W]*?)</script>'
    #    filename = 'threedays.txt'
     #   root_html = re.findall(three_days_pattern, htmls2)
     #   string=root_html[0]
     #   a=1#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


    def __analysis2(self,htmls2,htmls3,htmls4,htmls5):

        self.seven_day(htmls2)
        self.seven_day_chaoyang(htmls3)
        self.seven_day_haidian(htmls4)
        self.seven_day_fengtai(htmls5)
        #self. three_day_temp(htmls2)





    def go(self):
        htmls=self.__fetch_content()
        htmls2=self.__fetch_content2()
        htmls3=self.__fetch_content3()
        htmls4=self.__fetch_content4()
        htmls5=self.__fetch_content5()
        self.__analysis(htmls)
        self.__analysis2(htmls2,htmls3,htmls4,htmls5)



spider= Spider()
spider.go()



