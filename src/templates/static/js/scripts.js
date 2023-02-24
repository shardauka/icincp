(function($) {
    var allfunction = {
        // sticky menu js code here
        sticky_menu: function() {
            $(window).on("scroll", function() {
                var $this = ".header-area";
                var scrollDistance = $(window).scrollTop();
                var topOffset = $($this).position().top + 150;
                var showSticky = $($this).position().top + 500;
                if (topOffset <= scrollDistance) {
                    $($this).addClass("sticky");
                } else if (showSticky <= scrollDistance) {
                    $($this).addClass("show-sticky");
                } else {
                    $($this).removeClass("sticky show-sticky");
                }
            });
        },
        // MainMenu funstions
        mainmenu: () => {
            $('.main-navbar ul li').each(function() {
                if ($(this).children('ul').length) {
                    $(this).children('a').append('<i class= "icofont-thin-down icon-hidden-md"></i><div class="drop-icon"><span class="icofont-minus"></span><span class="icofont-plus"></span></div>');
                } else if ($(this).children('div').length) {
                    $(this).children('a').append('<i class= "icofont-thin-down icon-hidden-md"></i><div class="drop-icon"><span class="icofont-minus"></span><span class="icofont-plus"></span></div>');
                }

            })
            $('.main-navbar ul li').click(function(e) {
                e.stopPropagation();
                $(this).children('a').next().toggleClass('active');
                $(this).children('a').toggleClass('active');
                $(this).siblings('li').children('a').next().removeClass('active');
                $(this).siblings('li').children('a').removeClass('active');
            })
        },
        // features mouse event jQuery here
        featureEvent: function() {
            $(".feature-card-animate")
                .mouseover(function() {
                    $(this).children().removeClass("active");
                })
                .mouseout(function() {
                    $(this).children().addClass("active");
                });
        },
        // form click js here
        form_click: function() {
            $(".animation-form").on("click", function(e) {
                e.stopPropagation();
                $(this).addClass("active").siblings().removeClass("active");
                $(this)
                    .parents(".subscribe-input")
                    .addClass("active")
                    .siblings()
                    .removeClass("active");
            });
        },
        cart_close: function() {
            $(".card-close").on("click", function() {
                $(this).parents('tr').addClass("active");
            });
        },
        //case_study  Owl Carousel
        case_study_slick: function() {
            var $cs_carousel = $(".cs-carosoul");
            if ($cs_carousel.length) {
                $cs_carousel.owlCarousel({
                    resonsiveClass: true,
                });
                $(".am-next").click(function() {
                    $cs_carousel.trigger("next.owl.carousel");
                });
                $(".am-prev").click(function() {
                    $cs_carousel.trigger("prev.owl.carousel", [300]);
                });
            }
        },
        //clients  Owl Carousel
        clients_owl: function() {
            if ($('.clients-owl-area').length) {
                var $cl_carousel = $(".clients-owl-area");
                $(".co-next").click(function() {
                    $cl_carousel.trigger("next.owl.carousel");
                });
                $(".co-prev").click(function() {
                    $cl_carousel.trigger("prev.owl.carousel", [300]);
                });
            }

            var $ct_carousel = $(".blog-owl");
            if ($ct_carousel.length) {
                $(".blog-next").click(function() {
                    $ct_carousel.trigger("next.owl.carousel");
                });
                $(".blog-prev").click(function() {
                    $ct_carousel.trigger("prev.owl.carousel", [300]);
                });
            }

        },
        //pricing monthly yearly function here
        pricing_click: function() {
            $(".yearly-btn").on("click", function() {
                $(this).addClass("active");
                $(this).siblings().removeClass("active");
                $(".pre-parent").addClass("show-year");
                $(".pre-parent").removeClass("show-month");
            });
            $(".monthly-btn").on("click", function() {
                $(this).addClass("active");
                $(this).siblings().removeClass("active");
                $(".pre-parent").removeClass("show-year");
                $(".pre-parent").addClass("show-month");
            });
        },
        //home 2 all function start here
        home_two_logo_slick: function() {
            $(".h2-logo-slick").slick({
                dots: false,
                infinite: true,
                speed: 300,
                slidesToShow: 5,
                slidesToScroll: 1,
                autoplay: true,
                centerMode: true,
                arrows: false,
                responsive: [{
                        breakpoint: 1024,
                        settings: {
                            slidesToShow: 3,
                            slidesToScroll: 1,
                            infinite: true,
                            dots: false,
                        },
                    },
                    {
                        breakpoint: 767,
                        settings: {
                            slidesToShow: 2,
                            slidesToScroll: 1,
                        },
                    },
                    {
                        breakpoint: 580,
                        settings: {
                            slidesToShow: 1,
                            slidesToScroll: 1,
                        },
                    }
                ],
            });
        },
        //case_study  Owl Carousel
        home_two_study_slick: function() {
            var $cs_carousel = $(".h2-cs-carosoul");
            if ($cs_carousel.length) {
                $(".am-next").click(function() {
                    $cs_carousel.trigger("next.owl.carousel");
                });
                $(".am-prev").click(function() {
                    $cs_carousel.trigger("prev.owl.carousel", [300]);
                });
            }
        },
        //clients  Owl Carousel
        home_two_pricing: function() {
            var $swip_class = $(".pricing-container , .h4-client-container");
            if ($swip_class.length) {
                var swiper = new Swiper(".pricing-container, .h4-client-container", {
                    grabCursor: false,
                    centeredSlides: true,
                    freeMode: true,
                    slidesPerView: "auto",
                    effect: "coverflow",
                    coverflowEffect: {
                        rotate: 20,
                        stretch: 50,
                        depth: 50,
                        modifier: 1,
                        slideShadows: false,
                    },
                    breakpoints: {
                        992: {
                            initialSlide: 1
                        },
                    },
                });
            }
            //yearly  click function
            $(".h2-yearly").on("click", function() {
                $(this).addClass("active");
                $(this).siblings().removeClass("active");
                $(".year-comon-two").addClass("active");
            });
            //yearly  click function
            $(".h2-monthly").on("click", function() {
                $(this).addClass("active");
                $(this).siblings().removeClass("active");
                $(".year-comon-two").removeClass("active");
            });
        },
        //home3 script here
        home_two_slider: function() {
            $(".clip-slide-nav li").click(function() {
                var $this = $(this);
                var index = $this.index();
                var slider = $this
                    .parents()
                    .next(".clip-banner-slider-wrapper")
                    .children();
                slider
                    .eq(index)
                    .addClass("active")
                    .css({
                        zIndex: 99,
                    })
                    .siblings()
                    .css({
                        zIndex: -99,
                    });
                $this.addClass("active");
                setTimeout(() => {
                    slider.eq(index).siblings().removeClass("active");
                    $this.siblings().removeClass("active");
                }, 00);
                setTimeout(() => {
                    if (index === 2) {
                        $("body").addClass("slide-3");
                    } else {
                        $("body").removeClass("slide-3");
                    }
                }, 500);
            });
        },
        // h3-counter js  function here
        home_three_counter: function() {
            var $counter_class = $(".h3-counter-area , .seo-counter");
            if ($counter_class.length) {
                $(".h3-counter-area , .seo-counter").waypoint(
                    function() {
                        $(".h2-cn1").CountUpCircle({
                            duration: 500,
                            opacity_anim: false,
                            step_divider: 100,
                        });
                        $(".h2-cn2").CountUpCircle({
                            duration: 2500,
                            opacity_anim: false,
                            step_divider: 100,
                        });
                        $(".h2-cn3").CountUpCircle({
                            duration: 500,
                            opacity_anim: false,
                            step_divider: 100,
                        });
                        $(".h2-cn4").CountUpCircle({
                            duration: 1500,
                            opacity_anim: false,
                            step_divider: 100,
                        });
                    }, { offset: "90%" }
                );
            }
        },
        // //clients  Owl Carousel
        home_three_pricing: function() {
            $(".h3-pricing-tab .h2-yearly").on("click", function() {
                $(this).parent().addClass("active");
            });
            $(".h3-pricing-tab .h2-monthly").on("click", function() {
                $(this).parent().removeClass("active");
            });
        },
        // h4 all js here
        // h4-counter js  function here
        h4_counter: function() {
            var $counter = $(".h4-grouth-area");
            if ($counter.length) {
                $(".h4-grouth-area").waypoint(
                    function() {
                        $(".h4-cnt1").CountUpCircle({
                            duration: 3000,
                            opacity_anim: false,
                            step_divider: 20,
                        });
                        $(".h4-cnt2").CountUpCircle({
                            duration: 3000,
                            opacity_anim: false,
                            step_divider: 20,
                        });
                    }, { offset: "60%" }
                );
            }
        },
        //clients  Owl Carousel
        home_four_client: function() {
            var $client_swip = $('.h4-client-container')
            if ($client_swip.length) {
                var swiper = new Swiper(".h4-client-container", {
                    grabCursor: false,
                    centeredSlides: true,
                    freeMode: false,
                    initialSlide: 1,
                    slidesPerView: "auto",
                    effect: "coverflow",
                    autoplay: false,
                    loop: false,
                    coverflowEffect: {
                        rotate: 15,
                        stretch: 80,
                        depth: 50,
                        modifier: 1,
                        slideShadows: false,
                    },
                    breakpoints: {
                        768: {
                            coverflowEffect: {
                                rotate: 20,
                                stretch: 0,
                                depth: 0,
                                modifier: 1,
                                slideShadows: false,
                            },
                        },
                    },
                });
            }
        },
        blog_mesonry: () => {
            if ($('.mesonry').length) {
                var $grid = $('.mesonry').isotope({
                    itemSelector: '.mesonry-item',
                    percentPosition: true,
                    masonry: {
                        columnWidth: 1
                    }
                });
                $grid.imagesLoaded().progress(function() {
                    $grid.isotope('layout')
                });
                // filter items on button click
                $('.isotope-menu').on('click', 'li', function() {
                    var filterValue = $(this).attr('data-filter');
                    $grid.isotope({ filter: filterValue });
                });
            }
        },
        isotopActivation: () => {
            if ($('.isotop-grid').length) {
                var $grid = $('.isotop-grid').isotope({
                    // options
                    itemSelector: '.isotope-item',
                    layoutMode: 'fitRows'
                });
                // layout Isotope after each image loads
                $grid.imagesLoaded().progress(function() {
                    $grid.isotope('layout');
                });
                // filter items on button click
                $('.isotope-menu').on('click', 'li', function() {
                    var filterValue = $(this).attr('data-filter');
                    $grid.isotope({ filter: filterValue });
                    $(this).addClass('active');
                    $(this).siblings('li').removeClass('active');
                });
            }
        },
        // StopPropagations elements
        stopPropagationElements: () => {
            $(".animation-form").click(function(e) {
                e.stopPropagation();
            });
        },

        // Document click to hide elements
        elementHide: () => {
            $(document).click(function() {
                $(".animation-form").removeClass("active");
                $(".subscribe-input").removeClass("active");
                $(".mega-menu a , .mega-dropdawn , .main-navbar ul li a , .dropdawn").removeClass("active");
            });
        },
        // IMG to SVG
        imgToSvg: function() {
            function jetix_svg() {
                jQuery('img').each(function() {
                    var jQueryimg = jQuery(this);
                    var imgClass = jQueryimg.attr('class');
                    var imgURL = jQueryimg.attr('src');
                    jQuery.get(imgURL, function(data) {
                        // Get the SVG tag, ignore the rest
                        var jQuerysvg = jQuery(data).find('svg');

                        // Add replaced image's classes to the new SVG
                        if (typeof imgClass !== 'undefined') {
                            jQuerysvg = jQuerysvg.attr('class', imgClass + ' replaced-svg');
                        }
                        jQuerysvg = jQuerysvg.removeAttr('xmlns:a');
                        // Replace image with new SVG
                        jQueryimg.replaceWith(jQuerysvg);

                    }, 'xml');

                });
            }
            $(document).each(function() {
                jetix_svg();
            })
        },
        //counter plugin code
        counter_up: function() {
            if ($('.counter-area').length) {
                $(".counter-area").waypoint(
                    function() {
                        $(".counter1").CountUpCircle({
                            duration: 10,
                            opacity_anim: false,
                            step_divider: 10,
                        });
                        $(".counter2").CountUpCircle({
                            duration: 10,
                            opacity_anim: false,
                            step_divider: 10,
                        });
                        $(".counter3").CountUpCircle({
                            duration: 10,
                            opacity_anim: false,
                            step_divider: 10,
                        });
                        $(".counter4").CountUpCircle({
                            duration: 10,
                            opacity_anim: false,
                            step_divider: 10,
                        });
                    }, { offset: "90%" }
                );
            }
        },
        select: () => {
            if ($('select').length) {
                $('select').niceSelect();
            }
        },

        home_two_counters: function() {
            if ($('.counter').length) {
                $(".counter").waypoint(
                    function() {
                        $(".h2-cn1").CountUpCircle({
                            duration: 1000,
                            opacity_anim: false,
                            step_divider: 100,
                        });
                        $(".h2-cn2").CountUpCircle({
                            duration: 1000,
                            opacity_anim: false,
                            step_divider: 100,
                        });
                        $(".h2-cn3").CountUpCircle({
                            duration: 1000,
                            opacity_anim: false,
                            step_divider: 100,
                        });
                        $(".h2-cn4").CountUpCircle({
                            duration: 1000,
                            opacity_anim: false,
                            step_divider: 100,
                        });
                    }, { offset: "90%" }
                );
            }
        },
        niceScrollBar: () => {
            var scrollBarColor = $('body').data('scrollbar');
            $("body").niceScroll({
                cursorcolor: scrollBarColor,
                cursorwidth: "5px",
                cursorborder: "0px solid #fff",
            });
        },
        spinner: () => {
            if ($('#spinner, #spinner2').length) {
                function spinner() {
                    $("#spinner, #spinner2").spinner();
                    $('#spinner, #spinner2').keyup(function() {
                        this.value = this.value.replace(/[^0-9]/g, '');
                    });
                }

                function maxLengthCheck(object) {
                    if (object.value.length > object.maxLength)
                        object.value = object.value.slice(0, object.maxLength)
                }
                window.onload = spinner;
            }
        },
        ui_crad: () => {
            if ($('#slider-container').length) {
                $('#slider-container').slider({
                    range: true,
                    min: 0,
                    max: 20,
                    values: [0, 20],
                    create: function() {
                        $("#amount").val("$0 - $20");
                    },
                    slide: function(event, ui) {
                        $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
                        var mi = ui.values[0];
                        var mx = ui.values[1];
                        filterSystem(mi, mx);
                    }
                })

                function filterSystem(minPrice, maxPrice) {
                    $(".filter-wrapper div.filter-data").hide().filter(function() {
                        var price = parseInt($(this).data("price"), 10);
                        return price >= minPrice && price <= maxPrice;
                    }).show();
                }

            }
        },
        elevated_zoom: () => {
            if ($('#elevate-img').length) {
                $('#elevate-img').elevateZoom({
                    zoomType: "inner",
                    cursor: "crosshair",
                    zoomWindowFadeIn: 500,
                    zoomWindowFadeOut: 750,
                    easing: true
                });
            }
        },
        video_popup: () => {
            if ($('#exampleImage , #home-three-video').length) {
                // Video popup
                const videoPopup = () => {
                    var a = $("#exampleImage , #home-three-video");
                    var configObject = {
                        sourceUrl: a.attr("data-videourl"),
                        triggerElement: "#" + a.attr("id"),
                        progressCallback: function() {}
                    };

                    var videoBuild = new YoutubeOverlayModule(configObject);
                    videoBuild.activateDeployment();
                };
                videoPopup()
            }
        },
        parallax: () => {
            if ($('.paralax-img').length) {
                var image = document.getElementsByClassName('paralax-img');
                new simpleParallax(image, {
                    delay: .6,
                    transition: 'cubic-bezier(0,0,0,1)'
                });
            }
        },
        init: function() {
            allfunction.imgToSvg();
            allfunction.stopPropagationElements();
            allfunction.elementHide();
            allfunction.sticky_menu();
            allfunction.mainmenu();
            allfunction.featureEvent();
            allfunction.form_click();
            allfunction.cart_close();
            allfunction.case_study_slick();
            allfunction.clients_owl();
            allfunction.pricing_click();
            allfunction.home_two_study_slick();
            allfunction.home_two_pricing();
            allfunction.home_two_slider();
            allfunction.home_three_counter();
            allfunction.home_three_pricing();
            allfunction.home_four_client();
            allfunction.counter_up();
            allfunction.home_two_counters();
            allfunction.h4_counter();
            allfunction.select();
            allfunction.isotopActivation();
            allfunction.blog_mesonry();
            allfunction.home_two_logo_slick();
            allfunction.niceScrollBar();
            allfunction.spinner();
            allfunction.ui_crad();
            allfunction.elevated_zoom();
            allfunction.video_popup();
            allfunction.parallax();
        },
    };

    $(document).ready(function() {
        allfunction.init();
    });
})(jQuery);
//loder js code
$(window).load(function() {
    $('.loader-wrapper').addClass('hide');
    $('body').removeClass('placeholder')
});

// responsive menu design
const navSlide = () => {
    const bar = document.querySelector(".animate-bar");
    const nav = document.querySelector(".pupko-menu");
    const body = document.querySelector("body");
    const header = document.querySelector(".header-area");

    bar.addEventListener("click", () => {
        bar.classList.toggle("active");
        body.classList.toggle('show-mobile-nav')
        nav.classList.toggle("active-nav");
    });
};
const app = () => {
    navSlide();
};
app();