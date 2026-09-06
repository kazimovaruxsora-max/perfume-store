document.addEventListener('DOMContentLoaded', function () {
    // Мобильное меню
    var burger = document.getElementById('burgerBtn');
    var nav = document.getElementById('mainNav');
    if (burger && nav) {
        burger.addEventListener('click', function () {
            burger.classList.toggle('active');
            nav.classList.toggle('open');
        });
        nav.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                burger.classList.remove('active');
                nav.classList.remove('open');
            });
        });
    }

    // Плавное появление карточек товаров при прокрутке
    var cards = document.querySelectorAll('.product-card');
    if ('IntersectionObserver' in window && cards.length) {
        cards.forEach(function (card) {
            card.classList.add('pre-reveal');
        });
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        cards.forEach(function (card) { observer.observe(card); });
    }
});
