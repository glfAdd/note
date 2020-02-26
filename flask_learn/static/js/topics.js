/**
 * Created by Administrator on 2017/8/1.
 */

var come = false;
var topic = false;

(function (doc, win) {
	var docEl = doc.documentElement,
		resizeEvt = 'orientationchange' in window ? 'orientationchange' : 'resize',
		recalc = function () {
			var clientWidth = docEl.clientWidth;
			if (!clientWidth) return;
			docEl.style.fontSize = 20 * (clientWidth / 320) + 'px';
		};

	if (!doc.addEventListener) return;
	win.addEventListener(resizeEvt, recalc, false);
	doc.addEventListener('DOMContentLoaded', recalc, false);
})(document, window);

$(document).on('change','select',function(){
	if ($(this).val() == '99') {
		$("#where").val("");
		come = false;
		$(".a").css({"display": "block"})
	} else {
		if ($(this).val() == '0') {
			come = false;
			return;
		}
		come = true;
		$(".a").css({"display": "none"})
	}
})

function textChange(){
	var objS = document.getElementById("come-from");
	var text = objS.options[objS.selectedIndex].innerHTML;
	$("#select").html(text);
}

function check(){
	if($("#where").val() != ""){
		come = true;
	} else {
		come = false;
	}
}

// 复选框
function check_click(elem){
	var flag = $(elem).find(".form_check")[0].checked;
	$(elem).find(".form_check")[0].checked = !flag;
	if($("input:checked").length > 0){
		topic = true;
	} else {
		topic = false;
	}
}

function submit_check(){
	if(!come){
		alert("请选择您从哪知道的公众号");
		return false;
	}
	if(!topic){
		alert("请选择您感兴趣的话题");
		return false;
	}
	return true;
}
