```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> html5文档类型 </title>
</head>
<body>
</body>
</html>
--------------------------------------------
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <title> xhtml 1.0 文档类型 </title>
</head>
<body>
</body>
</html>
--------------------------------------------
html文档规范
1、所有的标签必须小写
2、所有的属性必须用双引号括起来
3、所有标签必须闭合
4、img必须要加alt属性(对图片的描述)
--------------------------------------------
<!-- 成对出现的标签  -->
<body>...</body>

<!-- 单个出现的标签  -->
<img src="..." />

<h1>、<h2>、<h3>、<h4>、<h5>、<h6>
<p>		段落
<br />	换行
&nbsp;	多个空格
&lt &gt	< >

<img src="images/pic.jpg" alt="图片加载失败时显示的文字" />
<a href="#">链接到页面顶部</a>
<a href="http://www.baidu.com/" title="鼠标停留提示文字">传智播客</a>

<a href="#mao1">href和id成对使用</a>
<h3 id="mao1">跳转到mao1这个位置</h3>

<ol>
    <li>有序列表</li>
</ol>

<ul>
    <li>无序列表</li>
</ul>

<dl>
<!-- dl标签表示列表的整体 -->
    <dt>标签定义术语的题目</dt>
    <dd>标签是术语的解释</dd>
</dl>
```

表格

```python
table常用标签
1、table标签：声明一个表格
2、tr标签：定义表格中的一行
3、td和th标签：定义一行中的一个单元格，td代表普通单元格，th表示表头单元格

table常用属性：
1、border 		边框
2、cellpadding 	内容与边框距离
3、cellspacing 	单元格与单元格间的距离
4、align 		水平对齐left | center | right
5、valign 		垂直对齐top  | middle | bottom
6、colspan 		水平合并
7、rowspan 		垂直合并
--------------------------------------------
<table border="5" width="500" height="200" cellpadding="30" cellspacing="20">
	<tr>
		<th colspan="2">111</th>
		<th rowspan="2">222</th>
		<th align="left">333</th>
		<th valign="top">444</th>
		<th >555</th>
	</tr>

	<tr>
		<th>111</th>
		<th>222</th>
		<th>333</th>
		<th>444</th>
		<th>555</th>
	</tr>

	<tr>
		<th>111</th>
		<th>222</th>
		<th>333</th>
		<th>444</th>
		<th>555</th>
		<th>666</th>
	</tr>

<table>
```

表单

```python
action属性定义表单数据提交的地址，
method属性定义提交的方式。 

<form action="http://www..." method="get">
<label>单行文本输入框</label><input type="text" name="username" />
<br/>

<label>密码</label><input type="password" name="password" />
<br/>

<label>单选框</label>
<input type="radio" name="gender" value="0" /> 男
<input type="radio" name="gender" value="1" /> 女
<br/>

<label>多选框</label>
<input type="checkbox" name="like" value="sing" /> 唱歌
<input type="checkbox" name="like" value="run" /> 跑步
<input type="checkbox" name="like" value="swiming" /> 游泳
<br/>

<label>上传</label>
<input type="file" name="person_pic">
<br/>

<label>多行文本输入</label>
<textarea name="about"></textarea>
<br/>

<label>下拉列表选择：</label>
<select name="site">
    <option value="0">北京</option>
    <option value="1">上海</option>
    <option value="2">广州</option>
    <option value="3">深圳</option>
</select>
<br/>

<input type="submit" name="" value="提交按钮">
<input type="reset" name="" value="重置按钮">
</form>
```

内嵌框架

```python
<a href="http://www.baidu.com" target="myframe">页面一</a>
<a href="http://www.taobao.com" target="myframe">页面二</a>
<iframe src="http://www.baidu.com" frameborder="0" scrolling="no" name="myframe" height="500" width="1000"></iframe>
```

