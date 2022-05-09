var chatSocket;

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
		broadcaststatus('online')
	} else if ($("#status-away").hasClass("active")) {
		$("#profile-img").addClass("away");
		broadcaststatus("away")
	} else if ($("#status-busy").hasClass("active")) {
		$("#profile-img").addClass("busy");
		broadcaststatus("busy")
	} else if ($("#status-offline").hasClass("active")) {
		$("#profile-img").addClass("offline");
		broadcaststatus("offline")
	} else {
		$("#profile-img").removeClass();
	};
	
	$("#status-options").removeClass("active");
});

// On Application Start
var contact_selected = 0;
document.getElementsByClassName('message-input')[0].style.display= 'none';

// // document.getElementsByClassName('messages')[0].style.display= 'none';

// document.getElementsByClassName('messages')[0].innerHTML='';
$('.messages ul')[0]['innerHTML']='' 
document.getElementById('receiver-img').src='';
document.getElementById('rcvr_name').innerHTML='';
document.getElementById('rcvr-wallet').style.display='none';
// // document.getElementsByClassName('contact-profile')[0].style.display= 'none';
document.getElementsByClassName('content')[0].style.backgroundColor = '#161818';


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

//fetch user's chats

window.onload = function fetch_chat_ids(fetcher){
	$.ajax({
		data: JSON.stringify({user:fetcher}),
		type: 'POST',
		url: '/api/chat_ids',
		dataType: 'json',
		contentType: 'application/json',
		headers:{'X-CSRFToken':csrf_token}
	}).done(function(data){
		console.log(data)
		for(i=0;i<Object.keys(data.chats).length;i++){
			current_chat_id = Object.keys(data.chats)[i];
			console.log(current_chat_id)
			users_in_room = data.chats[current_chat_id]
			for(j=0;j<users_in_room.length;j++){
				current_user = users_in_room[j]
				console.log(users_in_room)
				console.log(current_user)
				console.log(currentAccount!=current_user)
				if(currentAccount != current_user){
					receivers_addr = current_user
				}
			}
			console.log(current_chat_id,currentAccount,receivers_addr)
			init_ws(current_chat_id,currentAccount,receivers_addr)
		}
	})
}


// Fetch Communication Messages Between Sender and Receiver
function fetch_message(fetcher, receiver){
	$.ajax({
		data : JSON.stringify({
		networkID : ethereum.networkVersion,
		fetcher : fetcher,
		receiver : receiver,
			}),
		type : 'POST',
		url : '/api/fetch_messages',
		dataType: 'json',
		contentType: 'application/json',
		headers: {fetcher : fetcher, 'X-CSRFToken':csrf_token}
	}).done(function(data){displaymessages(data,fetcher,receiver,fromws=false)});
};

// initiate WS connection

function init_ws(roomName,fetcher,receiver){

	chatSocket = new WebSocket(
		'ws://'
		+ window.location.host
		+ '/ws/'
		+ roomName
		+ '/'
	);
	
	chatSocket.onmessage = function(e){
		data = JSON.parse(e.data)
		console.log(data)
		console.log("message event received.")
		if(data.message.msg_status){
		displaymessages(data,fetcher,receiver,fromws=true)
		}
		else if(data.message.contact_status){
			updateContactStatus(data.message)
		}
	}

	chatSocket.onclose = function(e) {
		console.error('Chat socket closed unexpectedly');
	};
}

function send_ws_message(payload){
	console.log("sending message event");
	chatSocket.send(JSON.stringify(payload));
}

//Update incomming contact status using websockets

function updateContactStatus(data){
	console.log("updating contact status")
	contact = Object.keys(data.contact_status)[0]
	console.log(contact)
	if(contact!=currentAccount){
	contact_status = data.contact_status[contact]
	console.log(contact_status)
	document.querySelector('[address-receiver="'+contact+'"]').children[0].children[0].className = "contact-status "+contact_status 
	}
}

// BroadCast user's status
function broadcaststatus(status){
	payload = {"type":"chat_message","message":{"contact_status":{[currentAccount]:status}}}
	send_ws_message(payload)
}

// updating code to display messages on the UI throught a common function... Required for WebSockets support.
// fromws varible tells if the message was sent is from websocket of not.
function displaymessages(data,fetcher,receiver,fromws=false) {
	console.log(data,fetcher,receiver)
	$('#output').text(data.output).show();
	// Show Message Status Success/Failure
	if(fromws){
		data = data.message;
		//console.log(data);
	}
	if (data.message_data == undefined){
		console.log(data.output);
	}
	else{
		console.log(data.output);

		validity_chk_data = {'status':data.msg_status, 'color':data.color}

		document.getElementById("msg-send-confirm").textContent = data.msg_status;
		document.getElementById("msg-send-confirm").style.color = data.color;

		setTimeout(function() {
			document.getElementById("msg-send-confirm").textContent = '';
		}, 1000);

		msg_data = data.message_data  
		//console.log("getting message data")
		if (msg_data.length!=0){
			for (let i = 0; i < msg_data.length; i++) {
				
				//console.log("looping")
				//console.log(msg_data[i]['sender'].toLowerCase() == fetcher.toLowerCase())
				if (msg_data[i]['sender'].toLowerCase() == fetcher.toLowerCase()){
					console.log("sender is fetcher")
					$('<li class="sent"><img src="'+$("#profile-img")[0]['src']+'" alt="" /><p>' + msg_data[i]['message'] + '</p></li>').appendTo($('.messages ul'));
					// $('#message').val(null);
					if (i+1 == msg_data.length){
						var last_msg_sndr = 'You';
					};
					
				}
				else if (msg_data[i]['sender'].toLowerCase() == receiver.toLowerCase()){
					console.log("sender is receiver")
					$('<li class="replies"><img src="'+$(".contact-profile #receiver-img")[0]['src']+'" alt="" /><p>' + msg_data[i]['message'] + '</p></li>').appendTo($('.messages ul'));
					if (i+1 == msg_data.length){
						var last_msg_sndr =  $('.'+receiver+' .wrap .meta .name')[0]['innerText'];
					};
				};	
			}
			console.log("loop done")
			$('.'+receiver+' .wrap .meta .preview')[0]['innerHTML'] = '<span>'+last_msg_sndr+': </span>' + msg_data[msg_data.length-1]['message']
			$(".messages").animate({ scrollTop: $(document).height() }, "fast");
		}
	}
}

// Generate Random Static Sender Pic
$("#profile-img")[0]['src'] = getRandomProfileimg();

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
		$('<li onclick="view_conversation($(this).attr(\'address-receiver\'))" address-receiver='+new_Receiver_Address+' class="contact '+new_Receiver_Address+'"><div class="wrap"><span class="contact-status"></span><img src="'+getRandomProfileimg()+'" alt="" /><div class="meta"><p class="name">'+new_Receiver_Address+'</p><p class="preview"><span>You:</span> Added Contact</p></div></div></li>};').appendTo($('#contacts ul'));
		
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
/*
function newMessage() {
	message = $(".message-input input").val();
	if($.trim(message) == '') {
		return false;
	}
	$('<li class="sent"><img src="'+$("#profile-img")[0]['src']+'" alt="" /><p>' + message + '</p></li>').appendTo($('.messages ul'));
	$('.message-input input').val(null);
	$('.contact.active .preview').html('<span>You: </span>' + message);
	$(".messages").animate({ scrollTop: $(document).height() }, "fast");
};

$('.submit').click(function() {
  newMessage();
});
*/
// $(window).on('keydown', function(e) {
//   if (e.which == 13) {
//     newMessage();
//     return false;
//   }
// });

// Redirections

document.getElementById("settings").onclick = function () {
    location.href = '/user/account';
};



// Open Conversation
function view_conversation(rcvr_addr) {
// $('.contact').click(function() {
	// console.log($(data).attr("address-receiver"));
	rcvr_addr = rcvr_addr.toLowerCase();
	rcvr_name = $('.'+rcvr_addr+' .wrap .meta .name')[0]['innerText'];
	rcvr_img = $('.'+rcvr_addr+' .wrap img')[0]['currentSrc'];

	if (document.getElementsByClassName('contact active')[0] == undefined){
		// Add Active Class in currect contact
		document.getElementsByClassName(rcvr_addr)[0].classList.add("active");
	}
	else{
		// Remove Active Class from previous contact
		
		document.getElementsByClassName('contact active')[0].classList.remove('active');

		// Add Active Class in currect contact
		document.getElementsByClassName(rcvr_addr)[0].classList.add("active");

		
	}
	
	
	// Update Message Field
	document.getElementById('rcvr_name').innerHTML = rcvr_name;
	document.getElementById('receiver-img').src = rcvr_img;
	if ($('.messages ul')[0] != undefined){
		$('.messages ul')[0]['innerHTML'] = '';
	}
	

	if (contact_selected==0){
		// Show Conversation UI
		document.getElementsByClassName('message-input')[0].style.display= 'block';
		// document.getElementsByClassName('messages')[0].style.display= 'block';
		// document.getElementsByClassName('contact-profile')[0].style.display= 'block';
		document.getElementsByClassName('content')[0].style.removeProperty('background-color');
		// document.getElementById('receiver-img').src='';
		// document.getElementById('rcvr_name').innerHTML='';
		document.getElementById('rcvr-wallet').style.removeProperty('display');
		document.getElementsByClassName('startup-logo')[0].style.display='none';
		document.getElementsByClassName('message-input')[0].style.display= 'block';



// document.getElementById('rcvr-wallet').style.display='none';
// // // document.getElementsByClassName('contact-profile')[0].style.display= 'none';
// document.getElementsByClassName('content')[0].style.backgroundColor = '#161818';

		contact_selected=1;
	};
	

	// Update Receiver Wallet Address List
	$("#rcvr-wallet-lst-box p")[0]['textContent'] = rcvr_addr;
	document.getElementById('receiver').value = rcvr_addr;

	// Fetch Conversation Between the sender & Receiver
	fetch_message(ethereum.selectedAddress, rcvr_addr);
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

 function constructcontactsUI(data){
	contacts_div = document.getElementById('contacts_holder') 
	Object.keys(data.result.sent).forEach(function(address){
		contacts_div.innerHTML = contacts_div.innerHTML + '<li class="contact" id='+address+' onclick=changeactive("'+address+'")><div class="wrap"><span class="contact-status online"></span><img src="http://emilcarlsson.se/assets/louislitt.png" alt="" /><div class="meta"><p class="name">'+address+'</p></div></div></li>'
	 });
	Object.keys(data.result.received).forEach(function(address){
		contacts_div.innerHTML = contacts_div.innerHTML + '<li class="contact" id='+address+' onclick=changeactive("'+address+'")><div class="wrap"><span class="contact-status online"></span><img src="http://emilcarlsson.se/assets/louislitt.png" alt="" /><div class="meta"><p class="name">'+address+'</p></div></div></li>'
	 }) 
 }

function changeactive(address){
	if (document.getElementsByClassName('contact active')[0] != null){
	document.getElementsByClassName('contact active')[0].className = 'contact';
	document.getElementById(address).className = 'contact active';
	}
	else{
		document.getElementById(address).className = 'contact active';
	}
}
 function getmessages(download=false){
    url = "/api/getMessages"
    fetch(url,{
        method:"POST",
        headers:{"Content-type":"application/json"},
        body:JSON.stringify({"wallet_address":g_wallet_address})
    })
    .then(response => {return response.json()})
    .then(data => {
        if (download==true){
			data = JSON.stringify(data);
            var blob = new Blob([content], {
                type: "text/plain;charset=utf-8"
               });
            saveAs(blob,'messages.txt')
        }
        else{
        console.log(data);
		constructcontactsUI(data);
	}
    })
}

