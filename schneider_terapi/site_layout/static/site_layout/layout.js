document.addEventListener('DOMContentLoaded', () => {
    
    
    const navEl = document.querySelector('.navbar');
    const label = document.querySelector('[for=id_message]');
    const textArea = document.querySelector('.textarea');

    // Removes 'Besked' floating field when there is enough text
    // in the textArea that the window needs a scrollbar
    textArea.addEventListener('scroll', () => {
        if (textArea.clientHeight < textArea.scrollHeight) {
            label.style.display = 'none';
        } 
    });


    // Alerts for page --> gets sepcific alert placeholders from template
    const alertPlaceholder = document.getElementById('liveAlertPlaceholder');
    const appendAlert = (message, type) => {
        const wrapper = document.createElement('div');
        wrapper.innerHTML = [
            `<div class="alert alert-${type} alert-dismissible fade show" role="alert">`,
            `   <div>${message}</div>`,
            '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
            '</div>'
        ].join('')

        // Appends to alert placeholder
        alertPlaceholder.append(wrapper);
    }

    // Appends alert button from the const declared above
    const alertTrigger = document.getElementById('-');
    
    if (alertTrigger) {
        alertTrigger.addEventListener('click', () => {
            appendAlert('Jeg har modtaget din email. Jeg vender tilbage indenfor X dage.', 'success');
        });
    }

    // Navbar --> must be reworked...
    window.addEventListener('scroll', () => {
        if (window.scrollY >= 56) {
            navEl.classList.add('navbar-scrolled');
        } else if (window.scrollY < 56) {
            navEl.classList.remove('navbar-scrolled');
        }
    });

    const el_autohide = document.querySelector('.autohide');

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