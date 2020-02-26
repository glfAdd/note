##### css页面引入方法：
```
1、外联式：通过link标签，链接到外部样式表到页面中。
<link rel="stylesheet" type="text/css" href="css/main.css">

2、嵌入式：通过style标签，在网页上创建嵌入的样式表。
<style type="text/css">
    div{ width:100px; height:100px; color:red }
</style>

3、内联式：通过标签的style属性，在标签上直接写样式。
<div style="width:100px; height:100px; color:red ">......</div>
```
##### css文本设置:
```
color 颜色. color:red;
font-size 大小. font-size:12px;
font-family 字体. font-family:'微软雅黑';
font-style 是否倾斜. font-style:'normal'; 设置不倾斜，font-style:'italic';设置文字倾斜
font-weight 是否加粗. font-weight:bold; 设置加粗 font-weight:normal 设置不加粗
line-height 行高. line-height:24px;
同时设置文字的几个属性，写的顺序有兼容问题，建议按照如下顺序写： font：是否加粗 字号/行高 字体；如： font:normal 12px/36px '微软雅黑';

text-decoration 下划线. text-decoration:none; 将文字下划线去掉
text-indent 文字首行缩进. text-indent:24px
text-align 对齐方式. text-align:center水平居中
```
##### css颜色表示法
```
颜色名表示. red gold
rgb表示. rgb(255,0,0)
16进制数值表示. #ff0000, 这种可以简写成 #f00
```

##### 选择器

```css
(1)标签选择器 
div{color:red}
<div>....</div>
(2)id选择器
#box{color:red} 
<div id="box">....</div>
(3)类选择器 
.red{color:red}
<div class="red">....</div>
(4)层级选择器
.box span{color:red}
.box .red{color:pink}
.red{color:red}
<div class="box">
    <span>....</span>
    <a href="#" class="red">....</a>
</div>
<h3 class="red">....</h3>
(5)组选择器
.box1,.box2,.box3{width:100px;height:100px}
<div class="box1">....</div>
<div class="box2">....</div>
<div class="box3">....</div>
(6)伪类及伪元素选择器:常用的伪类选择器有hover，表示鼠标悬浮在元素上时的状态，伪元素选择器有before和after,它们可以通过样式在元素中插入内容
.box1:hover{color:red}
.box2:before{content:'行首文字';}
.box3:after{content:'行尾文字';}
<div class="box1">....</div>
<div class="box2">....</div>
<div class="box3">....</div>
```

##### CSS盒子模型

```



```

