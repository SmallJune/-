var user = "xiaoming";
function ItXueyuan(user){
    this.name = "IT学院";
    this.domain = "www.itxueyuan.org";
    this.user = user;
    this.showUser = function(){
      alert(this.user);
    }
}
var zhangsan = new ItXueyuan("zhangsan");
zhangsan.showUser();  // 显示"zhangsan"

var wangming = new ItXueyuan("wangming");
wangming.showUser();  // 显示 wangming