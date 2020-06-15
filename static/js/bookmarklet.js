/*
(function () {
    var jquery_version = '3.3.1';
    var site_url='https://fa80c121.ngrok.io/';
    var static_url = site_url + 'static/';
    var min_width = 100;
    var min_height = 100;
    function bookmarklet(msg) {
        //这里是分享图片的代码
        //加载css文件
        var css = jQuery('<link>');
        css.attr({
            rel:'stylesheet',
            type:'text/css',
            href:static_ur + 'css/bookmarklet.css?r='+ Math.floor(Math.random()*9999999999999999)
        });
        jQuery('head').append(css);

        //加载HTML结构
        box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>选择一张照片到书签:</h1><div class="images"></div></div>';
        jQuery('body').append(box_html);

        //关闭事件
        jQuery('#bookmarklet #close').click(function () {
            jQuery('#bookmarklet').remove();
        });

        //寻找页面内所有图片然后显示在新增的HTML结构中
        jQuery.each(jQuery('img[src$="jpg"]'), function(index, image) {
      if (jQuery(image).width() >= min_width && jQuery(image).height() >= min_height)
      {
        image_url = jQuery(image).attr('src');
        jQuery('#bookmarklet .images').append('<a href="#"><img src="'+ image_url +'" /></a>');
      }
    });
}
        /*
        jQuery.each(jQuery('img[src$="jpg"]'),function (index, image) {
            if (jQuery(image).width() >= min_width && jQuery(image).height() >= min_height){
                image_url = jQuery(image).attr('src');
                jQuery('#bookmarklet .images').append('<a href="#"><img src="'+image_url+'"/></a>');
            }
        });
        */

        //打开url图片
/*
        jQuery('#bookmarklet .images a').click(function (e) {
            selected_image = jQuery(this).children('img').attr('src');
            //隐藏书签
            jQuery('#bookmarklet').hide();
            //打开新的窗口来提交图片
            window.open(site_url + 'images/create/?url='+encodeURIComponent(selected_image)+'&title='+encodeURIComponent(jQuery('title').text()),'_blank');
        });
*/
        //点击图片时按照指定URL访问我们的网站

        /*
        jQuery('#bookmarklet .images a').click(function (e) {
            var selected_image = jQuery(this).children('src');
            //　隐藏bookmarklet
            jQuery('#bookmarklet').hide();
            //打开新的窗口来提交图片
            window.open(site_url + 'images/create/?url=' + encodeURIComponent(selected_image)
            + '&title=' + encodeURIComponent(jQuery('title').text()),'_blank');
        });
    };
    */
        /*
    //检查页面是否加载了JQuery,如果没有就进行加载，尝试１５次



    if(typeof window.jQuery !== 'undefined'){
        bookmarklet();
    }
    else{
        var conflict = typeof  window.$ !== 'undefined';
        var script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js';
        document.head.appendChild(script);
        var attempts = 15;
        (function () {
            if(typeof window.jQuery === 'undefined'){
                if(--attempts > 0){
                    window.setTimeout(arguments.callee,250)
                }else{
                    alert('加载jQuery出现错误')
                }
            }else{
                bookmarklet();
            }
        })();
    }
});
*/


(function(){
  var jquery_version = '3.3.1';
  var site_url = 'https://d201033b.ngrok.io/';
  var static_url = site_url + 'static/';
  var min_width = 100;
  var min_height = 100;

  function bookmarklet(msg) {
    // load CSS
    var css = jQuery('<link>');
    css.attr({
      rel: 'stylesheet',
      type: 'text/css',
      href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random()*99999999999999999999)
    });
    jQuery('head').append(css);

    // load HTML
    box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>选择一张图片分享到书签:</h1><div class="images"></div></div>';
    jQuery('body').append(box_html);

    // close event
    jQuery('#bookmarklet #close').click(function(){
       jQuery('#bookmarklet').remove();
    });

    // find images and display them
    jQuery.each(jQuery('img[src$="jpg"]'), function(index, image) {
      if (jQuery(image).width() >= min_width && jQuery(image).height() >= min_height)
      {
        image_url = jQuery(image).attr('src');
        jQuery('#bookmarklet .images').append('<a href="#"><img src="'+ image_url +'" /></a>');
      }
    });

    // when an image is selected open URL with it
    jQuery('#bookmarklet .images a').click(function(e){
      selected_image = jQuery(this).children('img').attr('src');
      // hide bookmarklet
      jQuery('#bookmarklet').hide();
      // open new window to submit the image
      window.open(site_url +'images/create/?url='
                  + encodeURIComponent(selected_image)
                  + '&title='
                  + encodeURIComponent(jQuery('title').text()),
                  '_blank');
    });
  }

  // Check if jQuery is loaded
  if(typeof window.jQuery != 'undefined') {
    bookmarklet();
  } else {
    // Check for conflicts
    var conflict = typeof window.$ != 'undefined';
    // Create the script and point to Google API
    var script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js';
    // Add the script to the 'head' for processing
    document.head.appendChild(script);
    // Create a way to wait until script loading
    var attempts = 15;
    (function(){
      // Check again if jQuery is undefined
      if(typeof window.jQuery == 'undefined') {
        if(--attempts > 0) {
          // Calls himself in a few milliseconds
          window.setTimeout(arguments.callee, 250)
        } else {
          // Too much attempts to load, send error
          alert('An error ocurred while loading jQuery')
        }
      } else {
          bookmarklet();
      }
    })();
  }
})();