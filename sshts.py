#! /usr/bin/env python
# coding=utf-8
from flask import Flask
import os
import time

app = Flask(__name__)

sshdict={
        'http://116.62.46.33:60666/Pain/index.html':'87',
        'http://116.62.46.33:60686/Pain/index.html':'86',
        'http://116.62.46.33:60001/Pain/index.html':'发射器测试',
        'http://116.62.46.33:60006/Pain/index.html':'东营人民',
        'http://116.62.46.33:60008/Pain/index.html':'天门人民',
        'http://116.62.46.33:60023/Pain/index.html':'平南第二人民',
        'http://116.62.46.33:60028/Pain/index.html':'梧州桂东',
        'http://116.62.46.33:60031/Pain/index.html':'南华附一',
        'http://116.62.46.33:60034/Pain/index.html':'河南153',
        'http://116.62.46.33:60039/Pain/index.html':'广东省二',
        'http://116.62.46.33:60050/Pain/index.html':'千佛山',
        'http://116.62.46.33:60055/Pain/index.html':'绵阳404',
        'http://116.62.46.33:60067/Pain/index.html':'河南省空军',
        'http://116.62.46.33:60074/Pain/index.html':'龙岗骨科',
        'http://116.62.46.33:60084/Pain/index.html':'邢台人民',
        'http://116.62.46.33:60089/Pain/index.html':'昆明医科大学附二（麻醉）',
        'http://116.62.46.33:60093/homepage.html':'昌吉人民（MC）',
        'http://116.62.46.33:60094/Pain/index.html':'江西省妇保',
        'http://116.62.46.33:60097/Pain/index.html':'深圳总院',
        'http://116.62.46.33:60105/Pain/index.html':'昌吉人民（术后）',
        'http://116.62.46.33:60109/Pain/index.html':'临沂人民',
        'http://116.62.46.33:60111/Pain/index.html':'西安红会（一部）',
        'http://116.62.46.33:60112/Pain/index.html':'西安红会（二部）',
        'http://116.62.46.33:60113/Pain/index.html':'永州中心',
        'http://116.62.46.33:60115/Pain/index.html':'惠安妇保',
        'http://116.62.46.33:60126/Pain/index.html':'成都市一',
        'http://116.62.46.33:60127/Pain/index.html':'成都妇幼',
        'http://116.62.46.33:60133/Pain/index.html':'苏州科技城',
        'http://116.62.46.33:60147/Pain/index.html':'随州中心',
        'http://116.62.46.33:60152/Pain/index.html':'湖南省人民',
        'http://116.62.46.33:60154/Pain/index.html':'汉川人民',
        'http://116.62.46.33:60170/Pain/index.html':'东莞常平',
        'http://116.62.46.33:60173/Pain/index.html':'佛山市一',
        'http://116.62.46.33:60183/Pain/index.html':'陕西人民',
        'http://116.62.46.33:60191/Pain/index.html':'周口市中心',
        'http://116.62.46.33:60192/Pain/index.html':'六安市人民',
        'http://116.62.46.33:60194/Pain/index.html':'苏州附一',
        'http://116.62.46.33:60199/Pain/index.html':'潮州人民',
        'http://116.62.46.33:60201/Pain/index.html':'东莞市高埗',
        'http://116.62.46.33:60208/Pain/index.html':'张家口第一',
        'http://116.62.46.33:60213/Pain/index.html':'南昌大一',
        'http://116.62.46.33:60214/Pain/index.html':'榆林二院',
        'http://116.62.46.33:60215/Pain/index.html':'南医三',
        'http://116.62.46.33:60216/Pain/index.html':'上海四院',
        'http://116.62.46.33:60217/Pain/index.html':'德宏州',
        'http://116.62.46.33:60222/Pain/index.html':'石岩人民',
        'http://116.62.46.33:60228/Pain/index.html':'杭州市妇产',
        'http://116.62.46.33:60230/Pain/index.html':'萍乡市妇幼',
        'http://116.62.46.33:60231/Pain/index.html':'宜昌市一',
        'http://116.62.46.33:60234/Pain/index.html':'南部县人民',
        'http://116.62.46.33:60238/Pain/index.html':'公安县人民',
        'http://116.62.46.33:60240/Pain/index.html':'綦江区人民',
        'http://116.62.46.33:60241/Pain/index.html':'常州市一',
        'http://116.62.46.33:60242/Pain/index.html':'湖南妇女儿童',
        'http://116.62.46.33:60243/Pain/index.html':'重庆璧山区人民',
        'http://116.62.46.33:60245/Pain/index.html':'抚顺矿务局',
        'http://116.62.46.33:60247/Pain/index.html':'泰康同济武汉',
        'http://116.62.46.33:60254/Pain/index.html':'梧州市人民',
	'http://116.62.46.33:60255/Pain/index.html':'楚雄州人民',
        'http://116.62.46.33:65035/Pain/index.html':'成都市三（DDB）',
        'http://116.62.46.33:65040/Pain/index.html':'黔南州人民'
        }

@app.route('/sshonline')
def sshonline():
    tstime=time.ctime(os.stat("sshoffline.txt").st_mtime) #文件的修改时间即ssh check update time
    ssh=[]
    tsoffline=[]
    tsonline=[]
    with open("ssh.txt", 'r') as file:
        for line in file.readlines():
            temp=line.replace('\n','')
            ssh.append(temp)
    with open("sshoffline.txt", 'r') as file:
        for line in file.readlines():
            temp=line.replace('\n','')
            tsoffline.append(temp)
    with open("sshonline.txt", 'r') as file:
        for line in file.readlines():
            temp=line.replace('\n','')
            tsonline.append(temp)

    html = f"""
	<html><head>
    <title>apon ssh</title>
    <link rel="shortcut icon" href="static/favicon.ico"> 
    <meta http-equiv="refresh" content="60">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=0.5, maximum-scale=2.0, user-scalable=yes" />
    	</head><body>
    """
    html += f"""
        <h1><center>OnLine</center></h1>
        <h2>&ensp;SSH Total:&thinsp;{str(len(ssh))}&ensp;|&ensp;<a href="http://101.34.92.86:5000/sshoffline">SSH Offline:&thinsp;{str(len(tsoffline))}</a></h2>
        <h2>&ensp;<font color="#00E3E3">SSH Online:&thinsp;{str(len(tsonline))}</font></h2>
	    <h3>&ensp;Check Time:&thinsp;{tstime}</h3>
        <ol>
    """ 

    for i in range(0,len(tsonline)):
      html += f"""
        <li>
        {sshdict.get(str(tsonline[i]))}:  <a href="{tsonline[i]}" target="_blank">{tsonline[i]}</a>
        </li>
        <br/>
      """
        
    html += f"""
    </ol>
    <footer style="margin-bottom:15px;text-align: center;padding:10px;">
        <span>Copyright &copy; 2021.</span>
        <span> Published by <a href="https://github.com/chenonce" target="_blank">chen</a> on<a href="https://github.com/chenonce/apon"> GitHub</a>.</span>
    </footer>
    </body></html>
    """
    return html


@app.route('/sshoffline',methods=['GET','POST'])
def sshoffline():  
    tstime=time.ctime(os.stat("sshoffline.txt").st_mtime) #文件的修改时间即ssh check update time
    ssh=[]
    tsoffline=[]
    tsonline=[]
    with open("ssh.txt", 'r') as file:
        for line in file.readlines():
            temp=line.replace('\n','')
            ssh.append(temp)

    with open("sshoffline.txt", 'r') as file:
        for line in file.readlines():
            temp=line.replace('\n','')
            tsoffline.append(temp)

    with open("sshonline.txt", 'r') as file:
        for line in file.readlines():
            temp=line.replace('\n','')
            tsonline.append(temp)
    
    html = f"""
	<html><head>
    <title>apon ssh</title> 
    <link rel="shortcut icon" href="static/favicon.ico">
    <meta http-equiv="refresh" content="60">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=0.5, maximum-scale=2.0, user-scalable=yes" />
    	</head><body>
    """
    html += f"""
        <h1><center>OffLine</center></h1>
        <h2>&ensp;SSH Total:&thinsp;{str(len(ssh))}&ensp;|&ensp;<a href="http://101.34.92.86:5000/sshonline">SSH Online:&thinsp;{str(len(tsonline))}</a></h2>
        <h2>&ensp;<font color="#FF0000">SSH Offline:&thinsp;{str(len(tsoffline))}</font></h2>
	    <h3>&ensp;Check Time:&thinsp;{tstime}</h3>
        <ol>
    """ 
    for i in range(0,len(tsoffline)):
      html += f"""
        <li>
        {sshdict.get(str(tsoffline[i]))}:  <a href="{tsoffline[i]}" target="_blank">{tsoffline[i]}</a>
        </li>
        <br/>
      """
        
    html += f"""
    </ol>
    <footer style="margin-bottom:15px;text-align: center;padding:10px;">
        <span>Copyright &copy; 2021.</span>
        <span> Published by <a href="https://github.com/chenonce" target="_blank">chen</a> on<a href="https://github.com/chenonce/apon" target="_blank"> GitHub</a>.</span>
    </footer>
    </body></html>
    """
    return html

app.run(host='0.0.0.0',port='5000',debug=True)
