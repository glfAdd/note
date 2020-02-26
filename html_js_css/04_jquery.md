##### 简介

- jquery是一个函数库，一个js文件，页面用script标签引入这个js文件就可以使用
- 将获取元素的语句写到页面头部，会因为元素还没有加载而出错，jquery提供了ready方法解决这个问题，它的速度比原生的 window.onload 更快。

```javascript
<script type="text/javascript" src="js/jquery-1.12.2.js"></script>
<script type="text/javascript">
$(document).ready(function(){
     ......
});

// 简写为
$(function(){
     ......
});  
</script>
```

#####选择器

```javascript
选择器：快速地选择元素。
$(document) 			//选择整个文档对象
$('li') 				//选择所有的li元素
$('#myId') 				//选择id为myId的网页元素
$('.myClass') 			// 选择class为myClass的元素
$('input[name=first]')	// 选择name属性等于first的input元素
$('#ul1 li span') 		//选择id为为ul1元素下的所有li下的span元素
--------------------------------------------
对选择集进行修饰过滤(类似CSS伪类)
$('#ul1 li:first') 		//选择id为ul1元素下的第一个li
$('#ul1 li:odd') 		//选择id为ul1元素下的li的奇数行
$('#ul1 li:eq(2)') 		//选择id为ul1元素下的第3个li
$('#ul1 li:gt(2)') 		//选择id为ul1元素下的前三个之后的li
$('#myForm :input') 	//选择表单中的input元素
$('div:visible') 		//选择可见的div元素
--------------------------------------------
对选择集进行函数过滤
$('div').has('p'); 				//选择包含p元素的div元素
$('div').not('.myClass'); 		//选择class不等于myClass的div元素
$('div').filter('.myClass');	//选择class等于myClass的div元素
$('div').first(); 				//选择第1个div元素
$('div').eq(5); 				//选择第6个div元素
--------------------------------------------
选择集转移
$('div').prev('p'); 		//选择div元素前面的第一个p元素
$('div').next('p'); 		//选择div元素后面的第一个p元素
$('div').closest('form'); 	//选择离div最近的那个form父元素
$('div').parent(); 			//选择div的父元素
$('div').children(); 		//选择div的所有子元素
$('div').siblings(); 		//选择div的同级元素
$('div').find('.myClass'); 	//选择div内的class等于myClass的元素
```

##### 样式

```javascript
获取div的样式
$("div").css("width");
$("div").css("color");
--------------------------------------------
设置div的样式
$("div").css("width","30px");
$("div").css("height","30px");
$("div").css({fontSize:"30px",color:"red"});
--------------------------------------------
操作样式类名
$("#div1").addClass("divClass2") //为id为div1的对象追加样式divClass2
$("#div1").removeClass("divClass")  //移除id为div1的对象的class名为divClass的样式
$("#div1").removeClass("divClass divClass2") //移除多个样式
$("#div1").toggleClass("anotherClass") //重复切换anotherClass样式
--------------------------------------------
选择器获取的多个元素，获取信息获取的是第一个，比如：$("div").css("width")，获取的是第一个div的width。
```

##### 绑定click事件

```javascript
$('#btn1').click(function(){
    // 内部的this指的是原生对象
    // 使用jquery对象用 $(this)
})
```

##### **获取元素的索引值** 

```javascript
var $li = $('.list li').eq(1);
alert($li.index()); // 弹出1
......
<ul class="list">
    <li>1</li>
    <li>2</li>
    <li>4</li>
    <li>5</li>
    <li>6</li>
</ul>
```

##### jquery特殊效果

```javascript
fadeIn() 淡入
fadeOut() 淡出
fadeToggle() 切换淡入淡出
hide() 隐藏元素
show() 显示元素
toggle() 依次展示或隐藏某个元素
slideDown() 向下展开
slideUp() 向上卷起
slideToggle() 依次展开或卷起某个元素

$btn.click(function(){
    $('#div1').fadeIn(1000,'swing',function(){
        alert('done!');
    });
});
```

##### 属性操作

```javascript
// 取出html内容
var $htm = $('#div1').html();
// 设置html内容
$('#div1').html('<span>添加文字</span>');

// 取出图片的地址
var $src = $('#img1').prop('src');
// 设置图片的地址和alt属性
$('#img1').prop({src: "test.jpg", alt: "Test Image" });
```

##### 循环

- 对jquery选择的对象集合分别进行操作，需要用到jquery循环操作，此时可以用对象上的each方法

```javascript
$(function(){
    $('.list li').each(function(i){
        $(this).html(i);
    })
})
......
<ul class="list">
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ul>
```

##### jquery事件

```javascript
blur() 元素失去焦点
focus() 元素获得焦点
click() 鼠标单击
mouseover() 鼠标进入（进入子元素也触发）
mouseout() 鼠标离开（离开子元素也触发）
mouseenter() 鼠标进入（进入子元素不触发）
mouseleave() 鼠标离开（离开子元素不触发）
hover() 同时为mouseenter和mouseleave事件指定处理函数
ready() DOM加载完成
resize() 浏览器窗口的大小发生改变
scroll() 滚动条的位置发生变化
submit() 用户递交表单

$(function(){
    $('#div1').bind('mouseover click', function(event) {
        alert($(this).html());

      	// 取消绑定事件
        // $(this).unbind();
        $(this).unbind('mouseover');

    });
});
```



 

























