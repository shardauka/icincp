// mouse event jquery start
var windowWidth = $(window).width();

$(".traffic-area").mousemove(function(event) {
    var moveX = ($(window).width() / 2 - event.pageX) * 0.04;
    var moveY = ($(window).height() / 2 - event.pageY) * 0.03;
    $(".tf-c1").css("margin-left", -moveX + "px");
    $(".tf-c1").css("margin-top", moveY + "px");
    $(".tf-c2").css("margin-right", moveX + "px");
    $(".tf-c2").css("margin-top", moveY + "px");
    $(".tf-m1").css("margin-right", moveX + "px");
    $(".tf-m1").css("margin-top", moveY + "px");
    $(".tf-m2").css("margin-left", -moveX + "px");
    $(".tf-m2").css("margin-top", moveY + "px");
});
$(".moving-banner-area").mousemove(function(event) {
    var moveX = ($(window).width() / 2 - event.pageX) * 0.03;
    var moveY = ($(window).height() / 2 - event.pageY) * 0.03;
    $(".move-x").css("margin-left", -moveX + "px");
    $(".move-x").css("margin-top", moveY + "px");
    $(".moving-cloud").css("margin-left", -moveX + "px");
    $(".moving-cloud").css("margin-top", moveY + "px");
    $(".moving-small-cloud").css("margin-left", -moveX + "px");
    $(".moving-small-cloud").css("margin-top", moveY + "px");
    $(".moving-banner-img").css("margin-right", moveX + "px");
    $(".moving-banner-img").css("margin-top", moveY + "px");
});

// mouse event jquery end

(function($) {
    var allfunction = {
        // btn shatter js code
        btnShatter: function() {
            $(".btn-animate")
                .mouseover(function() {
                    $(this).removeClass("active");
                })
                .mouseout(function() {
                    $(this).addClass("active");
                });
        },
        iconShatter: function() {
            $(".icon-animation, .icon-animation-melon")
                .mouseover(function() {
                    $(this).removeClass("active");
                })
                .mouseout(function() {
                    $(this).addClass("active");
                });
        },
        // StopPropagations elements
        stopPropagationElements: () => {
            $(".dropdawn").click(function(e) {
                e.stopPropagation();
            });
            $(".mega-menu").click(function(e) {
                e.stopPropagation();
            });
        },
        // Document click to hide elements
        elementHide: () => {
            $(document).click(function() {
                $(".dropdawn").children("ul").removeClass("active");
                $(".dropdawn a").removeClass("active");
                $(".mega-menu").children(".mega-dropdawn").removeClass("active");
                $(".mega-menu a").removeClass("active");
            });
        },
        init: function() {
            allfunction.stopPropagationElements();
            allfunction.elementHide();
            // allfunction.btnShatter();
            allfunction.iconShatter();
        },
    };
    $(document).ready(function() {
        allfunction.init();
    });
})(jQuery);