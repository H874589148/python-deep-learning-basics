import configparser                 #配置文件模块 读写配置文件

from aip import AipImageClassify    #图像识别模块

class BaiDuAPI(object):
    #定义一个类
    def __init__(self,filepath):
        target = configparser.ConfigParser()
        target.read(filepath,encoding='utf-8-sig')
        app_id = target.get('password', 'APP_ID')
        api_key = target.get('password', 'API_KEY')
        secret_key = target.get('password', 'SECRET_KEY')

        self.client = AipImageClassify(app_id,api_key,secret_key)

    #读取图片
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def picture2Name(self,filepath):
        #读取图片
        images = self.get_file_content(filepath)
        alltexts = self.client.plantDetect(images)
        text = alltexts.get('result', '')
        print(text)
        name = []
        for word in alltexts['result']:
            name.append(word['name'])
        text = alltexts.get('result', '')
        return name

if __name__ == '__main__':
    baiduapi = BaiDuAPI('passwd.ini')
    #baiduapi.picture2Name('plant.png')
    print(baiduapi.picture2Name('plant.png'))