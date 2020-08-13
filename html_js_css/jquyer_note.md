##### jquery   绑定按钮点击事件

```javascript
$("#search").on("click", function () {
        
});

$('#btn1').click(function(){
    // 内部的this指的是原生对象
    // 使用jquery对象用 $(this)
})
```

##### ajax    post

```javascript
$('#search').click(function () {
    $.ajax({
        url: '/postpartum/assessment/',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({'phone': 1})
    })
        .done(function (data) {
            alert(data.name);
        })
        .fail(function () {
            alert('服务器超时，请重试！');
        });
});
```

##### ajax   get

```javascript





```

