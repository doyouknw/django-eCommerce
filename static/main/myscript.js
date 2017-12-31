$(document).ready(function(){
    $('#search').keypress(function(e){
        if(e.which == 13){
            $('#searchForm').submit()
        }
    });
});