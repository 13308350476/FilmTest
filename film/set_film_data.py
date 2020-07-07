"""
from film.models import tb_Film
import random
from django.http import HttpResponse


def insert(request):
    for i in range(0, 5):
        studentNum = int(random.uniform(0, 1) * 10000000000)
        # 从models文件中获取student对象
        tb_film = tb_Film()
        # 给对象赋值
        tb_film.fl_filmid_str = studentNum
        tb_film.fl_title_str = 'tom' + str(i)
        tb_film.fl_intro_str = 15
        tb_film.fl_goodNum_int = random.choice([True, False])
        tb_film.fl_replyNum_int = int(random.uniform(0, 1) * 10000000000)
        tb_film.fl_grade_str = int(random.uniform(0, 1) * 10000000000)
        # 插入数据
        tb_film.save()
    return HttpResponse('数据插入完毕')


def find(request, film_id):
    # sql = 'select * from student'
    # django 也可以执行原生的sql语句
    # result = Student.objects.raw(sql)
    # 查询name = tom1的数据
    result = tb_Film.objects.filter(fl_filmid_str=film_id)

    # result为<class 'django.db.models.query.QuerySet'>的对象
    # 需要进行数据处理

    arr = []
    for i in result:
        content = {'电影名称': i.fl_title_str, '类型': i.fl_intro_str, '豆瓣评分': i.fl_goodNum_int}
        arr.append(content)
    print(arr)
    print(type(arr))
    return HttpResponse(arr)


def modify(request, film_id):
    # 通过学号获取student对象
    tb_film = tb_Film.objects.get(fl_filmid_str=film_id)
    # 设置student的name为jack
    tb_film.fl_title_str = 'jack'
    tb_film.save()
    return HttpResponse('修改成功.')


def delete(request, film_id):
    tb_film = tb_Film.objects.get(fl_filmid_str=film_id)
    tb_film.delete()
    return HttpResponse('删除成功.')

"""
