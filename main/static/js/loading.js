function disable_loading() {
    const loading = document.getElementById('loading');
    setTimeout(() => {
        loading.classList.add('fade')
        document.body.style.overflowY = "auto";
        setTimeout(() => {
            loading.classList.add('d-none')
        }, 100);
    }, 300);
}
if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', disable_loading);
} else {
    disable_loading();
}