$(document).ready(function () {
    // set language
    if(!sessionStorage.getItem("language")){
        sessionStorage.setItem("language", "none");
        setLang()
    }else{
        setLang()
    }
    function setLang (){
        if(sessionStorage.getItem("language") == "none"){
            document.getElementById('setLANGUAGE').classList.add('show')
            document.getElementById('setLANGUAGE').classList.remove('d-none')
            $("#setEN").click(()=>{
                sessionStorage.setItem("language", "true");
            })
            $("#setFA").click(()=>{
                sessionStorage.setItem("language", "true");
            })
            $("#setAR").click(()=>{
                sessionStorage.setItem("language", "true");
            })
            $("#setKU").click(()=>{
                sessionStorage.setItem("language", "true");
            })
        }
    }

    $(".dropdown-menu").click(function (e) {
        e.stopPropagation();
    })

    var mixer = mixitup('#mixitup_list');
    $(".owl-carousel").owlCarousel({
        responsiveClass: true,
        autoplay: true,
        autoplayTimeout: 2000,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 2
            }
        }
    });
    $(".filter").click(function () {
        $('li.active').removeClass('active');
        $(this).addClass('active');
    })
    const navbar = document.getElementById("navbar");
    const sticky = navbar.offsetTop;
    function fixedNavbar() {
        if (window.pageYOffset >= 500) {
            navbar.classList.add("fixed-navbar")
        } else {
            navbar.classList.remove("fixed-navbar");
        }
    }
    window.onscroll = function () { fixedNavbar() };

    const pageLANGUAGE = window.location.href.split('/')[3]
    const selectLANGUAGE = document.getElementById('selectLANGUAGE');
    if(pageLANGUAGE == 'en'){
        selectLANGUAGE.innerHTML = `<img class="me-2" src="/static/images/en.svg" width="25px"> English`
        document.getElementById('enLang').remove()
    }else if(pageLANGUAGE == 'fa'){
        selectLANGUAGE.innerHTML = `<img class="me-2" src="/static/images/fa.svg" width="25px"> فارسی`
        document.getElementById('faLang').remove()
    }
    else if(pageLANGUAGE == 'ar'){
        selectLANGUAGE.innerHTML = `<img class="me-2" src="/static/images/ar.svg" width="25px">  العربیة`
        document.getElementById('arLang').remove()
    }
    else if(pageLANGUAGE == 'ku'){
        selectLANGUAGE.innerHTML = `<img class="me-2" src="/static/images/ku.svg" width="25px">  kurdî`
        document.getElementById('kuLang').remove()
    }
    
})
