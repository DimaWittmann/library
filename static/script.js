function show_edit_pane () {
    $('.edit_pane').toggle();
};

function delete_entity(url){
    $.ajax({
    	type: "DELETE",
    	url: url, 
        success: function(data, textStatus, jqXHR ){
            window.location.replace(data[0]);
        }
    })
};
