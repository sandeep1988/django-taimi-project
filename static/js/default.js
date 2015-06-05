$(function(){
	$('#BlogFeed').FeedEk({
		Type:'Blog',
		Title : 'Latest Articles',
		FeedUrl : 'http://blog.anujkumar.com/rss', //Provide link to your blog rss feed here
		SourceUrl : 'http://blog.anujkumar.com', //Provide link to your blog here
		MaxCount : 3, //Maximum number of posts to diaplay
		ShowDesc : true,
		ShowPubDate: true,
		FooterText:'Visit our blog' //text to display in footer link
	});
	$('#TwitterFeed').FeedEk({
		Type:'Tweets',
		Title : 'Recent Tweets',
		FeedUrl : 'https://api.twitter.com/1/statuses/user_timeline.rss?screen_name=anujkkk', //replace anujkkk with your twitter username
		SourceUrl : 'http://www.twitter.com/anujkkk', //replace anujkkk with your twitter username
		MaxCount : 3, //maximum number of tweets to display
		ShowDesc : true,
		ShowPubDate: true,
		FooterText:'Follow us @anujkkk' //text to display in footer link
	});
	$('#btnMgmt').click(function(e) {
		$('.all').quicksand( $('.mgmt li'), {
			duration: 500,
			attribute: 'id',
			easing: 'easeInOutQuad'
		});
		$("#liMgmt").attr("class","active");		
		$("#liHacks").attr("class","");
		$("#liDesigns").attr("class","");
		$("#liAll").attr("class","");
		e.preventDefault();
	});
	$('#btnDesigns').click(function(e) {
		$('.all').quicksand( $('.designs li'), {
			duration: 500,
			attribute: 'id',
			easing: 'easeInOutQuad'
		});
		$("#liMgmt").attr("class","");
		$("#liAll").attr("class","");		
		$("#liHacks").attr("class","");
		$("#liDesigns").attr("class","active");
		e.preventDefault();
	});

	$('#btnHacks').click(function(e) {
		$('.all').quicksand( $('.hacks li'), {
			duration: 500,
			attribute: 'id',
			easing: 'easeInOutQuad'
		});
		$("#liMgmt").attr("class","");
		$("#liAll").attr("class","");		
		$("#liHacks").attr("class","active");
		$("#liDesigns").attr("class","");
		e.preventDefault();
	});
	$('#btnAll').click(function(e) {
		$('.all').quicksand( $('.everything li'), {
			duration: 500,
			attribute: 'id',
			easing: 'easeInOutQuad'
		});
		$("#liMgmt").attr("class","");
		$("#liAll").attr("class","active");		
		$("#liHacks").attr("class","");
		$("#liDesigns").attr("class","");
		e.preventDefault();
	});

	$('body').tooltip({
		selector: '[rel=tooltip]',
		placement: 'bottom'
	});

	$('LI h4').click(function(e) {
		e.preventDefault(); // disable text selection
		$(this).parent().find('span').slideToggle();
		return false; // disable text selection
	});

	$('#search').keyup(function(e) {
		var s = $(this).val().trim();
		if (s === '') {
			$('#result LI').show();
			return true;
		}
		$('#result LI:not(:contains(' + s + '))').hide();
		$('#result LI:contains(' + s + ')').show();
		return true;
	});


});
