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

function getRandomProfileimg() {
	var ProfileImgList = [
		"https://i.postimg.cc/pXHPfSx9/user1.png",
		"https://i.postimg.cc/wT2YhT0P/user10.png",
		"https://i.postimg.cc/7ZL8X8RL/user11.png",
		"https://i.postimg.cc/DwYVMpVP/user12.png",
		"https://i.postimg.cc/N09hq8Bq/user13.png",
		"https://i.postimg.cc/25PszqSq/user14.png",
		"https://i.postimg.cc/G2GZ9c4X/user15.png",
		"https://i.postimg.cc/fys196XD/user16.png",
		"https://i.postimg.cc/gjKQqNqR/user17.png",
		"https://i.postimg.cc/NG83cjqM/user18.png",
		"https://i.postimg.cc/159L51sK/user19.png",
		"https://i.postimg.cc/y86B5SDs/user2.png",
		"https://i.postimg.cc/VLD2JZNP/user20.png",
		"https://i.postimg.cc/mgkJC3cz/user21.png",
		"https://i.postimg.cc/Cx2tNZDv/user22.png",
		"https://i.postimg.cc/3wDqbKF3/user23.png",
		"https://i.postimg.cc/NMqz3Wdm/user24.png",
		"https://i.postimg.cc/cHRb0Xzj/user25.png",
		"https://i.postimg.cc/tJ9mTFQg/user26.png",
		"https://i.postimg.cc/4yw2hnsQ/user27.png",
		"https://i.postimg.cc/h405YZTQ/user28.png",
		"https://i.postimg.cc/TYY4vjJ7/user29.png",
		"https://i.postimg.cc/mgdRG29M/user3.png",
		"https://i.postimg.cc/8PKnpFy1/user30.png",
		"https://i.postimg.cc/1387f9TD/user31.png",
		"https://i.postimg.cc/DwRjG9kH/user32.png",
		"https://i.postimg.cc/zfWdFxqB/user33.png",
		"https://i.postimg.cc/DZTxj1zc/user34.png",
		"https://i.postimg.cc/V6WD35rP/user35.png",
		"https://i.postimg.cc/8cywz3my/user36.png",
		"https://i.postimg.cc/T2Qt0Lvr/user37.png",
		"https://i.postimg.cc/FsBDtMRz/user38.png",
		"https://i.postimg.cc/Z5vjJwBc/user39.png",
		"https://i.postimg.cc/25VYjRdt/user4.png",
		"https://i.postimg.cc/cJqhCffN/user40.png",
		"https://i.postimg.cc/TPr9Dhc5/user41.png",
		"https://i.postimg.cc/NMBx7YNJ/user43.png",
		"https://i.postimg.cc/pTCJs742/user44.png",
		"https://i.postimg.cc/j2jQmcYy/user45.png",
		"https://i.postimg.cc/sx09rW3q/user46.png",
		"https://i.postimg.cc/y6fT9M0j/user47.png",
		"https://i.postimg.cc/65yfhM0X/user48.png",
		"https://i.postimg.cc/9FKtgy8q/user49.png",
		"https://i.postimg.cc/xdh2cxt1/user5.png",
		"https://i.postimg.cc/52z5hjTK/user50.png",
		"https://i.postimg.cc/q7dc44dJ/user51.png",
		"https://i.postimg.cc/G2D1YF5J/user6.png",
		"https://i.postimg.cc/T1Xvcy88/user7.png",
		"https://i.postimg.cc/sx9dHVyM/user8.png",
		"https://i.postimg.cc/05psyCm9/user9.png"

	];
	return ProfileImgList[Math.floor(Math.random() * ProfileImgList.length)];
};

var validity_chk_data={};
function chk_addr_validity(addr){

	$.ajax({
		data : JSON.stringify({
		networkID : ethereum.networkVersion,
		address : addr,
			}),
		type : 'POST',
		url : '/api/chk_addr_validity',
		dataType: 'json',
		contentType: 'application/json',
		headers: {'address_chk':addr,'X-CSRFToken':csrf_token}
	}).done(function(data) {
	$('#output').text(data.output).show();

	// Show Message Status Success/Failure
	if (data.error != undefined){
		console.log(data.error);
	}
	else{
		console.log(data.output);
	}
	validity_chk_data = {'status':data.msg_status, 'color':data.color}

	document.getElementById("msg-send-confirm").textContent = data.msg_status;
	document.getElementById("msg-send-confirm").style.color = data.color;

	setTimeout(function() {
		document.getElementById("msg-send-confirm").textContent = '';
	}, 1000);

	
	});
	return true;
};

// Receiver Wallet Address List Box
var modal = null
 function AddNewContactForm() {
   if(modal === null) {
     document.getElementById("new-contact-detail").style.display = "block";
     modal = true
   } else {
     document.getElementById("new-contact-detail").style.display = "none";
     modal = null
   }
 }


function newContact() {
	new_Receiver_Address = $("#newReceiverAddress").val();
        
    if($.trim(new_Receiver_Address) == '') {
        return false;
    }


	$.ajax({
		data : JSON.stringify({
		networkID : ethereum.networkVersion,
		sender_address : ethereum.selectedAddress,
		receiver_address : new_Receiver_Address,
			}),
		type : 'POST',
		url : '/api/chk_addr_validity',
		dataType: 'json',
		contentType: 'application/json',
		headers: {'sender_address': ethereum.selectedAddress, 'receiver_address':new_Receiver_Address, 'X-CSRFToken':csrf_token}
	}).done(function(data) {
	$('#output').text(data.output).show();

	// Show Message Status Success/Failure
	if (data.error != undefined){
		console.log(data.error);
	}
	else{
		console.log(data.output);
	}
	validity_chk_data = {'status':data.msg_status, 'color':data.color}

	document.getElementById("msg-send-confirm").textContent = data.msg_status;
	document.getElementById("msg-send-confirm").style.color = data.color;

	setTimeout(function() {
		document.getElementById("msg-send-confirm").textContent = '';
	}, 1000);

	// Show status and colour & add contact
	document.getElementById("newContactValidityStatus").style.color = validity_chk_data['color'];

	if (validity_chk_data['status'] == "SUCCESS"){
		document.getElementById("newContactValidityStatus").textContent = "Address is correct for current networkID: "+ethereum.networkVersion+" (Check details in console)";
		$('<li class="contact"><div class="wrap"><span class="contact-status"></span><img src="'+getRandomProfileimg()+'" alt="" /><div class="meta"><p class="name">'+new_Receiver_Address+'</p><p class="preview"><span>You:</span> Added Contact</p></div></div></li>};').appendTo($('#contacts ul'));
		
		setTimeout(function() {
			AddNewContactForm()
			$('#newReceiverAddress').val(null);
			document.getElementById("newContactValidityStatus").textContent = '';
		}, 2000);
		
	}
	else if (validity_chk_data['status'] == "FAILED"){
		document.getElementById("newContactValidityStatus").textContent = "Address is incorrect for current networkID: "+ethereum.networkVersion+" (Check details in console)";
	};

	});



	// validity_chk_data = chk_addr_validity(new_Receiver_Address);
	// var executed = chk_addr_validity(new_Receiver_Address);
	// console.log(validity_chk_data);

	// document.getElementById("newContactValidityStatus").style.color = validity_chk_data['color'];

	// if (validity_chk_data['status'] == "SUCCESS"){
	// 	// $('#newContactValidityStatus').val('New Contact Address is Valid')
	// 	document.getElementById("newContactValidityStatus").textContent = "Address is correct for current networkID: "+ethereum.networkVersion+"\nCheck details in console";
	// 	// document.getElementById("newContactValidityStatus").style.color = validity_chk_data['color'];
	// 	$('<li class="contact"><div class="wrap"><span class="contact-status"></span><img src="'+getRandomProfileimg()+'" alt="" /><div class="meta"><p class="name">'+new_Receiver_Address+'</p><p class="preview"><span>You:</span> Added Contact</p></div></div></li>};').appendTo($('#contacts ul'));
		
	// 	setTimeout(function() {
	// 		AddNewContactForm()
	// 		$('#newReceiverAddress').val(null);
	// 		document.getElementById("newContactValidityStatus").textContent = '';
	// 	}, 2000);
		
	// }
	// else if (validity_chk_data['status'] == "FAILED"){
	// 	console.log("entered in ERROR")
	// 	document.getElementById("newContactValidityStatus").textContent = "Address is incorrect for current networkID: "+ethereum.networkVersion+"\nCheck details in console";
	// 	// document.getElementById("newContactValidityStatus").style.color = validity_chk_data['color'];
	// };

	
	// $('.contact.active .preview').html('<span>You: </span>' + message);
	// $(".messages").animate({ scrollTop: $(document).height() }, "fast");
};

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


// Receiver Wallet Address List Box
var modal = null
 function wallet_addr_list() {
	document.getElementById('receiver-wallet-lst-img').src=$(".contact-profile #receiver-img")[0]['src'];
   if(modal === null) {
     document.getElementById("rcvr-wallet-lst-box").style.display = "block";
     modal = true
   } else {
     document.getElementById("rcvr-wallet-lst-box").style.display = "none";
     modal = null
   }
 }