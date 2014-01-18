#coding=utf-8 
import urllib2
import urllib
import requests
import re
from urllib import urlencode
# from requests_toolbelt.multipart import MultipartEncoder
def login():
	name=""
	pw=""
	login_url="http://bbs.nju.edu.cn/vd26401/bbslogin?type=2"
	para={
	    'id':name,
	    'pw':pw
	    }
	# post_data=urllib.urlencode(para)
	# req=urllib2.Request(login_url,post_data)
	# resp=urllib2.urlopen(req)
	# file=resp.read()
	# c_cookie=re.findall(r'.+?setCookie\(\'(.+?)\'\).+?', file, re.S)
	# print c_cookie
	r = requests.post(login_url, data=para)
	print r.content
	
	c_cookie=re.findall(r'.+?setCookie\(\'(.+?)\'\).+?', r.text)
	
	return c_cookie

def logout(c_cookie):
	# data is a list like ['222Nluckydedong+81755315']

	str_cookie=c_cookie[0]
	_U_NUM=int(re.findall(r'(\d+)N', str_cookie)[0])+2
	_U_UID=re.findall(r'.+?N(\w+)\+', str_cookie)[0]
	_U_KEY=int(re.findall(r'.+?\+(\d+)$', str_cookie)[0])-2
	FOOTKEY='1988883348'
	logout_url='http://bbs.nju.edu.cn/vd25709/bbslogout'
	cookie={'_U_NUM':str(_U_NUM), '_U_UID':_U_UID, '_U_KEY':str(_U_KEY), 'FOOTKEY':FOOTKEY}
	
	r = requests.post(logout_url, cookies=cookie)
	print r
	# req = urllib2.Request(logout_url)
	# req.add_header('Cookie', cookie)
	# print cookie
	# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:20.0) Gecko/20100101 Firefox/20.0')
	# response=urllib2.urlopen(req)
	# res=response.read()
	# print res




#comment 
# title=Re: 南大最浪漫的事，屌丝有木有&pid=886196475&reid=1389427065&reusr=MCsquare&signature=1&autocr=on&text=小幸福中都是真情，祝福祝福！
# 【 在 MCsquare 的大作中提到: 】
# : 
# :     要结婚了，去了一趟婚纱影楼，准备拍一套婚纱照，屌丝真是伤不起，太贵..
# : 宜的1999，内景和外景各一套，最后有40张精修相片给我们；3999，内景和外景..
# : 最后有40张精修相片给我们；不过我们能买得起的这两个价格的套系都很犹豫，..
# : 用鄙视的眼光看我们，不停地向我们推荐5999以上的套餐。
# :    大家都做得很俗的事，能不能在我们手中做得不一样些呢？
# :    要不我们自己拍吧，关键是让更多的同学参与进来，会得到更多人的祝福，..
# : 一张相片入册更有意义一些。最主要的是我们想让每一张相片都有故事。
# : 
# :    首先要解决拍照的技术问题，没有摄影师我们如何解决？原来特别简单，现..
# : 方便，只要一个无线快门就可以了。
# :    http://bbs.nju.edu.cn/file/Pictures/MCsquare1389424445.jpg
# : 
# :    其次是服装，没有设计师和化妆师，我们如何解决？淘宝一找，什么都有，..
# : 以下的装备，全部买完，才900元。穿上就好了，加上天生丽质，不化妆，直接拍。
# : http://bbs.nju.edu.cn/file/Pictures/MCsquare1389424477.JPG
# :    
# :    事情和同学一说，都非常乐意帮忙，开心了。
# : 
# : http://bbs.nju.edu.cn/file/Pictures/IMG_8038.jpg
# : (以下引言省略...)


def comment(c_cookie):
	str_cookie=c_cookie[0]
	_U_NUM=int(re.findall(r'(\d+)N', str_cookie)[0])+2
	_U_UID=re.findall(r'.+?N(\w+)\+', str_cookie)[0]
	_U_KEY=int(re.findall(r'.+?\+(\d+)$', str_cookie)[0])-2
	FOOTKEY='1988883348'
	logout_url='http://bbs.nju.edu.cn/vd25709/bbssnd?board=Pictures'
	cookie={'_U_NUM':str(_U_NUM), '_U_UID':_U_UID, '_U_KEY':str(_U_KEY), 'FOOTKEY':FOOTKEY}
	# cookie='_U_NUM='+str(_U_NUM)+';_U_UID='+_U_UID+';_U_KEY='+str(_U_KEY)
	# print cookie
	# # Submit=%D7%A2%CF%FA%B5%C7%C2%BC
	# title=Re: 南大最浪漫的事，屌丝有木有&pid=886196475&reid=1389427065&reusr=MCsquare&signature=1&autocr=on&text=小幸福中都是真情，祝福祝福！
	title=u'Re: 南大最浪漫的事，屌丝有木有'
	text=u'小幸福中都是真情，祝福祝福！'
	title=title.encode('gbk')
	text=text.encode('gbk')
	payload={'title':title, 'pid':'886196475', 'reid':'1389427065','reusr':'MCsquare','signature':'1','autocr':'on','text':text}
	dataEncoded=urlencode(payload)
	r = requests.post(logout_url, data=payload, cookies=cookie)
	print r

def test():
	# payload={'title':'Re: 南大最浪漫的事，屌丝有木有', 'pid':'886196475', 'reid':'1389427065','reusr':'MCsquare','signature':'1','autocr':'on','text':'小幸福中都是真情，祝福祝福！'}
	# urlencode(payload)
	data=u'南大最浪漫的事，屌丝有木有'

	if isinstance(data,unicode):
		print data.encode('gbk')
	else:
		print 'world'



def sendFileTest(c_cookie):
	str_cookie=c_cookie[0]
	_U_NUM=int(re.findall(r'(\d+)N', str_cookie)[0])+2
	_U_UID=re.findall(r'.+?N(\w+)\+', str_cookie)[0]
	_U_KEY=int(re.findall(r'.+?\+(\d+)$', str_cookie)[0])-2
	FOOTKEY='1988883348'
	url='http://bbs.nju.edu.cn/bbsdoupload'
	cookie={'_U_NUM':str(_U_NUM), '_U_UID':_U_UID, '_U_KEY':str(_U_KEY), 'FOOTKEY':FOOTKEY}
	# form_value={'exp':'python', 'ptext':'text', 'board':'Pictures'}
	myfile = [
		('up', ('a', open('c:/a', 'rb'), 'application/octet-stream')),
		('exp',(None, 'pp', None)),
		('ptext',(None, 'ss',None)),
		('board',(None, 'D_Computer', None))
		]
	r = requests.post(url, files=myfile, cookies=cookie)
	print r.text.encode('utf-8')

	img_url = re.findall(r".+url=([^']+)", r.text, re.S)[0]
	img2 = img_url.replace('\r\n','')
	print img2
	uu = 'http://bbs.nju.edu.cn/'+img2
	print requests.get(uu, cookies=cookie).text.encode('utf-8');
	
	
	print r
# c_cookie=login()
# [u'779Nkeygen+68718282']
# print c_cookie


# comment(c_cookie)
sendFileTest(c_cookie)
# logout(c_cookie)
