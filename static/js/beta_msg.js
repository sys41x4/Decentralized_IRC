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


// Basic helper functions
// String Manipulation
function hex2ascii(str1){
	var hex  = str1.toString();
	var str = '';
	for (var n = 0; n < hex.length; n += 2) {
		str += String.fromCharCode(parseInt(hex.substr(n, 2), 16));
	}
	return str;
}

// Message Status and colour codes
var msg_status = {0:'FAILED', 1:'SUCCESS'}
var color = {0:'#e74c3c', 1:'#2ecc71'}

// Dragable DIVs with ID
// dragElement(document.getElementById('settings_tab'));
// dragElement(document.getElementById('new-contact-detail'));
// dragElement(document.getElementById('rcvr-wallet-lst-box'));

// $(function() {
// 	$('#new-contact-detail').draggable();
// });

// // Wait for HTML document to get ready
// window.addEventListener('load', function() { // NOT `DOMContentLoaded`
// 	// Do something about HTML document
// 	draggable = new PlainDraggable($('#new-contact-detail')[0]);
// });


// window.addEventListener('load', function() { // NOT `DOMContentLoaded`
// 	const wrapper = document.querySelector(".new-contact-detail"),
// 	header = wrapper.querySelector("div");

// 	function onDrag({movementX, movementY}){
// 		let getStyle = window.getComputedStyle(wrapper);
// 		let leftVal = parseInt(getStyle.left);
// 		let topVal = parseInt(getStyle.top);
// 		wrapper.style.left = `${leftVal + movementX}px`;
// 		wrapper.style.top = `${topVal + movementY}px`;
// 	}
// 	header.addEventListener("mousedown", ()=>{
// 		header.classList.add("active");
// 		header.addEventListener("mousemove", onDrag);
// 	});
// 	document.addEventListener("mouseup", ()=>{
// 		header.classList.remove("active");
// 		header.removeEventListener("mousemove", onDrag);
// 	});
// });



// Drag div with ID function Started

// Make the DIV element draggable:

function dragElement(elmnt) {
	var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
	if (document.getElementById(elmnt.id + "header")) {
		// if present, the header is where you move the DIV from:
		document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
	} else {
		// otherwise, move the DIV from anywhere inside the DIV:
		elmnt.onmousedown = dragMouseDown;
	}

	function dragMouseDown(e) {
		e = e || window.event;
		e.preventDefault();
		// get the mouse cursor position at startup:
		pos3 = e.clientX;
		pos4 = e.clientY;
		document.onmouseup = closeDragElement;
		// call a function whenever the cursor moves:
		document.onmousemove = elementDrag;
	}

	function elementDrag(e) {
		e = e || window.event;
		e.preventDefault();
		// calculate the new cursor position:
		pos1 = pos3 - e.clientX;
		pos2 = pos4 - e.clientY;
		pos3 = e.clientX;
		pos4 = e.clientY;
		// set the element's new position:
		elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
		elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
	}

	function closeDragElement() {
		// stop moving when mouse button is released:
		document.onmouseup = null;
		document.onmousemove = null;
	}
}
// Drag div with ID function END Here

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

var startupData;

function basic_usr_detail(){
	
	usr_basic_detail = window.startupData['basic_data'];

	return usr_basic_detail
}

function current_contact_detail_from_html(){
	room_type = $('#contacts .active')[0]['attributes'][1].value;
	room = $('#contacts .active')[0]['attributes'][2].value;
	contact_name = $('#contacts .active .name')[0].innerHTML;
	rcvr_wallet_addresses = window.startupData['rooms'][room_type][room][contact_name]['wallet_address']
	rcvr_pmry_wallet = window.startupData['rooms'][room_type][room][contact_name]['primary_address'][0]

	return {'room_type':room_type, 'room':room, 'contact_name':contact_name, 'rcvr_pmry_wallet':rcvr_pmry_wallet, 'rcvr_wallet_addresses':rcvr_wallet_addresses};
}
//fetch user's chats

// window.onload = function fetch_chat_ids(fetcher){
function fetch_chat_ids(room_amount='indv'){
	// // console.log(fetcher);
	// $.ajax({
	// 	data: JSON.stringify({user:ethereum.selectedAddress.toUpperCase()}),
	// 	type: 'POST',
	// 	url: '/api/chat_ids',
	// 	dataType: 'json',
	// 	contentType: 'application/json',
	// 	headers:{'X-CSRFToken':csrf_token}
	// }).done(function(data){
	// 	console.log(data['chats'])
	// 	for(i=0;i<Object.keys(data.chats).length;i++){

	// 		current_chat_id = Object.keys(data.chats)[i];
	// 		console.log(current_chat_id)
	// 		users_in_room = data.chats[current_chat_id]

	// 		for(j=0;j<users_in_room.length;j++){
	// 			current_user = users_in_room[j]
	// 			console.log(users_in_room)
	// 			console.log(current_user)
	// 			console.log(currentAccount!=current_user)
	// 			if(currentAccount != current_user){
	// 				receivers_addr = current_user
	// 			}
	// 		}
	// 		console.log(current_chat_id,currentAccount,receivers_addr)
	// 		init_ws(current_chat_id,currentAccount,receivers_addr)
	// 	}
	// })


	currentAccount = ethereum.selectedAddress.toUpperCase();
	// room = $('#contacts .active')[0]['attributes'][2].value
	// {'room_type':room_type, 'room':room, 'contact_name':contact_name, 'rcvr_wallet_addresses':rcvr_wallet_addresses};
	contact_data_from_html = current_contact_detail_from_html();
	
	if(room_amount=='indv'){
		// init_ws(room, currentAccount, window.startupData['rooms'][room_type][room_list[j]][receiver_list[0]]['wallet_address']);
		init_ws(room, currentAccount, rcvr_wallet_addresses);
	}
	else if(room_amount=='all'){
		for(i=0;i<Object.keys(window.startupData['rooms']).length;i++){

			room_type = Object.keys(window.startupData['rooms'])[i];
			room_list = Object.keys(window.startupData['rooms'][room_type]);
			// console.log(room_type);
			if (room_type=='dm'){
				for(j=0;j<room_list.length;j++){
					receiver_list = Object.keys(window.startupData['rooms'][room_type][room_list[j]]);
	
					// Add Contact Tiles
					// $('<li onclick="view_conversation($(this).attr(\'room\'))" room='+room_list[j]+' address-receiver='+window.startupData['rooms'][room_type][room_list[j]][receiver_list[0]]['primary_address'][0]+' class="contact '+window.startupData['rooms'][room_type][room_list[j]][receiver_list[0]]['primary_address'][0]+'"><div class="wrap"><span class="contact-status"></span><img src="'+getRandomProfileimg()+'" alt="" /><div class="meta"><p class="name">'+receiver_list[0]+'</p><p class="preview"><span></span> </p></div></div></li>};').appendTo($('#contacts ul'));
					// $('<li onclick="view_conversation($(this).attr(\'room\'))" room_type='+room_type+' room='+room_list[j]+' address-receiver='+window.startupData['rooms'][room_type][room_list[j]][receiver_list[0]]['primary_address'][0]+' class="contact '+room_list[j]+'"><div class="wrap"><span class="contact-status"></span><img src="'+getRandomProfileimg()+'" alt="" /><div class="meta"><p class="name">'+receiver_list[0]+'</p><p class="preview"><span></span> </p></div></div></li>};').appendTo($('#contacts ul'));
					console.log('line249: room_name', room_list[j], 'rcvr_wlt_lst', window.startupData['rooms'][room_type][room_list[j]][receiver_list[0]]['wallet_address'])
					init_ws(room_list[j], currentAccount, window.startupData['rooms'][room_type][room_list[j]][receiver_list[0]]['wallet_address']);
					
				}
			}
	
			// else if(startupData['startup_data'][Object.keys(startupData['startup_data'])[i]]=='group'){
			// 	for(j=0;j<Object.keys(startupData['startup_data']['dm']).length;j++){
					
			// 		init_ws(Object.keys(startupData['startup_data']['dm'][j],currentAccount,receivers_addr));
			// 	}
			};
	}
	
}

//Get Chat JWTs
var chat_jwt;
function fetch_chat_jwt(){
	/*
	fetch('/api/fetch_chat_token',{
		method:'POST',
		headers:{'X-CSRFToken':csrf_token,'Content-type':"application/json"}
	})
	.then((response) => response.json())
	.then((responseData) => {
	chat_jwt = responseData.access_token
	console.log("Successfully Fetch Chat jwt",chat_jwt);
	return responseData;
	})
	.catch(error => console.warn(error));
}
*/
	$.ajax({
		type:'POST',
		url:'/api/fetch_chat_token',
		dataType:'json',
		contentType:'application/json',
		headers:{'X-CSRFToken':csrf_token}
	}).done(function(data){console.log("Successfully Fechted Chat JWT", data);chat_jwt=data.access_token})
}

// Fetch Communication Messages Between Sender and Receiver
// function fetch_message(fetcher, receiver){
function fetch_message(room){

	// $.ajax({
	// 	data : JSON.stringify({
	// 	networkID : ethereum.networkVersion,
	// 	fetcher : fetcher,
	// 	receiver : receiver,
	// 		}),
	// 	type : 'POST',
	// 	url : '/api/fetch_messages',
	// 	dataType: 'json',
	// 	contentType: 'application/json',
	// 	headers: {fetcher : fetcher, 'X-CSRFToken':csrf_token}
	// }).done(function(data){
	// 	displaymessages(data,ethereum.selectedAddress.toUpperCase(),receiver,fromws=false)
	// });

	room_type = $('#contacts .active')[0]['attributes'][1].value;
	conv_data = window.startupData['communication_data'][room_type][room]
	receiver_wallet_addresses = window.startupData['rooms'][room_type][room][$('#contacts .active .name')[0].innerHTML]['wallet_address']
	if (conv_data==undefined){
		conv_data={
			'you': {},
			'contact': {}
		}
	}

	displaymessages(conv_data, ethereum.selectedAddress.toUpperCase(), receiver_wallet_addresses, fromws=false);

};

// initiate WS connection

function init_ws(roomName,fetcher,rcvr_wallet_addr_lst){

	chatSocket = new WebSocket(
		'ws://'
		+ window.location.host
		+ '/ws/'
		+ roomName
		+ '/'
		+'?token=' + chat_jwt
	);
	
	chatSocket.onmessage = function(e){
		data = JSON.parse(e.data)
		console.log(data)
		console.log("message event received.")
		if(data.message.msg_status){
			// console.log('line 307: ', data,ethereum.selectedAddress.toUpperCase(),rcvr_wallet_addr_lst)
			// displaymessages(data,ethereum.selectedAddress.toUpperCase(),rcvr_wallet_addr_lst,fromws=true)
			displaymessages(data,ethereum.selectedAddress.toUpperCase(),rcvr_wallet_addr_lst,fromws=true)

		}
		else if(data.message.contact_status){
			updateContactStatus(data.message)
		}
	}

	chatSocket.onclose = function(e) {
		console.error('Chat socket closed unexpectedly');
	};
}

function send_ws_message(message){
	console.log("sending message event");
	contact_details = current_contact_detail_from_html();

	payload = {"msg_status": "SUCCESS", "color": "#2ecc71", "output": "Message Sent Successfully", "message_data": [{
		"room_type": contact_details["room_type"],
		"room": contact_details["room"],
		"sender": ethereum.selectedAddress.toUpperCase(),
		"receiver": contact_details["rcvr_wallet_addresses"],
		"message": message,
	}]};
	// console.log(payload);
	// // payload = {"type":"chat_message","message":{
	// // 	"msg_status": "SUCCESS", "color": "#2ecc71", "output": "Message Sent Successfully", "message_data": [{
	// // 		"sender": ethereum.selectedAddress.toUpperCase(), "nonce": 0, "receiver": receiver, "message": message, "networkId": 42, "timestamp": new Date().getTime()}]}}
	chatSocket.send(JSON.stringify(payload));
}


function startup_data(){

	$.ajax({
		data : JSON.stringify({
			current_WalletAddress : ethereum.selectedAddress.toUpperCase(),
			network_id : ethereum.networkVersion,
		}),
		type : 'POST',
		url : '/db/startup_data',
		dataType: 'json',
		contentType: 'application/json',
		headers: {'wallet_address':ethereum.selectedAddress,'X-CSRFToken':csrf_token}
	}).done(function(data) {
	$('#output').text(data.output).show();

	// Show Message Status Success/Failure
	if (data.error != undefined){
		console.log(data.error);
	}
	else{
		console.log(data.output);
	}

	// validity_chk_data = {'status':data.msg_status, 'color':data.color}
	console.log(data.data);
	update_status(data.msg_status, 2000);
	// document.getElementById("msg-send-confirm").textContent = data.msg_status;
	// document.getElementById("msg-send-confirm").style.color = data.color;

	// setTimeout(function() {
	// 	document.getElementById("msg-send-confirm").textContent = '';
	// }, 1000);
	
	if (data.msg_status == "SUCCESS"){
		window.startupData = data.data['startup_data'];
		// console.log(contact_list_data);
		// uuid = data.basic_UserData[0]; // Fetch uuid from the Server
		connected_wallets = startupData['basic_data']['wallet_address'];

		$('#uuid')[0].textContent = startupData['basic_data']['uuid'];
		uuid = window.startupData['basic_data']['uuid'];
		$('#user-Full_Name')[0].innerHTML = startupData['basic_data']['name'];

		// Set Green Border in primary Wallet Address

		
		$('<option style="color:'+getStatusColor('SUCCESS')+'" value="'+window.startupData['basic_data']['primary_address']+'"> '+window.startupData['basic_data']['primary_address']+' </option>').appendTo($('#CurrentUser_WalletAddresses'));

		for (let i = 0; i < connected_wallets.length; i++) {

			if (connected_wallets[i] != window.startupData['basic_data']['primary_address']){
				$('<option value="'+connected_wallets[i]+'"> '+connected_wallets[i]+' </option>').appendTo($('#CurrentUser_WalletAddresses'));
				console.log(connected_wallets[i]);
			}
			if (i+1==connected_wallets.length){
				fetch_contactList();
			}
		};
		
		// setTimeout(function() {
		// 	addNewContactForm()
		// 	$('#newReceiverAddress').val(null);
		// 	document.getElementById("newContactValidityStatus").textContent = '';
		// }, 2000);
	}
	
	
	});
};


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
function displaymessages(data,fetcher,receiver_wallet_addresses,fromws=false) {
	// console.log(data,fetcher,receiver)
	console.log('line 473',data)
	$('#output').text(data.output).show();
	receiver = $('#contacts ul .active')[0]['classList'][1];
	// Show Message Status Success/Failure
	if(fromws){
		data = data.message;
		//console.log(data);
		console.log(data.output);
		var msg_data_length = data.message_data.length;
		msg_data = data.message_data;
	}
	if ((fromws) && (data.message_data == undefined)){
		console.log(data.output);
	}
	else{
		if(fromws==false){
			msg_data = data;
			var msg_data_length = 0;
			for (let i = 0; i < Object.values(data).length; i++) {
				if (Object.keys(Object.values(data)[0]).length!=0){
					msg_data_length+=Object.keys(Object.values(data)[0]).length;
				}
			}
		}
		// validity_chk_data = {'status':data.msg_status, 'color':data.color}
		// update_status(data.msg_status, 1000);

		// document.getElementById("msg-send-confirm").textContent = data.msg_status;
		// document.getElementById("msg-send-confirm").style.color = data.color;

		// setTimeout(function() {
		// 	document.getElementById("msg-send-confirm").textContent = '';
		// }, 1000);

		// fetcher = ethereum.selectedAddress.toUpperCase();
		  
		

		//console.log("getting message data")
		if (msg_data_length!=0){
			// contact_basic_data = current_contact_detail_from_html();
			// // room_type = $('#contacts .active')[0]['attributes'][1].value;
			// // room = $('#contacts .active')[0]['attributes'][2].value
			// conv_data = window.startupData['communication_data'][contact_basic_data['room_type']][contact_basic_data['room']]
			// receiver_wallet_addresses = contact_basic_data['rcvr_wallet_addresses'];
			console.log(msg_data, fetcher.toUpperCase(), fromws);
			var contact_basic_data = current_contact_detail_from_html();

			if (fromws){

				// This if statement will run when user is sending live messages through web_Sockets
				update_status(data['msg_status'], 2000);
				fetcher = ethereum.selectedAddress.toUpperCase();
				// msg_data = data.message_data;

				for (let i = 0; i < msg_data.length; i++) {
					
					//console.log("looping")
					//console.log(msg_data[i]['sender'].toUpperCase() == fetcher.toUpperCase())
					// console.log('sender', msg_data[i]['sender'].toUpperCase(), 'fetcher', fetcher.toUpperCase(), 'receiver_wallet', receiver_wallet_addresses, fromws);

					if (fetcher.toUpperCase() == msg_data[i]['sender']){
						console.log("sender is fetcher")
						console.log('line 526', msg_data[i]['message']);

						// Update Local JSON Communication data
						window.startupData['communication_data'][contact_basic_data['room_type']][contact_basic_data['room']]['you'][msg_data[i]['timestamp']] = {'data': msg_data[i]['message']}

						var pt_msg = hex2ascii(msg_data[i]['message']);
						$('<li class="sent"><img src="'+$("#profile-img")[0]['src']+'" alt="" /><p>' + pt_msg + '</p></li>').appendTo($('.messages ul'));
						// $('#message').val(null);
						// if (i+1 == msg_data.length){
						var last_msg_sndr = 'You: ';
						// };
						
					}
					// else if (msg_data[i]['sender'].toUpperCase() in receiver_wallet_addresses){
					// else if (receiver_wallet_addresses.includes(msg_data[i]['sender'].toUpperCase())){
					else if (msg_data[i]['receiver'].includes(fetcher.toUpperCase())){
						console.log("sender is receiver")

						window.startupData['communication_data'][contact_basic_data['room_type']][contact_basic_data['room']]['contact'][msg_data[i]['timestamp']] = {'data': msg_data[i]['message']}
						var pt_msg = hex2ascii(msg_data[i]['message']);
						$('<li class="replies"><img src="'+$(".contact-profile #receiver-img")[0]['src']+'" alt="" /><p>' + pt_msg + '</p></li>').appendTo($('.messages ul'));
						// if (i+1 == msg_data.length){
						var last_msg_sndr =  '';
							
						// };
					}
					// else if (fetcher.toUpperCase() in receiver_wallet_addresses){
					else if (receiver_wallet_addresses.includes(fetcher.toUpperCase())){
					
						window.startupData['communication_data'][contact_basic_data['room_type']][contact_basic_data['room']]['contact'][msg_data[i]['timestamp']] = {'data': msg_data[i]['message']}
						var pt_msg = hex2ascii(msg_data[i]['message']);
						$('<li class="replies"><img src="'+$(".contact-profile #receiver-img")[0]['src']+'" alt="" /><p>' + pt_msg + '</p></li>').appendTo($('.messages ul'));
						// if (i+1 == msg_data.length){
						var last_msg_sndr =  '';
				
						// };
					};
					// // $('.'+receiver+' .wrap .meta .preview')[0]['innerHTML'] = '<span>'+last_msg_sndr+'</span>' + msg_data[msg_data.length-1]['message']
					$('.contact.active .preview').html('<span>'+last_msg_sndr+'</span>' + pt_msg);
					$(".messages").animate({ scrollTop: $(document).height() }, "fast");
				}
			}
			
			else{
				// Process Communication Data Fetched from database
				// contact_basic_data = current_contact_detail_from_html();
				// room_type = $('#contacts .active')[0]['attributes'][1].value;
				// room = $('#contacts .active')[0]['attributes'][2].value

				conv_data = window.startupData['communication_data'][contact_basic_data['room_type']][contact_basic_data['room']]
				receiver_wallet_addresses = contact_basic_data['rcvr_wallet_addresses'];
				console.log(msg_data, fetcher.toUpperCase(), fromws);

				comm_msg_data_list = Object.values(msg_data);
				comm_msg_data = (Object.keys(comm_msg_data_list[0])).concat(Object.keys(comm_msg_data_list [1])).sort();

				for (let i = 0; i < comm_msg_data.length; i++) {
					
					//console.log("looping")
					//console.log(msg_data[i]['sender'].toUpperCase() == fetcher.toUpperCase())
					// console.log('sender', msg_data[i]['sender'].toUpperCase(), 'fetcher', fetcher.toUpperCase(), 'receiver_wallet', receiver_wallet_addresses, fromws);


					if ((Object.keys(msg_data['you'])).includes(comm_msg_data[i])){
						console.log("sender is fetcher")
						var pt_msg = hex2ascii(msg_data['you'][comm_msg_data[i]]['data']);
						$('<li class="sent"><img src="'+$("#profile-img")[0]['src']+'" alt="" /><p>' + pt_msg + '</p></li>').appendTo($('.messages ul'));
						// $('#message').val(null);
						// if (i+1 == msg_data.length){
						var last_msg_sndr = 'You: ';
						// };
					}
					else if ((Object.keys(msg_data['contact'])).includes(comm_msg_data[i])){
						console.log("sender is receiver")
						var pt_msg = hex2ascii(msg_data['contact'][comm_msg_data[i]]['data']);
						$('<li class="replies"><img src="'+$(".contact-profile #receiver-img")[0]['src']+'" alt="" /><p>' + pt_msg + '</p></li>').appendTo($('.messages ul'));
						// if (i+1 == msg_data.length){
						var last_msg_sndr =  '';
							
						// };
					}
					// // $('.'+receiver+' .wrap .meta .preview')[0]['innerHTML'] = '<span>'+last_msg_sndr+'</span>' + msg_data[msg_data.length-1]['message']
					$('.contact.active .preview').html('<span>'+last_msg_sndr+'</span>' + pt_msg);
					$(".messages").animate({ scrollTop: $(document).height() }, "fast");
				}


			}
		}
	}
}

// Generate Random Static Sender Pic
$("#profile-img")[0]['src'] = getRandomProfileimg();

// var validity_chk_data={};

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

	// validity_chk_data = {'status':data.msg_status, 'color':data.color}
	update_status(data.msg_status, 2000);
	// document.getElementById("msg-send-confirm").textContent = data.msg_status;
	// document.getElementById("msg-send-confirm").style.color = data.color;

	// setTimeout(function() {
	// 	document.getElementById("msg-send-confirm").textContent = '';
	// }, 1000);

	
	});
	return true;
};

// Receiver Wallet Address List Box

function addNewContactForm() {
   if($("#new-contact-detail")[0].style.display == "" ) {
	$("#new-contact-detail")[0].style.display = 'block';
   } 
   else if ($("#new-contact-detail")[0].style.display == 'block' ) {
	$("#new-contact-detail")[0].style.display = "";
	$("#new-contact-detail")[0].style.top = "50%";
	$("#new-contact-detail")[0].style.left = "50%";

   };
 };


function newContact() {
	new_Receiver_Address = $("#newReceiverAddress").val();
	new_Receiver_Name = $("#newReceiverName").val();

    if($.trim(new_Receiver_Address) == '' || $.trim(new_Receiver_Name) == ''){
        return false;
    }

	$.ajax({
		data : JSON.stringify({
		networkID : ethereum.networkVersion,
		sender_address : ethereum.selectedAddress.toUpperCase(),
		receiver_address : new_Receiver_Address,
		receiver_name : new_Receiver_Name,
			}),
		type : 'POST',
		url : '/api/chk_addr_validity',
		dataType: 'json',
		contentType: 'application/json',
		headers: {'sender_address': ethereum.selectedAddress, 'receiver_address':new_Receiver_Address, 'receiver_name' : new_Receiver_Name, 'X-CSRFToken':csrf_token}
	}).done(function(data) {
	$('#output').text(data.output).show();

	// Show Message Status Success/Failure
	if (data.error != undefined){
		console.log(data.error);
	}
	else{
		console.log(data.output);
	}
	// validity_chk_data = {'status':data.msg_status, 'color':data.color}

	update_status(data.msg_status, 2000);
	// document.getElementById("msg-send-confirm").textContent = data.msg_status;
	// document.getElementById("msg-send-confirm").style.color = data.color;

	// setTimeout(function() {
	// 	document.getElementById("msg-send-confirm").textContent = '';
	// }, 1000);

	// Show status and colour & add contact
	// document.getElementById("newContactValidityStatus").style.color = validity_chk_data['color'];
	document.getElementById("newContactValidityStatus").style.color = getStatusColor(data.msg_status);


	// if (validity_chk_data['status'] == "SUCCESS"){
	if (data.msg_status == "SUCCESS"){
		document.getElementById("newContactValidityStatus").textContent = "Address is correct for current networkID: "+ethereum.networkVersion+" (Check details in console)";
		$('<li onclick="view_conversation($(this).attr(\'address-receiver\'))" address-receiver='+new_Receiver_Address+' class="contact '+new_Receiver_Address+'"><div class="wrap"><span class="contact-status"></span><img src="'+getRandomProfileimg()+'" alt="" /><div class="meta"><p class="name">'+new_Receiver_Name+'</p><p class="preview"><span>You:</span> Added Contact</p></div></div></li>};').appendTo($('#contacts ul'));
		
		setTimeout(function() {
			addNewContactForm()
			$('#newReceiverAddress').val(null);
			document.getElementById("newContactValidityStatus").textContent = '';
		}, 2000);
		
	}
	else if (data.msg_status == "FAILED"){
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
	// 		addNewContactForm()
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

// document.getElementById("settings").onclick = function () {
//     location.href = '/user/account';
// };


// Fetch StartUp Data

var uuid;

function fetch_StartUp_Data(){
	var data = {'msg_status': msg_status[1],  'color': color[1], 'output': 'Successfully Fetched, Basic User Data', 'basic_UserData':basic_usr_detail()};

	// $.ajax({
	// 	data : JSON.stringify({
	// 	current_WalletAddress : ethereum.selectedAddress.toUpperCase(),
	// 		}),
	// 	type : 'POST',
	// 	url : '/api/fetch_startup_data',
	// 	dataType: 'json',
	// 	contentType: 'application/json',
	// 	headers: {'current_WalletAddress' : ethereum.selectedAddress, 'X-CSRFToken':csrf_token}
	// }).done(function(data) {
	// $('#output').text(data.output).show();

	// // Show Message Status Success/Failure
	// if (data.error != undefined){
	// 	console.log(data.error);
	// }
	// else{
	// 	console.log(data.output);
	// }

	update_status(data.msg_status, 2000);	

	// document.getElementById("msg-send-confirm").textContent = data.msg_status;
	// document.getElementById("msg-send-confirm").style.color = data.color;

	// setTimeout(function() {
	// 	document.getElementById("msg-send-confirm").textContent = '';
	// }, 1000);

	// Show status and colour & add contact
	// document.getElementById("newContactValidityStatus").style.color = validity_chk_data['color'];
	
	if (data.msg_status == "SUCCESS"){

		
		// uuid = data.basic_UserData[0]; // Fetch uuid from the Server
		connected_wallets = data['basic_UserData']['wallet_address'];
		

		$('#uuid')[0].textContent = data['basic_UserData']['uuid'];
		uuid = data['basic_UserData']['uuid'];
		$('#user-Full_Name')[0].innerHTML = data['basic_UserData']['name'];

		for (let i = 0; i < connected_wallets.length; i++) {

			if (connected_wallets[i] == data['basic_UserData']['primary_address']){
				$('<option style="color:'+getStatusColor('SUCCESS')+'" value="'+data['basic_UserData']['primary_address']+'"> '+data['basic_UserData']['primary_address']+' </option>').appendTo($('#CurrentUser_WalletAddresses'));
			}
			else{
				$('<option value="'+connected_wallets[i]+'"> '+connected_wallets[i]+' </option>').appendTo($('#CurrentUser_WalletAddresses'));
			};
		};
		
		// setTimeout(function() {
		// 	addNewContactForm()
		// 	$('#newReceiverAddress').val(null);
		// 	document.getElementById("newContactValidityStatus").textContent = '';
		// }, 2000);
	}

	// });
};

// function fetch_uuid(){
// 	$.ajax({
// 		data : JSON.stringify({
// 		current_WalletAddress : ethereum.selectedAddress.toUpperCase(),
// 			}),
		
// 		type : 'POST',
// 		url : '/api/fetch_uuid',
// 		dataType: 'json',
// 		contentType: 'application/json',
// 		headers: {'current_WalletAddress' : ethereum.selectedAddress, 'X-CSRFToken':csrf_token}
// 	}).done(function(data) {
// 	$('#output').text(data.output).show();
// 		return data.uuid;
// 	});
// };

// Fetch Contact Lists

function fetch_contactList(){


	// $.ajax({
	// 	data : JSON.stringify({
	// 	current_WalletAddress : ethereum.selectedAddress.toUpperCase(),
	// 		}),
		
	// 	type : 'POST',
	// 	url : '/api/fetch_uuid',
	// 	dataType: 'json',
	// 	contentType: 'application/json',
	// 	headers: {'current_WalletAddress' : ethereum.selectedAddress, 'X-CSRFToken':csrf_token}
	// }).done(function(data) {
	// // $('#output').text(data.output).show();

	

	// 	// uuid = $('#uuid')[0].textContent
	// 	$.ajax({
	// 		data : JSON.stringify({
	// 		uuid : uuid,
	// 		current_WalletAddress : ethereum.selectedAddress.toUpperCase(),
	// 			}),
			
	// 		type : 'POST',
	// 		url : '/api/fetch_contacts',
	// 		dataType: 'json',
	// 		contentType: 'application/json',
	// 		headers: {'uuid': uuid, 'current_WalletAddress' : ethereum.selectedAddress, 'X-CSRFToken':csrf_token}
	// 	}).done(function(data) {
	// 	$('#output').text(data.output).show();

	// 	// Show Message Status Success/Failure
	// 	if (data.error != undefined){
	// 		console.log(data.error);
	// 	}
	// 	else{
	// 		console.log(data.output);
	// 	}

	// 	update_status(data.msg_status, 1000);

	// 	// document.getElementById("msg-send-confirm").textContent = data.msg_status;
	// 	// document.getElementById("msg-send-confirm").style.color = data.color;

	// 	// setTimeout(function() {
	// 	// 	document.getElementById("msg-send-confirm").textContent = '';
	// 	// }, 1000);

	// 	// Show status and colour & add contact
	// 	// document.getElementById("newContactValidityStatus").style.color = validity_chk_data['color'];
		
	// 	if (data.msg_status == "SUCCESS"){
	// 		contact_list_data = data.contact_list;

	// 		for (let i = 0; i < data.contact_list['totalContacts']; i++) {
	// 			// $('<li onclick="view_conversation($(this).attr(\'address-receiver\'))" address-receiver='+data.contact_list['contactsList'][i]['primary_wallet_address']+' class="contact '+data.contact_list['contactsList'][i]['primary_wallet_address']+'"><div class="wrap"><span class="contact-status"></span><img src="'+getRandomProfileimg()+'" alt="" /><div class="meta"><p class="name">'+data.contact_list['contactsList'][i]['name']+'</p><p class="preview"><span>SERVER:</span> Click to View Conversation</p></div></div></li>};').appendTo($('#contacts ul'));
	// 			$('<li onclick="view_conversation($(this).attr(\'address-receiver\'))" address-receiver='+data.contact_list['contactsList'][i]['primary_wallet_address']+' class="contact '+data.contact_list['contactsList'][i]['primary_wallet_address']+'"><div class="wrap"><span class="contact-status"></span><img src="'+getRandomProfileimg()+'" alt="" /><div class="meta"><p class="name">'+data.contact_list['contactsList'][i]['name']+'</p><p class="preview"><span></span> </p></div></div></li>};').appendTo($('#contacts ul'));
				
	// 		}
			
	// 		// setTimeout(function() {
	// 		// 	addNewContactForm()
	// 		// 	$('#newReceiverAddress').val(null);
	// 		// 	document.getElementById("newContactValidityStatus").textContent = '';
	// 		// }, 2000);
			
	// 	}

	// 	});
	// });


	// currentAccount = ethereum.selectedAddress.toUpperCase();

	for(i=0;i<Object.keys(window.startupData['rooms']).length;i++){

		room_type = Object.keys(window.startupData['rooms'])[i];
		room_list = Object.keys(window.startupData['rooms'][room_type]);
		// console.log(room_type);
		if (room_type=='dm'){
			for(j=0;j<room_list.length;j++){
				receiver_list = Object.keys(window.startupData['rooms'][room_type][room_list[j]]);

				// Add Contact Tiles
				// $('<li onclick="view_conversation($(this).attr(\'room\'))" room='+room_list[j]+' address-receiver='+window.startupData['rooms'][room_type][room_list[j]][receiver_list[0]]['primary_address'][0]+' class="contact '+window.startupData['rooms'][room_type][room_list[j]][receiver_list[0]]['primary_address'][0]+'"><div class="wrap"><span class="contact-status"></span><img src="'+getRandomProfileimg()+'" alt="" /><div class="meta"><p class="name">'+receiver_list[0]+'</p><p class="preview"><span></span> </p></div></div></li>};').appendTo($('#contacts ul'));
				$('<li onclick="view_conversation($(this).attr(\'room\'))" room_type='+room_type+' room='+room_list[j]+' address-receiver='+window.startupData['rooms'][room_type][room_list[j]][receiver_list[0]]['primary_address'][0]+' class="contact '+room_list[j]+'"><div class="wrap"><span class="contact-status"></span><img src="'+getRandomProfileimg()+'" alt="" /><div class="meta"><p class="name">'+receiver_list[0]+'</p><p class="preview"><span></span> </p></div></div></li>};').appendTo($('#contacts ul'));
				console.log('line249: room_name', room_list[j], 'rcvr_wlt_lst', window.startupData['rooms'][room_type][room_list[j]][receiver_list[0]]['wallet_address'])				
			}
		}

		// else if(startupData['startup_data'][Object.keys(startupData['startup_data'])[i]]=='group'){
		// 	for(j=0;j<Object.keys(startupData['startup_data']['dm']).length;j++){
				
		// 	}
		};

		// initiate after completion of the for loop
		if(i+1==Object.keys(window.startupData['rooms']).length){
			fetch_chat_ids('all');
		}

};



function fetch_CurrentUser_WalletAddress(){
	$.ajax({
		data : JSON.stringify({
		networkID : ethereum.networkVersion,
		sender_address : ethereum.selectedAddress.toUpperCase(),
		receiver_address : new_Receiver_Address,
		receiver_name : new_Receiver_Name,
			}),
		type : 'POST',
		url : '/api/chk_addr_validity',
		dataType: 'json',
		contentType: 'application/json',
		headers: {'sender_address': ethereum.selectedAddress, 'receiver_address':new_Receiver_Address, 'receiver_name' : new_Receiver_Name, 'X-CSRFToken':csrf_token}
	}).done(function(data) {
	$('#output').text(data.output).show();

	// Show Message Status Success/Failure
	if (data.error != undefined){
		console.log(data.error);
	}
	else{
		console.log(data.output);
	}
	validity_chk_data = {'status':data.msg_status, 'color':data.color};

	update_status(data.msg_status, 2000);

	// document.getElementById("msg-send-confirm").textContent = data.msg_status;
	// document.getElementById("msg-send-confirm").style.color = data.color;

	// setTimeout(function() {
	// 	document.getElementById("msg-send-confirm").textContent = '';
	// }, 1000);

	// Show status and colour & add contact
	document.getElementById("newContactValidityStatus").style.color = validity_chk_data['color'];

	if (validity_chk_data['status'] == "SUCCESS"){
		document.getElementById("newContactValidityStatus").textContent = "Address is correct for current networkID: "+ethereum.networkVersion+" (Check details in console)";
		$('<li onclick="view_conversation($(this).attr(\'address-receiver\'))" address-receiver='+new_Receiver_Address+' class="contact '+new_Receiver_Address+'"><div class="wrap"><span class="contact-status"></span><img src="'+getRandomProfileimg()+'" alt="" /><div class="meta"><p class="name">'+new_Receiver_Address+'</p><p class="preview"><span>You:</span> Added Contact</p></div></div></li>};').appendTo($('#contacts ul'));
		
		setTimeout(function() {
			addNewContactForm()
			$('#newReceiverAddress').val(null);
			document.getElementById("newContactValidityStatus").textContent = '';
		}, 2000);
		
	}
	else if (validity_chk_data['status'] == "FAILED"){
		document.getElementById("newContactValidityStatus").textContent = "Address is incorrect for current networkID: "+ethereum.networkVersion+" (Check details in console)";
	};

	});
}

function settings(){
	$(".settings-info-logo")[0].src = $("#profile-img")[0].src
	

	if ($(".settings")[0].style.display == ''){
		$(".settings")[0].style.display = 'block';
		$(".settings .settings-info .wrap-settings-info .settings-info-form .wrap-info-input input")[0].value = ethereum.selectedAddress;
		
		// Fetch Basic User Data
		$('#CurrentUser_WalletAddresses')[0].innerHTML='';
		fetch_StartUp_Data();
	}
	else if ($(".settings")[0].style.display == 'block'){
		$(".settings")[0].style.display = '';
		$(".settings")[0].style.top = "50%";
		$(".settings")[0].style.left = "50%";
	}
	
};


// Status Message Update


function getStatusColor(status){
	statusHexCodes = {
		'SUCCESS':'#2ecc71',
		'FAILED':'#e74c3c',
		'PENDING':'#f1c40f',
		'PROCESSING':'#f1c40f'
	}
	return statusHexCodes[status]
};

function update_status(status_detail) {
	// 'status_detail' is a array
	// which consist of ('SUCCESS/FAILED/PENDING/PROCESSING', 'Timeout')
	// Timeout => 1000 equals 1sec

	document.getElementById("msg-send-confirm").textContent = status_detail[0];
	document.getElementById("msg-send-confirm").style.color = getStatusColor(status_detail[0]);

	setTimeout(function() {
		document.getElementById("msg-send-confirm").textContent = '';
	}, status_detail[1]);

};


// Open Conversation
function view_conversation(room) {
// $('.contact').click(function() {
	// console.log($(data).attr("address-receiver"));
	// rcvr_name = $('.'+rcvr_addr+' .wrap .meta .name')[0]['innerText'];
	
	if (document.getElementsByClassName('contact active')[0] == undefined){
		// Add Active Class in currect contact
		document.getElementsByClassName(room)[0].classList.add("active");
	}
	else{
		// Remove Active Class from previous contact
		
		document.getElementsByClassName('contact active')[0].classList.remove('active');

		// Add Active Class in currect contact
		document.getElementsByClassName(room)[0].classList.add("active");

		
	}
	room_type = $('#contacts .active')[0]['attributes'][1].value;
	rcvr_addr = $('#contacts .active')[0]['attributes'][3].value;
	rcvr_img = $('.'+room+' .wrap img')[0]['currentSrc'];
	
	// Update Message Field
	document.getElementById('rcvr_name').innerHTML = Object.keys(window.startupData['rooms'][room_type][room])[0];
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
	


	// $.ajax({
	// 	data : JSON.stringify({
	// 	uuid : $('#uuid')[0].textContent,
	// 	current_WalletAddress : ethereum.selectedAddress.toUpperCase(),
	// 	rcvr_pmry_addr : rcvr_addr,
	// 		}),
	// 	type : 'POST',
	// 	url : '/api/fetch_indv_contact_details',
	// 	dataType: 'json',
	// 	contentType: 'application/json',
	// 	headers: {'current_WalletAddress': ethereum.selectedAddress, 'rcvr_pmry_addr':rcvr_addr, 'X-CSRFToken':csrf_token}
	// }).done(function(data) {
	// $('#output').text(data.output).show();

	// 	// Show Message Status Success/Failure
	// 	if (data.error != undefined){
	// 		console.log(data.error);
	// 	}
	// 	else{
	// 		console.log(data.output);
	// 	}

	// 	update_status(data.msg_status, 1000);

	// 	for (let i = 0; i < data.contact_detail['walletList'].length; i++) {
	// 		$('<option value="'+data.contact_detail["walletList"][i]["wallet_address"]+'"> '+data.contact_detail["walletList"][i]["wallet_address"]+' </option>').appendTo($('#Receiver_WalletAddresses'));

	// 	}

		

		
	// });
	
	// Update Receiver Wallet Address List
	// $("#rcvr-wallet-lst-box p")[0]['textContent'] = rcvr_addr;
	wallet_addr_list(0);
	document.getElementById('receiver').value = rcvr_addr;

	

	

	// Fetch Conversation Between the sender & Receiver
	fetch_message(room);

	// Make Socket Connection
	fetch_chat_ids();
};


// Receiver Wallet Address List Box
// var modal = null
 function wallet_addr_list(display_div=1) {

	document.getElementById('receiver-wallet-lst-img').src=$(".contact-profile #receiver-img")[0]['src'];

	if(($("#rcvr-wallet-lst-box")[0].style.display == "" ) || (($("#rcvr-wallet-lst-box")[0].style.display == "block") && display_div==0)) {
		if (display_div==1){
			$("#rcvr-wallet-lst-box")[0].style.display = 'block';
		}
		$('#Receiver_WalletAddresses')[0].innerHTML = '';
		active_rcvr_addr = $('#contacts .active')[0]['attributes'][3].value;
		active_rcvr_name = $('#contacts .active .name')[0].innerHTML;

		// $.ajax({
		// 	data : JSON.stringify({
		// 	uuid : $('#uuid')[0].textContent,
		// 	current_WalletAddress : ethereum.selectedAddress.toUpperCase(),
		// 	rcvr_pmry_addr : active_rcvr_addr,
		// 		}),
		// 	type : 'POST',
		// 	url : '/api/fetch_indv_contact_details',
		// 	dataType: 'json',
		// 	contentType: 'application/json',
		// 	headers: {'current_WalletAddress': ethereum.selectedAddress, 'rcvr_pmry_addr':active_rcvr_addr, 'X-CSRFToken':csrf_token}
		// }).done(function(data) {
		// $('#output').text(data.output).show();
	
		// 	// Show Message Status Success/Failure
		// 	if (data.error != undefined){
		// 		console.log(data.error);
		// 	}
		// 	else{
		// 		console.log(data.output);
		// 	}
	
		update_status('SUCCESS', 2000);
		// $('#Receiver_WalletAddresses')[0].innerHTML = '';
		var current_contact_details = current_contact_detail_from_html();
		console.log('line 1253', current_contact_details['rcvr_wallet_addresses'])
		if (current_contact_details['rcvr_wallet_addresses'].length<=1){
			
			$('#Receiver_WalletAddresses')[0].outerHTML = '<select id=\"Receiver_WalletAddresses\" name=\"Receiver Connected Wallets\" size=\"'+1+'\" multiple=\"multiple\"></select>';
		}
		else{
			$('#Receiver_WalletAddresses')[0].outerHTML = '<select id=\"Receiver_WalletAddresses\" name=\"Receiver Connected Wallets\" size=\"'+2+'\" multiple=\"multiple\"></select>';
		};
		
		for (let i = 0; i < current_contact_details['rcvr_wallet_addresses'].length; i++) {
			console.log('line 1262', current_contact_details['rcvr_wallet_addresses'][i])
			if (current_contact_details['rcvr_wallet_addresses'][i] == current_contact_details['rcvr_pmry_wallet']){
				$('<option style="color:'+getStatusColor('SUCCESS')+'" value="'+current_contact_details['rcvr_pmry_wallet']+'"> '+current_contact_details['rcvr_pmry_wallet']+' </option>').appendTo($('#Receiver_WalletAddresses'));
			}
			else{
				$('<option value="'+current_contact_details['rcvr_wallet_addresses'][i]+'"> '+current_contact_details['rcvr_wallet_addresses'][i]+' </option>').appendTo($('#Receiver_WalletAddresses'));
			};

		}
		// });


	} 
	else if ($("#rcvr-wallet-lst-box")[0].style.display == 'block' ) {
		if (display_div==1){
			$("#rcvr-wallet-lst-box")[0].style.display = "";
			$('#Receiver_WalletAddresses')[0].innerHTML = '';
		}
		$("#rcvr-wallet-lst-box")[0].style.top = "50%";
		$("#rcvr-wallet-lst-box")[0].style.left = "50%";
		

	}
//    if(modal === null) {
//      document.getElementById("rcvr-wallet-lst-box").style.display = "block";
//      modal = true
//    } else {
//      document.getElementById("rcvr-wallet-lst-box").style.display = "none";
//      modal = null
//    }

	


	
};

// On Startup run the Functions

// var startup_loaded = 0;
// while (startup_loaded==0){


// window.addEventListener('load', function() { // NOT `DOMContentLoaded`
// 	// Do something about HTML document
// 	// fetch_StartUp_Data();
// 	// fetch_contactList();
// });

function load_on_startup(){
	// // try{
	// $.when(fetch_StartUp_Data()).then(
	// 	fetch_contactList()
	// );

	
	// const start_data = startup_data().then(fetch_chat_ids()).catch((error) => {fetch_chat_ids()})
	startup_data();
	fetch_chat_jwt();
	// fetch_chat_ids();
		// fetch_chat_ids
		// ).then(
		// 	fetch_contactList
		// );
	
	// fetch_chat_ids();
	// fetch_StartUp_Data();
	// fetch_contactList();
	// startup_data();
	// $.when(fetch_StartUp_Data()).then(function(){
	// 	fetch_contactList();
	// })
	// fetch_contactList();
		// startup_loaded=1;
	// }
	// catch(e){};
		
};
