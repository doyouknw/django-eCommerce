$(document).ready(function(){
    $('.optBtn').on('click', function(){
        $(this).parent().find('.active').removeClass('active');
        $(this).addClass('active');
        if(this.id == "login"){
            $('.register').removeClass('active').addClass('inactive');
            $('.login').removeClass('inactive').addClass('active');
        }
        else{
            $('.login').removeClass('active').addClass('inactive');
            $('.register').removeClass('inactive').addClass('active');
        }
    });
});