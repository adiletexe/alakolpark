$(document).ready(function() {
    $(".clickable").click(function(event) {
        $(this).toggleClass("active").next().slideToggle(200);
    });

    
});