/**
 * Created by Administrator on 2017/8/1.
 */
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


$(function () {
	$(document).on('click','.card',function () {
		$(this).css({"-webkit-transition":".5s"});
		$(this).toggleClass('aaaa');
	});

	$('#Free_lectures').on('click' ,function () {
		var r = confirm('使用后，可听课次数将减1，确定使用？');
		if (r == false){
			return;
		}
		var eid = $(this).data("eid")
		$.ajax({
			type: "POST",
			url: "/weike/" + eid + "/use_free_ticket/",
			success: function(data) {
				if(data == "0") {
					alert("当前还没有免费听课机会，赶快邀请好友扫码，提升人气值");
				} else {
					alert('报名成功，小助理开课前2小时会拉您进群～');
					window.location.reload();
				}
			}
		});
		return false;
	});
});
