from mongoengine import * 
from django.db import models
# from mongoengine import connect
# connect('NiceJob',host = '127.0.0.1',port=27017)

# 下面使用mysql数据库
class monitor_list(models.Model):
    # 这里限制了长度，所以在输入时不用去验证工作内容是否包含不好的代码。
    job_name = models.CharField(max_length=100)
    def __str__(self):
        return self.job_name
    
class chart_0(Document):
    chart_name = StringField()
    address = StringField()
    location = DictField()
    job = StringField()
    job_url = StringField()
    experience = StringField()
    job_requirements = StringField()
    job_category = StringField()
    company = StringField()
    company_url = StringField()
    area = StringField()
    pay_frist = StringField()
    pay_last = StringField()
    pub_time_frist = StringField()
    pub_time_last = StringField()
    job_status = StringField()
    update_time = StringField()

    meta = {
            'collection':'JobDetail'
    }

class user_info(Document):

    user_id = StringField()
    reply = StringField()
    replay_time = StringField()
    user_name = StringField()

    meta = {
        'collection':'user_info'
    }


if __name__ == '__main__':
    # print(chart.objects)
    count = 0
    chart_names = ['爬虫开发']
    pipeline = [
        {'$match': {'chart_name': '爬虫开发'}}
    ]
    # for i in chart.objects:
    #     # print(i)
    #     count +=1
    # print(count)
    k = chart_0._get_collection().aggregate(pipeline)

    z = []
    for i in k:
        z.append(i)
    print(k)
    print(type(k))
    print(z)
    print(type(z))
    j = chart_0.objects
    print(j)
    print(type(j))

    # for i in k:
    #     print(i)