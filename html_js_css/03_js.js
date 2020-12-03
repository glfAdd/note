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