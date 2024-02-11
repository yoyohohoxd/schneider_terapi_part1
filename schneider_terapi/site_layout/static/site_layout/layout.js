document.addEventListener('DOMContentLoaded', () => {
    
    
    const navEl = document.querySelector('.navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY >= 56) {
            navEl.classList.add('navbar-scrolled');
        } else if (window.scrollY < 56) {
            navEl.classList.remove('navbar-scrolled');
        }
    });

    const el_autohide = document.querySelector('.autohide');
    if (el_autohide) {
        console.log(el_autohide);
    }

    if(el_autohide) {
        var last_scroll_top = 0;
        window.addEventListener('scroll', () => {
            let scroll_top = window.scrollY;
            if(scroll_top < last_scroll_top) {
                el_autohide.classList.remove('scrolled-down');
                el_autohide.classList.add('scrolled-up');
            } else {
                el_autohide.classList.remove('scrolled-up');
                el_autohide.classList.add('scrolled-down');
            }
            last_scroll_top = scroll_top;
        });
    }
});