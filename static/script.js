



function update_title(url){
    $.post(url, {new_title : $('#new_title').val()},
        function(){
            alert($('#new_title').val());
            $('#title').html($('#new_title').val());
        }
    )
};
