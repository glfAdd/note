// 引入次文件之前需引入'/static/js/clipboard.min.js'
// 需要弹窗的元素添加'showAS'class名
$(function() {
    var xdas_info={
        name:'MUA|VIP小助理（月嫂）',//小助理名称
        wx_num:'MUA-VIP666',//微信号
        headimg:'http://avatar.img.xindebaby.com/c50c59229bc67ec5d15881da9a7c4b221544162914.84?imageMogr2/auto-orient',//小助理头像
    };
    var xdas_html='<div class="xdas-layer-box" style="width:100%;height:100vh;position:fixed;left:0;top:0;z-index:999;background:rgba(116,112,108,0.2);display:none;cursor:pointer;"><div class="xdas-layer-main" style="width:6.2rem;height:9.06rem;background:#fff;overflow:hidden;border-radius:0.24rem;box-shadow:0 0.4rem 0.6rem 0 rgba(0,0,0,0.06);position:fixed;left:0;top:0;right:0;bottom:0;margin:auto;"><div class="xdas-rel-box" style="position:relative;padding:1.12rem 0.5rem 0;cursor:pointer;"><img src="/static/img/mobileWeb/yuezi/close.png" style="display:block;width:0.28rem;height:0.28rem;padding:0.48rem 0.48rem 0 0;position:absolute;top:0;right:0;cursor:pointer;" class="xdas-close"><p style="padding:0.32rem;background:#FFF5F4;border-radius:0.16rem;text-align:center;color:#FF8576;font-size:0.26rem;line-height:0.4rem;">添加小助理为好友<br>您的问题小助理都能帮您解决</p><img src="/static/img/mobileWeb/product/shape.png" style="display:block;width:0.4rem;height:0.4rem;margin:0.56rem auto 0.52rem;"><img src="'+xdas_info.headimg+'" style="display:block;width:1.64rem;height:1.64rem;border-radius:50%;margin:0 auto;background:#f5f4f4;"><p style="color:#FF8576;font-size:0.3rem;line-height:0.36rem;padding-top:0.54rem;text-align:center;font-weight:500;">'+xdas_info.name+'</p><p style="color:#FFAFA6;font-size:0.28rem;line-height:0.38rem;padding-top:0.08rem;text-align:center;">复制微信号：'+xdas_info.wx_num+' 并添加</p><div style="height:0.86rem;line-height:0.86rem;text-align:center;color:#fff;font-size:0.28rem;font-weight:500;background:#FF8576;border-radius:0.12rem;cursor:pointer;margin:0.4rem auto;" id="AsCopybtn" data-clipboard-text="'+xdas_info.wx_num+'">复制微信号</div></div></div></div>'
    $('body').append(xdas_html);
    // 禁止弹窗底部内容滚动
    $('.xdas-layer-box').on('touchmove', function(e) {
        e.stopPropagation();
        return false;
    })
    $('body').on('click','.showAs', function(e) {
        $('.xdas-layer-box').fadeIn(300);
        e.stopPropagation();
        return false;
    })
    $('body').on('click','.xdas-rel-box', function(e) {
        e.stopPropagation();
        return false;
    })
    $('body').on('click','.xdas-layer-box,.xdas-close', function(e) {
        $('.xdas-layer-box').fadeOut(300);
        e.stopPropagation();
        return false;
    })
    var clipboardxdas = new ClipboardJS('#AsCopybtn');
    clipboardxdas.on('success', function(e) {
        alert('复制成功！');
    });
    clipboardxdas.on('error', function(e) {
        alert('复制失败,暂不支持该功能，请手动复制！');
    });
})
