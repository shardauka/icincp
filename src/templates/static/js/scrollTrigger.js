// gsap.to(".header-area", {
//     scrollTrigger: ".header-area", // start the animation when ".box" enters the viewport (once)
//     x: 500
// });

function animateFrom(elem, direction) {
    direction = direction | 1;

    var x = 0,
        y = direction * 100;
    if (elem.classList.contains("get-left")) {
        x = -100;
        y = 0;
    } else if (elem.classList.contains("get-right")) {
        x = 100;
        y = 0;
    }
    if (elem.classList.contains("get-top")) {
        x = 0;
        y = -100;
    } else if (elem.classList.contains("get-bottom")) {
        x = 0;
        y = 100;
    }
    gsap.fromTo(elem, { x: x, y: y, autoAlpha: 0 }, {
        duration: 1.25,
        x: 0,
        y: 0,
        autoAlpha: 1,
        ease: "expo",
        overwrite: "auto"
    });
}

function hide(elem) {
    gsap.set(elem, { autoAlpha: 0 });
}

document.addEventListener("DOMContentLoaded", function() {
    gsap.registerPlugin(ScrollTrigger);

    gsap.utils.toArray(".animate").forEach(function(elem) {
        hide(elem); // assure that the element is hidden when scrolled into view

        ScrollTrigger.create({
            trigger: elem,
            once: true,
            onEnter: function() { animateFrom(elem) },
            // onEnterBack: function() { animateFrom(elem, -1) },
            //onLeave: function() { hide(elem) } // assure that the element is hidden when scrolled into view
        });
    });
});