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

$(document).on('change', 'select', function () {
	var select_val = $('select').val();
	$(".select_con").html(select_val)
	if ($(this).val() == '6') {
		$(".a").css({"opacity": "1"})
	} else {
		$(".a").css({"opacity": "0"})
	}
});

function redirect(elem){
	href = $(elem).find("a").attr("href");
	window.location = href;
}
