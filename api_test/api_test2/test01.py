# 上节课 postman接口测试  postman关联 断言 参数化 生成测试报告

# 这节课：重点
# 1.requests做接口测试
# 2.jsonpath的使用
# 3.接口关联

# 1.安装
import json

import jsonpath
import requests

# get请求
# 接口
# 接口步骤：
# 接口地址
# 接口参数
# 请求方式
# 响应内容

# 百度
# url='http://www.baidu.com'
# res=requests.get(url)
# 打印响应回来的内容  二进制文本内容
# print(res.content)
# 文本内容
# print(res.text)
# 接口地址
# print(res.url)
# cookie
# print(res.cookies)
# 打印头部内容
# print(res.headers)
# 打印json
# print(res.json())

# 请求不带参数  get请求带参数
# url='http://39.98.138.157:5000/api/gettomorrow'
# data={"city":"1"}
# res=requests.get(url=url,params=data)
# print(res.text,type(res.text))
# print(res.json(),type(res.json()))
# # 取响应回来的内容 res.json 好取点 数据类型 字典类型
# # res.text响应回来的内容  字符串类型

# post请求
# url='http://39.98.138.157:5000/api/login'
# data={"password": "123456","username": "admin"}
# print(type(data))
# # def post(url, data=None, json=None, **kwargs):  为什么用json
# res=requests.post(url,json=data)
# print(res.json())

# 什么时候用data 什么时候用json呢？ 看content-type数据类型 如果是json  要用json传
# 非要用data传可不可以 可以噢

# data 要求传的是字符串
# json要求传的是字典类型

# 接口文档 要求传的content-type:application/json
# url='http://39.98.138.157:5000/api/login'
# data='{"password": "123456","username": "admin"}'
# print(type(data))
#
# header={"content-type":"application/json"}# def post(url, data=None, json=None, **kwargs):  为什么用json
# # 加个请求头
# res=requests.post(url,data=data,headers=header)
# print(res.headers)
# print(res.json())

# 接口文档 实际的接口参数类型不一致 就要改  改json
# 运行成功 1  运行不成功2  数据类型是开发写接口的时候就定义好了

# data 要求传的是字符串
# 手动把字典改成的字符串
# url='http://39.98.138.157:5000/api/login'
# data={"password": "123456","username": "admin"}
# # 字典改成的字符串  json.dumps(data)
# data1=json.dumps(data)
# # print(type(data1))
# header={"content-type":"application/json"}# def post(url, data=None, json=None, **kwargs):  为什么用json
# # 加个请求头
# res=requests.post(url,data=data1,headers=header)
# print(res.json())

# json提交 字典类型数据
# # 字符串改成字典
# url='http://39.98.138.157:5000/api/login'
# data='{"password": "123456","username": "admin"}'
# # 字符串改成字典
# # data1=json.loads(data)
# # print(type(data1))
# data1=eval(data)
# print(type(data1))
# # 加个请求头
# res=requests.post(url,json=data1)
# print(res.json())
# print(res.headers)

# 总结：传json数据  重点理解  json取值
# 1.可以直接用json传参
# 2.如果你要用data传参  数据改成字符串类型
# json传字典  data传字符串
# 字符串改成字典 json.loads(data) eval
# 字典改成字符串 json.dumps(data)
# json.load:用于读取文件中json数据
# json.dump:用于写入json文件中，字典转成字符串写文件中
# data里面修改请求头


# json.load和json.dump
# json.load:用于读取文件中json数据
# json.dump:用于写入json文件中，字典转成字符串写文件中
# data={"password": "123456","username": "admin"}
# # print(type(data))
# f=open('tt.txt','a')
# json.dump(data,f)

# 读取出来文件是字符串
# f1=open('tt.txt','r')
# print(f1.read(),type(f1.read()))

# f1=open('tt.txt','r')
# ff=json.load(f1)
# print(ff,type(ff))

# 登录接口测试  测试一条用例 预期结果 实际结果 判断
url='http://39.98.138.157:5000/api/login'
data='{"password": "123456","username": "admin"}'
# 字符串改成字典
# data1=json.loads(data)
# print(type(data1))
data1=eval(data)
print(type(data1))
# 加个请求头
res=requests.post(url,json=data1)
print(res.text)
# 如果这条用例返回来的是success 用例成功 用例失败
# 预期结果
exmsg='success'
# # 实际结果 实际结果  msg的字段的值  字典 取值
# 其他的方式？取到实际结果 正则可以 json取值 json格式的数据
# 字典 数据类型 数据格式 通过json去取值
# sjmsg=res.json()['msg']
# 数据,表达式
sjmsg=jsonpath.jsonpath(res.json(),'$..msg')[0]
print(sjmsg)
# # 判断
if exmsg==sjmsg:
    print('用例成功')
else:
    print('用例失败')
# 相等 啥事没有 不相等 报错  提示很不友好  有个友好的提示 用什么方式 会有个友好的提示
# try:
#     assert exmsg==sjmsg
#     print('用例成功')
# except Exception as e:
#     print('用例失败')

# json怎么取值  几道题目

# 接口关联
