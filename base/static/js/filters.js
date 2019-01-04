$(function() {

	const $path = window.location.pathname;
	if ( '/' === $path ) {
		$('.m__filters-cycle').val('1');
  	$('.m__filters-topic').val('0');
	} else {
		const $expath = $path.split('/');
		$('.m__filters-cycle').val($expath[1]);
		$('.m__filters-topic').val($expath[2]);
	}

	$('.m__filters select').on('change', function() {
		const $cycle = $('.m__filters-cycle').val();
		const $topic = $('.m__filters-topic').val();
		window.location.replace('/'+$cycle+'/'+$topic);
	});


	$('#current-talk-form').on('submit', function(event){
    event.preventDefault();

    $.ajax({
      url : "/current/",
      type : "POST",
      data : { 
        csrfmiddlewaretoken: $(this).children('input[type=hidden]').val(),
        human: $('#id_human').val(),
       	topic: $('#id_topic').val(),
       	name: $('#id_name').val(),
       	link: $('#id_link').val(),
      },

      success : function(json) {
        if(json.success == '1'){
	        $('#current-talk-form').fadeOut();
  	      $('#results').html('<div class="alert alert-info" role="alert">Talk saved!</div>');
    	    $('.a__victimbtn').fadeIn();
        }
      },

      error : function(xhr,errmsg,err) {
        $('#results').html('<div class="alert alert-danger" role="alert">Oops! We have encountered an error</div>');
        console.log(xhr.status + ": " + xhr.responseText);
      }
    });
	});


});
