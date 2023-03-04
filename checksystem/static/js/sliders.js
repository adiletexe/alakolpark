const swiper = new Swiper('.swiper-1', {
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },

    loop: true,

    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },

    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

let slides = 3;

if (screen.width <= 880) {
    slides = 2;
}

if (screen.width <= 640) {
    slides = 1;
}

const swiper2 = new Swiper('.swiper-2', {
    slidesPerView: slides,
    
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },

    loop: true,

    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },

    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

const swiper3 = new Swiper('.swiper-3', {
    slidesPerView: 1,
    
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },

    loop: true,

    pagination: {
        el: '.testimonals .swiper-pagination',
        clickable: true,
    },

    navigation: {
        nextEl: '.testimonals .swiper-button-next',
        prevEl: '.testimonals .swiper-button-prev',
    },
});