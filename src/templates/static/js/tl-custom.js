
(function($) {
    var scrollfunction = {
        // //home 4 animation  scroll magic
        we_are_scrollmagic: function() {
            var Controller = new ScrollMagic.Controller();
            $(".we-are-img").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: this,
                        triggerHook: 0.6,
                    })
                    .setClassToggle(this, "active")
                    // .addIndicators({
                    //   colorTrigger: "black",
                    //   colorStart: "red",
                    // })
                    .reverse(false)
                    .addTo(Controller);
            });
        },
        we_are_bg_scrollmagic: function() {
            var Controller = new ScrollMagic.Controller();
            $(".we-are-bg").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: this,
                        triggerHook: 0.3,
                    })
                    .setClassToggle(this, "active")
                    .reverse(false)
                    .addTo(Controller);
            });
        },
        // homepage three scroll magic
        WebsiteTraffic: function() {
            var Controller = new ScrollMagic.Controller();
            $(".h3-about-img-part").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: this,
                        triggerHook: 0.5,
                    })
                    .setClassToggle(this, "active")
                    // .addIndicators({
                    //   colorTrigger: "black",
                    //   colorStart: "red",
                    // })
                    .reverse(false)
                    .addTo(Controller);
            });
        },
        way_to_feture: function() {
            var Controller = new ScrollMagic.Controller();
            $(".way-to-feture, .ppc-advertising-img-wrapper").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: this,
                        triggerHook: 0.3,
                    })
                    .setClassToggle(this, "active")
                    // .addIndicators({
                    //   colorTrigger: "black",
                    //   colorStart: "red",
                    // })
                    .reverse(false)
                    .addTo(Controller);
            });
        },
        ppc_advertising_img: function() {
            var Controller = new ScrollMagic.Controller();
            $(".ppc-advertising-img-wrapper, .degital-marketing-area").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: this,
                        triggerHook: 1,
                    })
                    .setClassToggle(this, "active")
                    // .addIndicators({
                    //   colorTrigger: "black",
                    //   colorStart: "red",
                    // })
                    .reverse(false)
                    .addTo(Controller);
            });
        },
        seo_trendImg: function() {
            var Controller = new ScrollMagic.Controller();
            $(".h3-seo-trend-img, .ppc-trend-img, .email-marketing-img , .web-Strategy-img").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: this,
                        triggerHook: 1,
                    })
                    .setClassToggle(this, "active")
                    // .addIndicators({
                    //   colorTrigger: "black",
                    //   colorStart: "red",
                    // })
                    .reverse(false)
                    .addTo(Controller);
            });
        },
        email_marketing: function() {
            var Controller = new ScrollMagic.Controller();
            $(".sem-service-img-area").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: this,
                        triggerHook: 0.5,
                    })
                    .setClassToggle(this, "active")
                    // .addIndicators({
                    //   colorTrigger: "black",
                    //   colorStart: "red",
                    // })
                    .reverse(false)
                    .addTo(Controller);
            });
        },
        h3_working_process: function() {
            var Controller = new ScrollMagic.Controller();
            $(".h3-working-process, .about-working-process").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: ".arrow-ani",
                        triggerHook: 0.5,
                    })
                    .setClassToggle(".arrow-ani", "arrow-path-left")
                    // .addIndicators({
                    //   colorTrigger: "black",
                    //   colorStart: "red",
                    // })
                    .reverse(false)
                    .addTo(Controller);
            });
        },
        homePage: function() {
            var Controller = new ScrollMagic.Controller();
            $(".banner-img").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: this,
                        triggerHook: 0.6,
                    })
                    .setClassToggle(this, "active")
                    // .addIndicators({
                    //     // colorTrigger: "black",
                    //     // colorStart: "red",
                    // })
                    .reverse(false)
                    .addTo(Controller);
            });
        },
        seoFour: function() {
            var Controller = new ScrollMagic.Controller();
            $(".h4-seo-area, .h4-business-area, .h4-grouth-area , .h5-about-animation-img, .future-man-img-area, .seo-banner-img, .prefer-man, .prefer-bg").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: this,
                        triggerHook: 0.8,
                    })
                    .setClassToggle(this, "active")
                    // .addIndicators({
                    //     colorTrigger: "black",
                    //     colorStart: "red",
                    // })
                    .reverse(false)
                    .addTo(Controller);
            });
        },
        prefer_scrollmagic: function() {
            var Controller = new ScrollMagic.Controller();
            $(".h2-prefer-image-area").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: this,
                        triggerHook: 0.7,
                        update: false,
                        // reverse: false,
                    })
                    .setClassToggle(this, "active")
                    .reverse(false)
                    .addTo(Controller);
            });
            // var controller = new ScrollMagic.Controller();

            // new ScrollMagic.Scene({
            //         triggerElement: '.h2-prefer-image-area',
            //         duration: "200%",
            //         triggerHook: 0.7,
            //     })
            //     .setClassToggle('.h2-prefer-image-area', 'active')
            //     .reverse(false)
            //     .addIndicators()
            //     .addTo(controller);
        },
        contact_scrollmagic: function() {
            var Controller = new ScrollMagic.Controller();
            $(".conatct-man , .contact-circle ,.contact-information-img").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: this,
                        triggerHook: 0.7,
                        update: false,
                        // reverse: false,
                    })
                    .setClassToggle(this, "active")
                    .reverse(false)
                    .addTo(Controller);
            });
        },
        footer_scrollmagic: function() {
            var Controller = new ScrollMagic.Controller();
            $(".footer-area").each(function() {
                new ScrollMagic.Scene({
                        triggerElement: this,
                        triggerHook: 0.5,
                    })
                    .setClassToggle(this, "active")
                    .reverse(false)
                    .addTo(Controller);
            });
        },

        init: function() {
            scrollfunction.we_are_scrollmagic();
            scrollfunction.WebsiteTraffic();
            scrollfunction.way_to_feture();
            scrollfunction.h3_working_process();
            scrollfunction.ppc_advertising_img();
            scrollfunction.we_are_bg_scrollmagic();
            scrollfunction.email_marketing();
            scrollfunction.seoFour();
            scrollfunction.homePage();
            scrollfunction.prefer_scrollmagic();
            scrollfunction.seo_trendImg();
            scrollfunction.footer_scrollmagic();
            scrollfunction.contact_scrollmagic();
        },
    };

    $(document).ready(function() {
        scrollfunction.init();
    });
})(jQuery);