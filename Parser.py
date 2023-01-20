import pymssql
from fuzzywuzzy import process
import requests
from bs4 import BeautifulSoup
import re
url = 'http://lk.kalmsu.ru/php_ajax/3/schedule/get_schedule.php'
con = pymssql.connect(host="",
                      user="",
                      password="",
                      database="",
                      port=17160
                      )
def get_schedule(target_week_start, target_week_end, id_group):
    data = {
        'tip': 'group',
        'id_group': id_group,
        'target_week_start': target_week_start,
        'target_week_end': target_week_end
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
    }
    try:
        response = requests.post(url=url, headers=headers, data=data)
    except :
        return 'Сайт КалмГу не работает('
    res = format_the_response(response)
    return res
def format_the_response(response):
    soup = BeautifulSoup(response.content, "lxml")
    r =soup.select('.day_caption,.day_lesson,.schedule_card')
    z=[]

    for i in range(len(r)-1):
        #print(r[i])
        if r[i].find('span','time') and r[i].find('p','schedule_caption') ==None:
            continue
        else:
            if r[i].find('span','caption'):
                z.append('\n'+'📅'+r[i].find('span','caption').get_text() +' '+ r[i].find('span','date_caption').get_text())
            elif r[i].find('span','time'):
                z.append('⏱'  +r[i].find('span','time').get_text()+' ⏱')
            elif r[i].find('span','schedule_caption'):
                z.append( r[i].find('p','schedule_caption').get_text())
                z.append('Где: '+ r[i].findAll('span','schedule_caption')[0].get_text() + ' ' + r[i].findAll('span','schedule_caption')[1].get_text())
                z.append('Кто: '+ r[i].find('p','').get_text())


    res=''
    for i in z:
        res+=i+'\n'
    return res+'*Информация взята из открытых источников сети интернет\n'

def search_by_group(name_group):
    l=open('items/id_list.txt','r')
    lst = []
    for i in l:
        lst.append(i.lower())

    try:
        id = lst.index(name_group+'\n')+1
        return str(lst[id])
    except ValueError:
        return None
def search_by_group_if_nothing_found(name_group):
    l = open('items/id_list.txt', 'r')
    lst = []
    for i in l:
        lst.append(i.lower())
    PerhapsTheRightGroup=  process.extract(name_group,lst)
    if len(PerhapsTheRightGroup)!=0:
        res=[]
        for i in PerhapsTheRightGroup:
            res.append(i[0].strip())
        return res
    else:
        return None

