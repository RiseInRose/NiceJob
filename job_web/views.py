
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from job_web.models import monitor_list
from myusers.models import User
import urllib.parse,time,re,pymongo
client = pymongo.MongoClient('localhost', 27017)
NiceJob = client.NiceJob
JobDetail = NiceJob.JobDetail
mission_list = NiceJob.mission_list
user_info = NiceJob.user_info
# now_time0 = time.asctime(time.localtime(time.time()))
# now_time = int(now_time0.split(' ')[4].split(':')[1])%2

from job_web.models import chart_0
# Create your views here.
def get_all_monitor_job():
    pass


def index2(request):
    names = []
    chart_names = ['爬虫开发']
    datas_name_check = ''
    for each in chart_names:
        names.append(each)
        datas_name_check = each
        break
    pipeline0 = [
        {'$match': {'chart_name': chart_names[0]}}

    ]
    count = 0

    for i in JobDetail.find():
        count +=1

    nums = 15
    sums = count
    add_datas_info = '已经有{}种工作监控中，共计{}个职位'.format(nums,sums)
    limit = 100
    pipeline1 = [
        {'$match': {'chart_name': chart_names[0]}}
    ]
    localt = chart_0._get_collection().aggregate(pipeline1)
    k = []
    # localt = chart.objects  # 这个是获取chart表内所有的数据。
    # localt = chart._get_collection().aggregate(pipeline) # 这个是获取chart内，pipleline的数据。
    for each in localt:
        k.append(each)
    paginatior = Paginator(k,limit) # k需要为list
    page = request.GET.get('page',1)
    loaded = paginatior.page(page)
    context = {
        'lat': loaded,
        'datas_name':names,
        'datas_name_check':datas_name_check,
        'add_datas_info': add_datas_info,
        'homepage_check': 'yes'
    }
    # 这里遇到字典在网页中无法正确解析，所以直接在数据结构里面搞定
    return render(request, 'job_web/index.html', context)

def mine(request):
    try:
        a = request.GET['add']
    except:
        a = ''

    # 获取到用户选取的select_chart，然后返回对应数据。
    try:
        select_chart = request.GET['select_chart']
    except:
        select_chart = ''

    # 获取用户删除数据
    try:
        d = request.GET['delete']
    except:
        d = ''
    # -------------基础数据处理-------------------
    job_monitors = User.objects.get(username=request.user.username).job_monitor
    # 这时的job_monitor 是一个str对象，现在还不能直接弄成数组，所以需要先处理下。
    # job_monitor = str_to_list(job_monitor) # 这个放到外层调用函数也没有用？下面直接把函数放里面来了。
    p = r"('.+?')"
    lists = re.findall(p, job_monitors)
    job_monitor = []
    if lists != []:
        for each in lists:
            job_monitor.append(each.split("'")[1])

    # lists是job_monitor 里面值还是转换后的。
    # 显示本用户监控的工作，并显示在百度地图下面。job_monitor直接包含在用户数据中
    lists = []
    for i in job_monitor:
        lists.append(urllib.parse.unquote(str(i)))

    # -------------用户第一次进入mine时默认状态-------------------
    if lists != []:
        datas_name_check = str(lists[0])
    else:
        datas_name_check = ''

    # -------------处理用户添加数据-------------------
    # 检查返回值是否在列表内，如果在，则不添加。
    # 找到当前登录用户，然后在其job_monitor内添加内容即可。
    if a != '':
        check_repeat = False
        a_quote = urllib.parse.quote(a)
        # 如果列表为空，则直接添加
        if job_monitor == []:
            check_repeat = True
        for i in job_monitor:
            # 如果列表内有某个值，则不添加
            if str(i) == str(a_quote):
                check_repeat = False
                break
            # 这里如果添加一个break 则会出问题。break跳出整个循环，continue 跳过本次循环。
            else:
                check_repeat = True

        # 这里限制每个普通用户只能添加3个工作，添加的工作将会加入任务列表。
        if check_repeat == True and len(job_monitor) < 3:
            # 将数据添加到用户信息中
            job_monitor.append(a_quote)
            User.objects.filter(username=request.user.username).update(job_monitor = job_monitor)
            # 将数据添加到任务列表中
            data = {
                'name': str(a)
            }
            mission_lists = mission_list.find()
            check_mission_lists = []
            for i in mission_lists:
                check_mission_lists.append(i['name'])
            if str(a) not in check_mission_lists:
                mission_list.insert(data)

        # # 读取所有用户数据，如果有新的监控添加，则加入监控循环队列
        # monitor_list_all = []
        # if len(job_monitor) < 3:
        #     for each in monitor_list.objects.all():
        #         monitor_list_all.append(each.job_name)
        #     if a_quote not in monitor_list_all:
        #         q = monitor_list(job_name=str(a_quote))
        #         q.save()

# --------处理用户选取的select_chart，然后返回对应数据。---------
    if select_chart != '':
        datas_name_check = str(select_chart)
        # 判断刚添加的任务是否完成，如果完成，mission_list里面会没有值
        j = []
        i = mission_list.find({'name': datas_name_check})
        for each in i:
            j.append(each)
        if str(j) != '[]':
            select_chart_info = '{}的数据更新中，请耐心等待，可以去冲杯茶再来查看数据哦！'.format(str(select_chart))
        else:
            select_chart_info = '{}的数据更新完毕！'.format(str(select_chart))
    else:
        select_chart_info = ''


# ------------------处理用户删除数据----------------------
    if d != '':
        d_quote = urllib.parse.quote(d)
        # 基础数据中，已经获取用户监控数据列表
        # 删除输入的内容
        try:
            job_monitor.remove(d_quote)
            User.objects.filter(username=request.user.username).update(job_monitor=job_monitor)

        except:
            pass
        lists = []
        for i in job_monitor:
            lists.append(urllib.parse.unquote(str(i)))
        delete_datas_info = '{}已从数据库删除'.format(d)
    else:
        delete_datas_info = ''

# ------------------返回信息处理----------------------
    limit = 50
    # 获取用户选择数据库名称，匹配相应数据
    pipeline = [
        {'$match': {'chart_name': datas_name_check}}
    ]
    localt = chart_0._get_collection().aggregate(pipeline)
    k = []
    for each in localt:
        k.append(each)
    paginatior = Paginator(k, limit)  # k需要为list
    page = request.GET.get('page', 1)
    loaded = paginatior.page(page)

    if len(job_monitor) >= 3 and a != '':
        add_datas_worning = '注意：普通用户只能监控3个项目，如需新项目，请先删除原有项目，再添加！'
        add_datas_info = '{}已加入数据库！刷新页面后查看，提取数据大约需要5分钟，请耐心等待'.format(a)
    else:
        add_datas_worning = ''
        add_datas_info = '{}已加入数据库！刷新页面后查看，提取数据大约需要5分钟，请耐心等待'.format(a)
    if a == '':
        add_datas_info = ''

    # content = '工作：{}'.format(loaded.job)
    context = {
        'lat': loaded,
        'datas_name': lists,
        'datas_name_check': datas_name_check,
        'add_datas_worning': add_datas_worning,
        'add_datas_info': add_datas_info,
        'select_chart_info': select_chart_info,
        'delete_datas_info': delete_datas_info,
        # 'content':content
    }
# 这里遇到字典在网页中无法正确解析，所以直接在数据结构里面搞定
    return render(request, 'job_web/index.html', context)

def contact(request):
    return render(request, 'job_web/author.html')

def helps(request):
    return render(request, 'job_web/help.html')

def my_vitae(request):
    return render(request, 'job_web/my_curriculum_vitae.html')

def auto_launch_vitae(request):
    return render(request, 'job_web/auto_launch_vitae.html')

def message_board(request):
    try:
        reply = request.POST['reply']
    except:
        reply = ''
    # ----------------基础数据处理------------------
    user_id = User.objects.get(username=request.user.username).id
    now_time1 = time.asctime(time.localtime(time.time()))

    whos_reply = ''
    # 先不做reply功能
    # ----------------添加reply数据----------------
    if reply != '':
        data = {
            'user_id': user_id,
            'reply': reply,
            'reply_time': now_time1,
            'user_name':request.user.username,
            'other_reply': whos_reply
        }
        user_info.insert(data)

    # -----------------返回数据处理--------------------
    pipeline = [
        {'$match': {'user_id': user_id}}
    ]
    # 后面的 .objects  得到的内容是针对Paginator用。想要得到数据，使用.find()即可。
    # replys = user_info._get_collection().aggregate(pipeline)
    replys = user_info.find()

    context = {
        'data':replys
    }

    return render(request, 'job_web/message_board.html',context)

def ajax_test(request):

    age = request.GET.get('age')
    wpm = request.GET.get('wpm')
    r = int(wpm)+ int(age)
    r = str(r)
    r = 'uiouwoueiowuieouwiouifoduaifopuaidopfuaiopdfuiaospfuaiopdfuiaopfuaiose'
    return HttpResponse(r)