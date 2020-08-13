##### JavaScript嵌入页面的方式

```javascript
// 1.行间事件（主要用于事件）
<input type="button" name="" onclick="alert('ok！');">
// 2.页面script标签嵌入
<script type="text/javascript">        
    alert('ok！');
</script>
// 3.外部引入
<script type="text/javascript" src="js/index.js"></script>
```

##### 变量

```javascript
var iNum = 123;
var iNum = 45,sTr='qwe',sCount='68';

1、number 数字类型
2、string 字符串类型
3、boolean 布尔类型 true 或 false
4、undefined undefined类型，变量声明未初始化，它的值就是undefined
5、null 可以将变量初始化为null
```

##### **变量、函数、属性、函数参数命名规范**

```
1、区分大小写
2、第一个字符必须是字母、下划线（_）或者美元符号（$）
3、其他字符可以是字母、下划线、美元符或数字
```

##### 获取元素

```javascript
// 此种写法需要元素写在上面, 文件是从上向下执行的
<div id="div1">这是一个div元素</div>

<script type="text/javascript">
    var oDiv = document.getElementById('div1');
</script>
---------------------------------------
// 将javascript语句放到window.onload触发的函数里面,获取元素的语句会在页面加载完后才执行
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementById('div1');
    }
</script>
<div id="div1">这是一个div元素</div>
```

##### 操作元素

```javascript
<script type="text/javascript">
    window.onload = function(){
        var oInput = document.getElementById('input1');
        var oA = document.getElementById('link1');
        // 读取属性值
        var sValue = oInput.value;
        var sType = oInput.type;
        var sName = oInput.name;
        var sLinks = oA.href;
        // 写(设置)属性
        oA.style.color = 'red';
        oA.style.fontSize = sValue;
    }
</script>
<input type="text" name="setsize" id="input1" value="20px">
<a href="http://www.itcast.cn" id="link1">传智播客</a>  
```

##### **innerHTML**

```javascript
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementById('div1');
        //读取
        var sTxt = oDiv.innerHTML;
        alert(sTxt);
        //写入
        oDiv.innerHTML = '<a href="http://www.itcast.cn">传智播客<a/>';
    }
</script>
<div id="div1">这是一个div元素</div>
```

##### **变量与函数预解析**

```javascript
// JavaScript解析过程分为两个阶段，先是编译阶段，然后执行阶段，在编译阶段会将function定义的函数提前，并且将var定义的变量声明提前，将它赋值为undefined。
<script type="text/javascript"> 
  	// 调用函数
    fnAlert();       
    alert(iNum);  // 弹出 undefined
    function fnAlert(){
        alert('hello!');
    }
    var iNum = 123;
</script>
```

##### 事件调用函数方式1

```javascript
<script type="text/javascript">        
    function fnAlert(){
        alert('ok!');
    }
</script>
<input type="button" name="" value="弹出" onclick="fnAlert()">
```

##### 事件调用函数方式2

```javascript
window.onload = function(){
    var oBtn = document.getElementById('btn1');
    oBtn.onclick = fnAlert;
    function fnAlert(){
        alert('ok!');
    }
}    
</script>
<input type="button" name="" value="弹出" id="btn1">
```

##### 匿名函数

```javascript
window.onload = function(){
    var oBtn = document.getElementById('btn1');
    oBtn.onclick = function (){
        alert('ok!');
    }
}
```

##### 有参数的函数

```javascript
<script type="text/javascript">
function add(a,b){
    var c = a + b;
    return c;
}
var d = add(3,4);
alert(d);  //弹出7
</script>
```

##### 封闭函数

```javascript
是匿名函数，定义了直接执行.可以传参数

写法1
(function(){
    var oDiv = document.getElementById('div1');
    oDiv.style.color = 'red';
})();
--------------------------------------------
写法2
!function(){
    var oDiv = document.getElementById('div1');
    oDiv.style.color = 'red';
}()
--------------------------------------------
写法3
~function(a){
    var oDiv = document.getElementById('div1');
    oDiv.style.color = 'red';
}()
```

##### 运算符

```javascript
1、算术运算符： +、 -、 *、 /、 %(求余)
2、赋值运算符：=、 +=、 -=、 *=、 /=、 %=
3、条件运算符：==、===、>、>=、<、<=、!=、&&(而且)、||(或者)、!(否)
var iNow = 1;
if(iNow==1)
{
    ... ;
}
else if(iNow==2)
{
    ... ;
}
else
{
    ... ;
}

// 多重if else语句可以换成性能更高的switch语句
switch (iNow){
    case 1:
        ...;
        break;
    case 2:
        ...;
        break;    
    default:
        ...;
}

for(var i=0;i<len;i++) {
    ......
}

while(i<8){
    ......
    i++;
}
```

##### 数组

```javascript
//对象的实例创建
var aList = new Array(1,2,3);
//直接量创建
var aList2 = [1,2,3,'asd'];

aList.length			# 长度
aList[0]				# 下标
aList.join('-')			# - 分隔符合并成字符串 
aList.push(5)			# 增加最后一个
aList.pop()				# 删除最后一个
aList.unshift(5)		# 增加第一个
aList.shift()			# 删除第一个
aList.reverse()			# 翻转
aList.indexOf(3)		# 元素3第一次出现的索引

var aList = [1,2,3,4];
aList.splice(2,1,7,8,9); //从第2个元素开始，删除1个元素，然后在此位置增加'7,8,9'三个元素
alert(aList); //弹出 1,2,7,8,9,4

var aList = [[1,2,3],['a','b','c']];
alert(aList[0][1]); //弹出2;

document.getElementsByTagName('')
```

##### 字符串

```java
parseInt() 		将数字字符串转化为整数
parseFloat() 	将数字字符串转化为小数
split() 		把一个字符串分隔成字符串组成的数组
charAt() 		获取字符串中的某一个字符
indexOf() 		查找字符串是否含有某字符
substring() 	截取字符串 用法： substring(start,end)（不包括end）
toUpperCase() 	字符串转大写
toLowerCase() 	字符串转小写

# 字符串反转
var str = 'asdfj12jlsdkf098';
var str2 = str.split('').reverse().join('');
alert(str2);
```

##### 类型转换

```javascript
parseInt(5.6)		# 转为int
parseFloat('5.6')	# 装维float
--------------------------------------------
隐式转换 “==” 和 “-”
if('3'==3){
    alert('相等');
}

alert('10'-3);  // 弹出7
--------------------------------------------
NaN非数字
isNaN 判断是不是非数字
```

