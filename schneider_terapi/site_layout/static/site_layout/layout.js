document.addEventListener('DOMContentLoaded', () => {
    const navEl = document.querySelector('.navbar');

    console.log(navEl);

    window.addEventListener('scroll', () => {
        if (window.scrollY >= 56) {
            navEl.classList.add('navbar-scrolled');
        } else if (window.scrollY < 56) {
            navEl.classList.remove('navbar-scrolled');
        }
    });
});