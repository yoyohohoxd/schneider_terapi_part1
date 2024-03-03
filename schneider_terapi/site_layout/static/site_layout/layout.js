document.addEventListener('DOMContentLoaded', () => {
    
    
    const navEl = document.querySelector('.navbar');
    const label = document.querySelector('[for=id_message]');
    const textArea = document.querySelector('.textarea');

    // Removes 'Besked' floating field when there is enough text
    // in the textArea that the window needs a scrollbar
    if (textArea) {
        textArea.addEventListener('scroll', () => {
            if (textArea.clientHeight < textArea.scrollHeight) {
                label.style.display = 'none';
            } 
        });
    }

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
    const alertTrigger = document.getElementById('submit-id-submit');
    
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
});