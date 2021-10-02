let owlSetting = {
    rtl: true,
    dots: false,
    loop: true,
    items: 4,
    autoplayHoverPause: true,
    autoplayTimeout: 3000,
    autoplay: true,
    autoplaySpeed: 2000,
    responsive: {
        0: {
            items: 1,
        },
        576: {
            items: 2
        },
        768: {
            items: 2
        },
        992: {
            items: 3
        },
        1200: {
            items: 4
        }

    },
};

$(window).ready(function () {
    if ($('.select-ex').length > 0)
        $('.select-ex').select2();

    $('input[type="radio"][name="like"]').change(function (e) {
        let value = $(this).val();

        if (value == 1) {
            $('.dislike').removeClass('dislikeChecked');
            $('.like').addClass('likeChecked');
        } else {
            $('.dislike').addClass('dislikeChecked');
            $('.like').removeClass('likeChecked');
        }
    });

    new WOW().init();

    $(".position-relative-blog").addClass('a');

    $('body').click(function (event) {
        if (!$(event.target).closest('#navbar-modal').length && !$(event.target).is('#navbar-modal')) {
            $(".navbar-modal").modal('hide');
        }
    });

    let newTheme = $('#owl-carousel');
    newTheme.owlCarousel(owlSetting);

    $('#next-owl').click(function (e) {
        e.preventDefault();
        newTheme.trigger('next.owl.carousel');
    });
    $('#prev-owl').click(function (e) {
        e.preventDefault();
        newTheme.trigger('prev.owl.carousel');
    });

    resize();

    $(window).resize(function () {
        resize();
    });


    var delay = 3500;
    var sliderRadios = document.getElementsByName("carousel-3d");
    var carouselText = $('.carousel-text');
    var index = 0;
    var imageCount = sliderRadios.length;

    setInterval(function () {
        index++;
        if (index > imageCount - 1) {
            index = 0;
        }
        $(carouselText).css({opacity: 0, height: '0'});
        $(carouselText[index]).css({opacity: 1, height: 'auto'});

        $(sliderRadios).removeAttr('checked');
        $(sliderRadios[index]).attr('checked', 'checked');
    }, delay);

    $('a[data-toggle="collapse"]').click(function () {
        let i = $($(this).children()[1]);
        if (i.hasClass('rotate180'))
            i.removeClass('rotate180');
        else
            i.addClass('rotate180');

    });

    $('#next_1').click(function () {
        sliders.trigger('next.owl.carousel');
    });
    $('#prev_1').click(function () {
        sliders.trigger('prev.owl.carousel');
    });

    if ($('.count').length > 0)
        $('.count').counterUp({
            delay: 10,
            time: 1000,
        });

    $('#clear-checked').on('click', function () {
        $('input:checked').prop('checked', false);
    });


// gallery owl-carousel

    document.documentElement.setAttribute("lang", "en");
    document.documentElement.removeAttribute("class");


// gallery owl-carousel


    let sliders = $('#owl_1');
    sliders.owlCarousel({
        rtl: true,
        dots: false,
        loop: true,
        items: 4,
        autoplayHoverPause: true,
        autoplayTimeout: 3000,
        autoplay: true,
        autoplaySpeed: 2000,
        margin: 20,
        responsive: {
            0: {
                items: 1,
            },
            500: {
                items: 2
            },
            600: {
                items: 2
            },
            992: {
                items: 3
            },
            1200: {
                items: 4
            },
        },

    });

    let sliderp = $('#owl-carousel-profile');
    sliderp.owlCarousel({
        rtl: true,
        dots: false,
        loop: true,
        items: 4,
        autoplayHoverPause: true,
        autoplayTimeout: 3000,
        autoplay: true,
        autoplaySpeed: 2000,
        margin: 20,
        responsive: {
            0: {
                items: 1,
            },
            500: {
                items: 2
            },
            600: {
                items: 2
            },
            992: {
                items: 3
            },
            1200: {
                items: 3
            },
        },
    });
});

function resize() {
    let addOwl = $('.add-owl');
    if ($(window).width() <= 992) {
        if (addOwl.length) {
            addOwl.addClass('owl-carousel');
            addOwl.owlCarousel(owlSetting);
        }
    } else {
        addOwl.trigger('destroy.owl.carousel').removeClass('owl-carousel');
    }

    if ($(window).width() >= 768)
        $('#navbar-modal').modal('hide');
}