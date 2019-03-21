$(document).ready(function(){
    $('.pet').click(function(){
        $('.pet').attr("disabled", "true");
        setTimeout(
            function() 
            {
                $('#one').toggle();
                $('#two').toggle();
                $('.pet').removeAttr("disabled");        
            }, 5000);
            $('#one').toggle();
            $('#two').toggle();
    });
    setTimeout(function(){
        $('.errorlist').css('display','none');
    },5000);
    
});