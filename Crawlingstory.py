# _*_ coding:utf-8 _*_
import requests,re
url='https://www.qingkanshu.cc/35_35068/'
'20930899.html 34287611.html'
def get_pages(url):
    res=requests.get(url)
    reg=re.compile('<dd><a href ="/35_35068/(.*)">')
    pages=re.findall(reg,res.text)
    stroypages=[]
    for i in pages[3503:3506]:
        storypage='https://www.qingkanshu.cc/35_35068/'+i
        stroypages.append(storypage)
    return stroypages
def write_storys(url):
    try:
        res=requests.get(url)
    except:
        res = requests.get(url)
    reg=re.compile('<h1>(.*)</h1>')
    result=res.text
    print(result)
    title=re.findall(reg,result)[0]
    reg_content=re.compile('class="showtxt">(.*)<br /><br /></div>')
    content=re.findall(reg_content,result)[0]
    content=str(content).replace('&nbsp;','').replace('<br />','\n')
    story=title+'\n'+content
    print(f'{title}')
    with open("story1",'a')as f:
        f.write(story)
# urls=get_pages(url)
# for url in urls:
#     write_storys(url)



def count():#统计重复章节
    with open('story')as f:
        content=f.read()
    reg=re.compile('第(\d+)章')
    list=re.findall(reg,content)
    a={}
    for i in list:
        if list.count(i) > 2:
            a[i] = list.count(i)
    print(a)
