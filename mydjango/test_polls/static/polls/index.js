$(document).ready(function(){
			$(window).scroll(function(){
				if($(this).scrollTop() > 100){
					$('.nav-container').addClass('nav-fixed')
				}
				else{
					$('.nav-container').removeClass('nav-fixed')
				}
			});

			$("#inner1-head").click(function(){
				$('#inner1-content').slideToggle()
				
			});

			$("#inner2-head").click(function(){
				$('#inner2-content').slideToggle()
				
			});	

			$('#slide-head1').click(function(){
				document.getElementById('img1').style.width = $('#slide-container').width() - 210 + "px"
				$('#slide-content1').animate({
					width:"toggle"
				});
				if($('#slide-content2').is(':visible') | $('#slide-content3').is(':visible') | $('#slide-content4').is(':visible') | $('#slide-content5').is(':visible') ){
					$('#slide-content2').animate({width:"hide"});
					$('#slide-content3').animate({width:"hide"});
					$('#slide-content4').animate({width:"hide"});
					$('#slide-content5').animate({width:"hide"});
				}

			});
			$('#slide-head2').click(function(){
				document.getElementById('img2').style.width = $('#slide-container').width() - 210 + "px"
				$('#slide-content2').animate({
					width:"toggle"
				});
				if($('#slide-content1').is(':visible') | $('#slide-content3').is(':visible') | $('#slide-content4').is(':visible') | $('#slide-content5').is(':visible') ){
					$('#slide-content1').animate({width:"hide"});
					$('#slide-content3').animate({width:"hide"});
					$('#slide-content4').animate({width:"hide"});
					$('#slide-content5').animate({width:"hide"});
				}
			});
			$('#slide-head3').click(function(){
				document.getElementById('img3').style.width = $('#slide-container').width() - 210 + "px"
				$('#slide-content3').animate({
					width:"toggle"
				});
				if($('#slide-content1').is(':visible') | $('#slide-content2').is(':visible') | $('#slide-content4').is(':visible') | $('#slide-content5').is(':visible') ){
					$('#slide-content1').animate({width:"hide"});
					$('#slide-content2').animate({width:"hide"});
					$('#slide-content4').animate({width:"hide"});
					$('#slide-content5').animate({width:"hide"});
				}
			});
			$('#slide-head4').click(function(){
				document.getElementById('img4').style.width = $('#slide-container').width() - 210 + "px"
				$('#slide-content4').animate({
					width:"toggle"
				});
				if($('#slide-content1').is(':visible') | $('#slide-content2').is(':visible') | $('#slide-content3').is(':visible') | $('#slide-content5').is(':visible') ){
					$('#slide-content1').animate({width:"hide"});
					$('#slide-content2').animate({width:"hide"});
					$('#slide-content3').animate({width:"hide"});
					$('#slide-content5').animate({width:"hide"});
				}
			});
			$('#slide-head5').click(function(){
				document.getElementById('img5').style.width = $('#slide-container').width() - 210 + "px"
				$('#slide-content5').animate({
					width:"toggle"
				});
				if($('#slide-content1').is(':visible') | $('#slide-content2').is(':visible') | $('#slide-content3').is(':visible') | $('#slide-content4').is(':visible')){
					$('#slide-content1').animate({width:"hide"});
					$('#slide-content2').animate({width:"hide"});
					$('#slide-content3').animate({width:"hide"});
					$('#slide-content4').animate({width:"hide"});
				}
				document.getElementById('img3-div3').style.opacity = 1.0
			});
			// if($('#slide-content1').is(':hidden')){
			// 	document.getElementById('img5').style.width = $('#slide-container').width() - 210 + "px"
			// 	$('#slide-content5').animate({width:"show"});
			// }
			$('#login-head').click(function(){
				$('#login-content').slideToggle()
			});
});