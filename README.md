SmartCar
========

智能车大赛官网
============

使用的库
-------
* **Django 1.4**
* django-gravatar 用户头像
* django-markdown 渲染markdown文本


注册流程
-------
* 输入注册表单（表单错误则返回）
* 验证用户是否存在（已存在则返回）
* 添加用户（未激活用户）
* 生成激活码
* 保存激活码（保存于激活码表）
* 发送激活码（发送失败则返回）
* 点击验证地址
* 验证用户和验证码是否存在（不存在则返回）
* 填写详细资料（错误则返回）
* 保存详细资料并激活用户
* 删除激活码
* 注册成功……