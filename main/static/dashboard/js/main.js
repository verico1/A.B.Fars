$(document).ready(function () {
    $('#createCategory').click(()=>{
        $('#categroyModal').removeClass( "fade d-none" )
    })
    $('#modalContent').click(function(e) {
        e.stopPropagation();
    });
    $('#categroyModal').click(function() {
        $('#categroyModal').addClass( "fade d-none" )
    });
})