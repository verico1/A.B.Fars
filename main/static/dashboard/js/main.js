
tagInput = document.getElementById('tagInput');
tagList = document.getElementById('tagList');
tagBtn = document.getElementById('tagBtn');

if(tagInput){
    removeTags.style.display = "none"
    tagBtn.addEventListener('click', function(){
        if (tagInput.value == "" || /^\s/.test(tagInput.value) === true){
            console.log("error");
            tagInput.value = '';
        }else{
            tagList.innerHTML += `<p class="text-secondary">${tagInput.value}</p>`;
            tagInput.value = ''; 
        }
        removeTags.style.display = "block"
    });

    tagInput.addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            tagBtn.click();
            removeTags.style.display = "block"
        }
    });
}

removeTags.addEventListener('click', () =>{
    tagList.innerHTML=""
    removeTags.style.display = "none"
})
