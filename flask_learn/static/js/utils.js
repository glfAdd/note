var xindeApi = {}
xindeApi._ajax = function(url, method, data, contentType, callback){
    var request = {
        url: url,
        type: method,
        contentType: contentType,
        data: data,
        success: function(response){
            callback(response)
        },
        error: function(err){
            var r = {
                'status': 1,
                'msg': '网络错误'
            }
            callback(r)
        }
    }
    $.ajax(request)
}

xindeApi.ajax = function(url, method, data, callback){
    var contentType = "application/json"
    xindeApi._ajax(url, method, data, contentType, callback)
}

xindeApi.get = function(url, params, callback){
    xindeApi._ajax(url, 'GET', params, null, callback)
}

xindeApi.postJson = function(url, data, callback){
    var _data = JSON.stringify(data)
    xindeApi.ajax(url, 'POST', _data, callback)
}