require(["../js/mmRouter", "../js/mmRequest"], function(Router){
//    var data = {
//        list: [
//            {
//                title: '<油价>调整周期缩至10个工作日 无4%幅度限制',
//                url: 'http://finance.qq.com/zt2013/2013yj/index.htm'
//            },
//            {
//                title: '明起汽油价格每吨下调310元 单价回归7元时代',
//                url: 'http://finance.qq.com/a/20130326/007060.htm'
//            },
//            {
//                title: '广东副县长疑因抛弃情妇遭6女子围殴 纪检调查',
//                url: 'http://news.qq.com/a/20130326/001254.htm'
//            },
//            {
//                title: '湖南27岁副县长回应质疑：父亲已不是领导',
//                url: 'http://news.qq.com/a/20130326/000959.htm'
//            },
//            {
//                title: '朝军进入战斗工作状态 称随时准备导弹攻击美国',
//                url: 'http://news.qq.com/a/20130326/001307.htm'
//            }
//        ]
//    };

    var api = {
        work: '/article/3/',
        jobs: '/jobs',
        culture: '/article/2',
        article_list: '/article/',
        article:'/article/info/',
        job_detail: '/jobs/info/',
    };

    var model = avalon.define({
        $id:'home',
        current_menu:'about',
        down_menu: function(e){
            console.log(e);
        }
    });
      /*==============================================*/
     /*                   相原UI                      */
    /*==============================================*/
    var OriginUi = {
        down_menu : function(){
            var timer = null;
            $('.down_menu').mouseenter(function(e){
                clearTimeout(timer);
                timer = null;
                var $dom = $(e.currentTarget);
                    $dom.next('.down_box').fadeIn();
            });
            $('.down_menu').mouseleave(function(e){
                var $dom = $(e.currentTarget),
                    $dropUl = $dom.next('.down_box');
                timer = setTimeout(function() {
                    $dropUl.fadeOut();
                }, 1000);
            });
        },
        init: function(){
            this.down_menu();
            console.log(this);
        }
    };
    OriginUi.init();

      /*===============================================*/
     /*                  相原文章列表页                 */
    /*==============================================*/
    avalon.router.get("/article_list/:bclass/:subclass/:page",  function(bclass,subclass,page) {
        require(['../html/build/article_list'], function (article_list) {
            document.getElementById('_content').innerHTML = article_list();
            var articlelist_model = avalon.define({
                    $id:'article_list',
                    name:"文章列表",
                    articlelist: [],
                    next:"",
                    page:"",
                    article_type:"",
                    sub_type:"sub_type",
                    test: function(e){
                        console.log(e);
                    }
            });
            var url =api.article_list+bclass+'/'+subclass+'/'+page;
            avalon.log(url);
            var init_articlelist = function(){
                avalon.ajax({
                    type: "get",
                    url: url,
                    success: function(data){
                        articlelist_model.articlelist = data;
                        articlelist_model.next=data[0]['next'];
                        articlelist_model.page=data[0]['page'];
                        articlelist_model.article_type=page=data[0]['article_type'];
                        articlelist_model.sub_type=page=data[0]['sub_type'];
                    },
                    dataType: 'json'
                });
            };
            avalon.log(articlelist_model.articlelist);
            avalon.scan();
            init_articlelist();
        });
    });

      /*===============================================*/
     /*                  相原文章                      */
    /*==============================================*/
     avalon.router.get("/article/:article_id",  function(article_id) {
        require(['../html/build/article'], function (article) {
            document.getElementById('_content').innerHTML = article();
            var article_model = avalon.define({
                    $id:'article',
                    article: [],
                    test: function(e){
                        console.log(e);
                    }
            });
            var url =api.article+article_id;
            avalon.log(url);
            var init_article = function(){
                avalon.ajax({
                    type: "get",
                    url: url,
                    success: function(data){
                        article_model.article = data[0]["article_attachment"];
                        $('#sildes').olvSlides(
                            {
                                thumb:true,
                                thumbPage:true,
                                thumbDirection:"Y",
                                effect:'fade'
                            }
                        );
                    },
                    dataType: 'json'
                });
            };
            avalon.scan();
            init_article();
        });
    });

     /*===============================================*/
     /*                  相原文章单页                  */
    /*==============================================*/
     avalon.router.get("/article_single/:article_id",  function(article_id) {
        require(['../html/build/article_single'], function (article) {
            document.getElementById('_content').innerHTML = article();
            var article_model = avalon.define({
                    $id:'article',
                    article_type_id:"",
                    sub_type:"",
                    article: [],
                    test: function(e){
                        console.log(e);
                    }
            });
            var url =api.article+article_id;
            avalon.log(url);
            var init_article = function(){
                avalon.ajax({
                    type: "get",
                    url: url,
                    success: function(data){
                        article_model.article = data[0]['article_attachment'];
                        article_model.article_type_id = data[0]['article_type_id'];
                        article_model.sub_type=data[0]['sub_type'];
                        $('#sildes').olvSlides(
                            {
                                thumb:true,
                                thumbPage:true,
                                thumbDirection:"Y",
                                effect:'fade'
                            }
                        );
                    },
                    dataType: 'json'
                });
            };
            avalon.scan();
            init_article();
        });
    });

      /*===============================================*/
     /*                  相原一张图片一段文字效果        */
    /*==============================================*/
    avalon.router.get("/article_loop/:bclass/:subclass",  function(bclass,subclass) {
        require(['../html/build/list'], function (list) {
            document.getElementById('_content').innerHTML = list();
            var article_model = avalon.define({
                    $id:'article',
                    articlelist: [],
                    test: function(e){
                        console.log(e);
                    }
            });
            var url =api.article_list+bclass+'/'+subclass;
            avalon.log(url);
            var init_article = function(){
                avalon.ajax({
                    type: "get",
                    url: url,
                    success: function(data){
                        article_model.articlelist = data;
                        $('.flexslider').flexslider({
                            animation: 'fade',
                            controlsContainer: '.flexslider'});
                    },
                    dataType: 'json'
                });
            };
            avalon.scan();
            init_article();
        });

    });

      /*==============================================*/
     /*                   相原文化                    */
    /*==============================================*/
    avalon.router.get("/culture/:culture",  function(a) {

        require(['../html/build/article'], function (tpl) {
            document.getElementById('_content').innerHTML = tpl(article);
        });

    });

      /*==============================================*/
     /*                   相原作品                    */
    /*==============================================*/
    avalon.router.get("/work",  function() {
        require(['../html/build/news'], function (footer) {
            document.getElementById('_content').innerHTML = footer();
        });
        model.current_menu = 'work';
    });

 
      /*==============================================*/
     /*                   相原招聘详情                 */
    /*==============================================*/
    avalon.router.get("/job_detail/:job_id/",  function(job_id) {
        // require(['text!../html/jobs.html'], function (tpl) {
        require(['../html/build/job_detail'], function (job_detail) {
            document.getElementById('_content').innerHTML = job_detail();
            var job_model = avalon.define({
                    $id:'job',
                    name: "相原杭州总部～",
                    job_data: [],
                    job:"",
                    number:"",
                    gender:"",
                    education:"",
                    major:"",
                    description:"",
                    demand:"",
                    test: function(e){
                        console.log(e);
                    }
                });
            var url = api.job_detail+job_id;
            avalon.log(url);
            var init_jobs = function(){
                avalon.ajax({
                    type: "get",
                    url: url,
                    success: function(data){
                        job_model.job_data = data;
                        job_model.job = data[0]['jobs'];
                        job_model.number = data[0]['number'];
                        job_model.gender = data[0]['gender'];
                        job_model.education = data[0]['education'];
                        job_model.major = data[0]['education'];
                        job_model.description=data[0]['description'];
                        job_model.demand=data[0]['demand'];
                    },
                    dataType: 'json'
                 });
            };
            avalon.log(job_model.pp);
            avalon.scan();
            init_jobs();
        });
    });

      /*==============================================*/
     /*                   联系我们                    */
    /*==============================================*/
    avalon.router.get("/contact",  function() {
        require(['../html/build/contact'], function (contact) {
            document.getElementById('_content').innerHTML = contact();
        });
    });


      /*==============================================*/
     /*                   相原招聘                    */
    /*==============================================*/
    avalon.router.get("/jobs/{sub_type}/",  function() {
        sub_type = this.params['sub_type'];
        // console.log(sub_type)
        require(['../html/build/jobs'], function (jobs) {
            document.getElementById('_content').innerHTML = jobs();
            var job_model = avalon.define({
                    $id:'jobs',
                    boolvalue:{
                        theory: false,
                        campus: false,
                        social: false,
                    },
                    name: "相原杭州总部～",
                    jobList: [],
                    // testClick: function(){
                        // console.log('job_model.bool_social')
                        // require(['../html/bulid/jobs_info'], function(jobs_info){
                            // job_model.bool_social = true;
                            // document.getElementById('_content').innerHTML = jobs_info(data)
                            // alert("猪猪住");
                        // });
                    // }
                });

            var init_jobs = function(){
                job_model.boolvalue[sub_type] = true;
                // console.log(job_model.boolvalue.campus)
                avalon.ajax({
                    type: "get",
                    url: api.jobs,
                    success: function(data){
                        job_model.jobList = data;
                        $(document).ready( function () {
                        $('#table_id').DataTable();
                         } );
                               },
                    dataType: 'json'
                 });
            };
            avalon.scan();
            init_jobs();
        });
    });


 
      /*==============================================*/
     /*                   下载中心                    */
    /*==============================================*/
    avalon.router.get("/download/{sub_type}/",  function() {
        sub_type = this.params['sub_type']
        require(['../html/build/download'], function (download) {
            var init_download = function(){
                avalon.ajax({
                    type: "get",
                    url: api.download + sub_type,
                    success: function(data){
                        file_model.fileList = data;
                    },
                    dataType: 'json'
                });
            };

            document.getElementById('_content').innerHTML = download();

            var file_model = avalon.define({
                $id: 'download',
                fileList: []
            });
            avalon.scan();
            init_download();
        });
    });

    avalon.history.start({
        basepath: "/"
    });
    avalon.scan();

});