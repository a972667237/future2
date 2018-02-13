/**
 * Created by wueiz on 2018/2/7.
 */
var search = function() {
    let key = document.getElementsByName('search')[0].value || '移动';
    let t = document.getElementsByName('now_type')[0].value;
    if (key) {
        if(t){
            window.location.href = "/search?keyword=" + key + "&type=" + t;
        }
       window.location.href = "/search?keyword=" + key;
    }
}

var pageJump = function() {
    let page = document.getElementsByName('page')[0].value || 1;
    let t = document.getElementsByName('now_type')[0].value || 1;
    let searchKeyword = document.getElementsByName('searchKeyword')[0].value || 0;
    let innerKeyword = document.getElementsByName('innerKeyword')[0].value || 0;
    if (searchKeyword != 0){
        if (page) {
            window.location.href = "/search?keyword=" + searchKeyword + "&page=" + page + "&type=" + t;
        }
    }
    else if (t) {
        if (page) {
            if(innerKeyword){
                window.location.href = "/list?type=" + t + "&page=" + page + "&keyword=" + innerKeyword;
            }
            else{
                window.location.href = "/list?type=" + t + "&page=" + page;
            }

        }
    }
}

document.getElementById("page_jump_icon").onclick = pageJump
document.getElementById("keyword_search").onclick = search
document.getElementsByName('search')[0].onkeyup = function(e) {
    var code = e.charCode || e.keyCode;
    if (code == 13) {
        search();
    }
}
document.getElementsByName('page')[0].onkeyup = function(e) {
    var code = e.charCode || e.keyCode;
    if (code == 13) {
        pageJump();
    }
}