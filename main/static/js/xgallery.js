const img_product = document.querySelector('.img-product')
const img_gallery = document.querySelectorAll('.img-gallery')
img_gallery.forEach((img) => {
    $(img).click(function (e) {
        img_product.src = img.src
        var current = document.getElementsByClassName("img-gallery active");
        if (current.length > 0) {
          current[0].className = current[0].className.replace(" active", "");
        }
        this.className += " active";
    });
})
