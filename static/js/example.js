var getChildNodes=function(ele){
    var childArr=ele.children,
         childArrTem=new Array();  //  临时数组，用来存储符合条件的节点
    for(var i=0,len=childArr.length;i<len;i++){
        if(childArr[i].nodeType==1){
            childArrTem.push(childArr[i]);  // push() 方法将节点添加到数组尾部
        }
    }
    return childArrTem;
}