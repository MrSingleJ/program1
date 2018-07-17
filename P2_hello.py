#!D:\anaconda\an\envs\python36\python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from P2_Ml_single import *
import cgi, cgitb 
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 
# 获取数据
speal_width =3#int(form.getvalue('speal_width'))
speal_length =3# int(form.getvalue('speal_length'))
petal_width =3#int(form.getvalue('petal_width'))
petal_length =3#int(form.getvalue('petal_length'))
t = [[speal_width,speal_length,petal_width,petal_length]]
ml = ml_single.singleton()
x = ml.getpredict(t)
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print("<form action=\"P2_hello.py\" method=\"POST\">")
print("speal width: <input type=\"text\" name=\"speal_width\">  <br />")   
print("speal length: <input type=\"text\" name=\"speal_length\" /><br/>")
print ("petal width: <input type=\"text\" name=\"petal_width\" /><br/>")
print ("petal length: <input type=\"text\" name=\"petal_length\" /><br/>")
print("<input type= \"submit\" value=\"Get type\" />")
print("</form>")
print ("<h2>预测类型:%s </h2>" %(x))
print ("</body>")
print ("</html>")
