function bindCaptchaBtnClick(){
    $("#captcha-btn").on("click",function(event){
        var email = $("input[name='email']").val();         //获取输入框中的值
        if(!email){
            alert("请先输入邮箱！");
        }
    });
}


//等网页文档所有元素都加载完成后再执行
$(function () {
    bindCaptchaBtnClick();
});