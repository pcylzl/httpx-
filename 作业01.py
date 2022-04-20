import httpx
import os

class crawling(object):#定义类
    def __init__(self):#定义函数，获取浏览器的指纹信息
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }
    def get_url(self):#定义获取url

        url_list = [
            'https://pic.netbian.com/uploads/allimg/220211/004115-1644511275bc26.jpg',
            'https://pic.netbian.com/uploads/allimg/220215/233510-16449393101c46.jpg',
            'https://pic.netbian.com/uploads/allimg/211120/005250-1637340770807b.jpg',
        ]
        return url_list

    def save_image(self,filename,img):#定义保存图片

        with open(filename,'wb') as f:
            f.write(img.content)
        print('图片提取成功')

    def request(self,url):#定义请求url函数

        res = httpx.request('get',url,headers = self.headers)
        if res.status_code == 200:#检查位置码，是否可以访问
            return res

    def run(self):

        url_list = self.get_url()#调用get_url函数，获取图片对应的url地址
        for index,url,in enumerate(url_list):
            file_name = './image/{}.jpg'.format(index)#将获取到的url地址写进列表
            data = self.request(url)#调用request函数
            self.save_image(file_name,data)#调用save_image函数，将获取到的数据参数代进去

if __name__ == '__main__':
#调用类
    c = crawling()
    if os.path.exists("./image") is False:#判断文件是否存在，若不存在就创建
        os.mkdir('./image')
    c.run()#执行类中的run函数