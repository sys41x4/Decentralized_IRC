$(".messages").animate({ scrollTop: $(document).height() }, "fast");

$("#profile-img").click(function() {
	$("#status-options").toggleClass("active");
});

$(".expand-button").click(function() {
  $("#profile").toggleClass("expanded");
	$("#contacts").toggleClass("expanded");
});

$("#status-options ul li").click(function() {
	$("#profile-img").removeClass();
	$("#status-online").removeClass("active");
	$("#status-away").removeClass("active");
	$("#status-busy").removeClass("active");
	$("#status-offline").removeClass("active");
	$(this).addClass("active");
	
	if($("#status-online").hasClass("active")) {
		$("#profile-img").addClass("online");
	} else if ($("#status-away").hasClass("active")) {
		$("#profile-img").addClass("away");
	} else if ($("#status-busy").hasClass("active")) {
		$("#profile-img").addClass("busy");
	} else if ($("#status-offline").hasClass("active")) {
		$("#profile-img").addClass("offline");
	} else {
		$("#profile-img").removeClass();
	};
	
	$("#status-options").removeClass("active");
});

function newMessage() {
	message = $(".message-input input").val();
	if($.trim(message) == '') {
		return false;
	}
	$('<li class="sent"><img src="https://avatars.githubusercontent.com/u/62654117?v=4" alt="" /><p>' + message + '</p></li>').appendTo($('.messages ul'));
	$('.message-input input').val(null);
	$('.contact.active .preview').html('<span>You: </span>' + message);
	$(".messages").animate({ scrollTop: $(document).height() }, "fast");
};

$('.submit').click(function() {
  newMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    newMessage();
    return false;
  }
});

// Redirections

document.getElementById("settings").onclick = function () {
    location.href = '/user/account';
};

// function show_wallet_addr_list() {
//     document.getElementById("rcvr_wallet").onclick = "hide_wallet_addr_list()";
//     document.getElementById("show_wallet_adresses_list").style.display = "block";
// }

// function hide_wallet_addr_list() {
//     document.getElementById("rcvr_wallet").onclick = "show_wallet_addr_list()";
//     document.getElementById("show_wallet_adresses_list").style.display = "none";

//   }

// $('#rcvr_wallet').click(function() {
//     show_wallet_addr_list();
//   });

// Receiver Wallet Address List Box
var modal = null
 function wallet_addr_list() {
   if(modal === null) {
     document.getElementById("rcvr-wallet-lst-box").style.display = "block";
     modal = true
   } else {
     document.getElementById("rcvr-wallet-lst-box").style.display = "none";
     modal = null
   }
 }