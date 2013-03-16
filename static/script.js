
$(document).ready(function(){
	

	$("a.editMode").click(
		function(){
			$("div.editField").slideToggle("medium");
		});

	var submit_book = function(e) {
      $.getJSON($SCRIPT_ROOT + '/add_book', {
        title: $('input[name="new_book"]').val(),
      }, function(data) {
      	if (data.title != ""){
      		$('div#BookList ul').prepend(title);
      	}
      	
        $('input[name=new_book]').focus().select();
      });
      return false;
    }

    $('a#add_book').click(submit_form);
}