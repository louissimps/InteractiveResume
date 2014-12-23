jQuery(document).ready(function($){
	var $timeline_block = $('#cd-timeline > .panel');
//	var $timeline_block = $('.cd-timeline-block');

	//hide timeline blocks which are outside the viewport
	$timeline_block.each(function(){
			if ($(this).offset().top > $(window).scrollTop() + $(window).height() * 0.75) {
				$(this).find('.panel-body, .panel-heading').addClass('is-hidden');
			}
	});

	//on scolling, show/animate timeline blocks when enter the viewport
	$(window).on('scroll', function(){
		$timeline_block.each(function(){
			if( $(this).offset().top <= $(window).scrollTop()+$(window).height()*0.75 && $(this).find('.panel-body').hasClass('is-hidden') ) {
				$(this).find('.panel-body, .panel-heading').removeClass('is-hidden').addClass('bounce-in');
			}
		});
	});
});