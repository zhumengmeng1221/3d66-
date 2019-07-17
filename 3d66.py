import time
import requests
from lxml import etree

class TreeD66spider:
    def __init__(self):
        self.headers={"User-Agent":"Mozilla/5.0"}
        self.url="https://so.3d66.com/res/4s_1_1.html"

    def getImgUrl(self):
        res = requests.get(self.url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        # print(html)
        #构建解析对象
        parseHtml = etree.HTML(html)
        # 图片链接列表
        t_list = parseHtml.xpath("/html/body/div[8]/ul/li/div/div/a/img/@data-src")
        print(t_list)
        for img_link in t_list:
            print(img_link)
            self.writeImg(img_link)

    def writeImg(self,img_link):
        res = requests.get(img_link,headers=self.headers)
        res.encoding="utf-8"
        html= res.content
        filename=img_link[-11:]
        with open(filename,"wb") as f:
            f.write(html)
            time.sleep(2)
            print("%s下载成功" % filename)

    def woreOn(self):
        self.getImgUrl()

if __name__=="__main__":
    treed66 = TreeD66spider()
    treed66.woreOn()