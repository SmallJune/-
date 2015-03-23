/**
 * Created by zgh on 15-3-10.
 */
define(function(require, exports, module) {

    module.exports={
        click: function(){
        document.getElementById("demo").onclick=function(e){
        var e=e||event;
        alert(e.screenX);}
    }
}})