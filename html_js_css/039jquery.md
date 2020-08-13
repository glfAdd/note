```python
http://jquery.com/ 			官方网站
https://code.jquery.com/	版本下载
--------------------------------------------
<script type="text/javascript" src="js/jquery-1.12.2.js"></script>
<script type="text/javascript">
    $(document).ready(function(){
    });
    
    # 简写方式
    $(function(){
	});
</script>
```

选择器

```python
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

样式

```python
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

属性

```python
1、html() 取出或设置html内容
// 取出html内容
var $htm = $('#div1').html();
// 设置html内容
$('#div1').html('<span>添加文字</span>');

2、text() 取出或设置text内容
// 取出文本内容
var $htm = $('#div1').text();
// 设置文本内容
$('#div1').text('<span>添加文字</span>');

3、attr() 取出或设置某个属性的值
// 取出图片的地址
var $src = $('#img1').attr('src');
// 设置图片的地址和alt属性
$('#img1').attr({ src: "test.jpg", alt: "Test Image" });
```

绑定click事件

```python
$('#btn1').click(function(){
    // 内部的this指的是原生对象
    // 使用jquery对象用 $(this)
})
```

jquery特殊效果

```python
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

链式调试

```python
jquery对象的方法会在执行完后返回这个jquery对象，所有jquery对象的方法可以连起来写：

$('#div1') // id为div1的元素
.children('ul') //该元素下面的ul子元素
.slideDown('fast') //高度从零变到实际高度来显示ul元素
.parent()  //跳到ul的父元素，也就是id为div1的元素
.siblings()  //跳到div1元素平级的所有兄弟元素
.children('ul') //这些兄弟元素中的ul子元素
.slideUp('fast');  //高度实际高度变换到零来隐藏ul元素
```

动画

```python
通过animate方法可以设置元素某属性值上的动画，可以设置一个或多个属性值，动画执行完成后会执行一个函数。
swing	开始、结束慢，中间快（默认值）
linear	匀速

# 改变的属性 时间（毫秒） swing动画速度曲线 回调函数
$('#div1').animate({
    width:300,
    height:300
},1000,swing,function(){
    alert('done!');
});

参数可以写成数字表达式：
$('#div1').animate({
    width:'+=100',
    height:300
},1000,swing,function(){
    alert('done!');
});
```

尺寸

```python
# 获取和设置元素的尺寸
width()、height()    				获取元素width和height  
innerWidth()、innerHeight()  		包括padding的width和height  
outerWidth()、outerHeight()  		包括padding和border的width和height  
outerWidth(true)、outerHeight(true)	包括padding和border以及margin的width和height

# 获取元素相对页面的绝对位置
offse()
# 获取可视区高度
$(window).height();
# 获取页面高度
$(document).height();
# 获取页面滚动距离
$(document).scrollTop();  
$(document).scrollLeft();
# 页面滚动事件
$(window).scroll(function(){  
    ......  
})
```

