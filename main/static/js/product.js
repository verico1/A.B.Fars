const product_name = document.getElementById('product-name').innerText
const share = (platform) => {
    if (platform == "facebook") {
        window.open(`https://www.facebook.com/sharer.php?u=${window.location.href}`);
    }
    if (platform == "whatsapp") {
        window.open(`https://api.whatsapp.com/send?text=${product_name}، مشاهده محصول در لینک : ${window.location.href}`);
    }
    if (platform == "telegram") {
        window.open(`https://t.me/share/url?url=${window.location.href}&text=${product_name}`);
    }
}