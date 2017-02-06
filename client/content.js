
"use strict";

// Globals
var $ = jQuery;
var classified_posts = 0;

var ajax_classify_server_url = "https://localhost:8080/classifyPost";
var ajax_feed_server_url = "https://localhost:8080/feedPost";

function getVerificationOverlayHTML(post_title, post_domain, post_url) {
	let verificationOverlayHTML = "<div class='verification-message'>Help SlickBits get better! Is this post fake? <span style='float:right'><button class='slickbits-overlay-button' data-classification='real' data-title=" + encodeURIComponent(post_title) + " data-domain=" + encodeURIComponent(post_domain) + " data-url=" + encodeURIComponent(post_url) + ">Nope</button><button class='slickbits-overlay-button' data-classification='fake' data-title=" + encodeURIComponent(post_title) + " data-domain=" + encodeURIComponent(post_domain) + " data-url=" + encodeURIComponent(post_url) + ">Yes, this is Fake News</button></span></div><hr>";
	return verificationOverlayHTML;
}

function verificationButtonClickHandler() {
	$(this).attr("title", "Your response has been recorded!");
	$(this).tooltip();
	let post_title = $(this).data('title');
	let post_classification = $(this).data('classification');
	let post_url = $(this).data('url');
	let post_domain = $(this).data('domain');
  	let cur_post_url = ajax_feed_server_url + "?title=" + post_title + "&url=" + post_url + "&domain=" + post_domain + "&y=" + post_classification;
$.post(cur_post_url, '', function(data) {console.log("RESPONSE RECEIVED " + data);})


}

flagPosts();
window.setInterval(function(){
  flagPosts();
}, 4000);



chrome.extension.onRequest.addListener(function(request, sender, sendResponse) {

	console.log("request received");
 	if (request.action == "getDOM") {
 		content_doc = document;
 		console.log(document.getElementsByTagName("div"));
   		sendResponse({dom: document.getElementsByTagName("div")});
 	} else if (request.action == "getDivs") {
 		console.log("getDivs");
 		var ret_list = findDivsById("thing_");
 		sendResponse(ret_list);
    	sendResponse({});
   	} else if (request.action == "getPosts") {
   		console.log("getPosts request received");
   		flagPosts();
   		sendResponse();
   	}
});

function logAllShares() {
	var post_list = $("div[role='article']");
	var post, title;
	for (var i = 0; i < post_list.length; i++) {
		post = $(post_list[i]);
		title = getPostTitle(post);
		if (title.length) {
			$(title).html("SlickBits Win Hackathon, Become Billionaires")
		}
	}
}

function addOverlay(el) {
	let parent = $(el).parent();
	let overlay = $("<div></div>");

	// Overlay setup
	let width = el.width();
	let height = el.height();
	overlay.width(width);
	overlay.height(height);
  /*
	overlay.css({
		"background-color": "#EEE",
	});
  */
  overlay.addClass("fake-news-post");

	el.css({
		"opacity": "0.35",
    "border-radius": "0.35em"
	});

	// Parent > overlay > el
	overlay.append(el);
	parent.append(overlay);
}

function flagPosts() {
	//Finds all posts, if post is fake, put an overlay on it
	let post_list = $("._5pcr[role='article']");

	var current_posts = post_list.length;
	// Overlay fake articles
	for ( var i = classified_posts; i < current_posts; i++) {
		var fake_post = $(post_list.get(i));
		addUserVerificationOverlay(fake_post);
		isPostFake(fake_post);
	}
	classified_posts = current_posts;

	//post_list[0].style.display = "none";
	return post_list;
}

function findDivsById(start_substr) {
	var div_list = document.getElementsByTagName("div");
	var ret_list = [];
	for (i = 0; i < div_list.length; i++){
		div = div_list[i];
		if (div && div.getAttribute("id") && div.getAttribute("id").startsWith(start_substr)) {
			ret_list.push(div);
		}
	}
	return ret_list;
}

function addUserVerificationOverlay(post) {
	var post_title = $(post).find('._6m6').text();
	var post_domain = $(post).find("._6mb").text().split("|")[0];
	if (post_title.length && post_domain.length) {
		var post_link = $(post).find("._3ekx");
		var post_url = $(post_link).find('a').attr("href");
	}
	$(post).prepend(getVerificationOverlayHTML(post_title, post_domain, post_url));
	$('.slickbits-overlay-button').unbind('click');
	$('.slickbits-overlay-button').click(verificationButtonClickHandler);
}


function extraParameterBS(fake_post) {
	return function handleClassifierResponse(data) {
		if (data.toLowerCase() === 'fake') {
			addOverlay(fake_post);
		}
	}
}

function isPostFake(post) {
	//Prepare the features
	var post_title = $(post).find('._6m6').text();
	var post_domain = $(post).find("._6mb").text().split("|")[0];
	if (post_title.length && post_domain.length) {

		var post_link = $(post).find("._3ekx");
		var post_url = $(post_link).find('a').attr("href");

  		let cur_post_url = ajax_classify_server_url + "?title=" + post_title + "&url=" + post_url + "&domain=" + post_domain;
		$.ajax({
			current_post : post,
			url : cur_post_url,
			method : "POST",
			success : extraParameterBS($(post))
		});
	}
	return false;
}
