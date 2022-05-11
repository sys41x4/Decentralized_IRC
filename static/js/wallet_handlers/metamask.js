let currentAccount = null;
// const MERCHANT_ACCOUNT = '0x8cceF537C24864f566b29Fa11ed0aDC113B7BAF9'
let g_wallet_address = null

let wallet_name = 'Wallet';
let price = 0;
// let msg_type = 'free';
/**
    To Generate a random ID
    source:- https://stackoverflow.com/a/1349426/275002
**/
function makeid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() *
 charactersLength));
   }
   return result;
}

// get cookie Value by name
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrf_token = getCookie('csrftoken');

function utf8ToHex(str) {
      return Array.from(str).map(c =>
        c.charCodeAt(0) < 128 ? c.charCodeAt(0).toString(16) :
        encodeURIComponent(c).replace(/\%/g,'').toLowerCase()
      ).join('');
}


function detectMetaMask() {
    if (typeof window.ethereum !== 'undefined') {
        return true
    } else {
        return false
    }
}




// $(document).ready(function() {
//     $('#send-message').on('submit', function(event) {
//       $.ajax({
//          data : JSON.stringify({
//             sender : g_wallet_address,
//             receiver: $('#receiver').val(),
//             message: $('#message').val(),
//                 }),
//             type : 'POST',
//             url : '/api/send_msg',
//             dataType: 'json',
//             contentType: 'application/json',
//             headers: {'Wallet_Address':g_wallet_address}
//            })
//        .done(function(data) {
//          $('#output').text(data.output).show();
//      });
//      console.log('Receiver ='+$('#receiver').val())
//      event.preventDefault();
//      });
// });

function set_wallet_address(wallet_address) {
    g_wallet_address = wallet_address
    fetch('/api/set_wallet',
    {method:'POST',
    headers:{'Content-type':'application/json','Wallet_address':wallet_address,'X-CSRFToken':csrf_token},
    body:JSON.stringify({"wallet_address":wallet_address})})
}

function addOrder(wallet_address,tx,name,invoice_id) {
    $.post("/api/add_order",
                        { wallet_address: wallet_address, tx: tx,name:name,invoice_id:invoice_id },
                         function(data, status){
                                if(data == 'OK') {
                                    alert('Order placed successfully')
                                } else {
                                    alert('Order could not place successfully')
                                }
    });
}
function getmessage(download=false){
    url = "/api/messages"
    if(download){
        window.open(url + "?download=true","_blank")
    }
    fetch(url,{method:"GET"})
    .then(response => {return response.json()})
    .then(data => {console.log(JSON.stringify(data))})
}

function connect() {
    console.log('Calling connect()')
    ethereum
    .request({ method: 'eth_requestAccounts' })
    .then(handleAccountsChanged)
    .catch((err) => {
    if (err.code === 4001) {
        // EIP-1193 userRejectedRequest error
        // If this happens, the user rejected the connection request.
        console.log('Please connect with Wallet.');
        $('#status').html('You refused to connect with Wallet')
        show_message_UI(null)
    } else {
        console.error(err);
        $('#status').html('Wallet is locked')
        $('#status-detail').html('Unlock Your wallet to sync & send Message')
        show_message_UI(null)
    }
    });
}


function get_api_response(err_occur){

    


    if(err_occur == 1){
        document.getElementById("msg-send-confirm").textContent = 'FAILED';
        document.getElementById("msg-send-confirm").style.color = '#e74c3c';
        setTimeout(function() {
            document.getElementById("msg-send-confirm").textContent = '';
        }, 1000);
        err_occur = 0;
    }
    else if (err_occur == 0){
        message = $('#message').val();
        // receiver =  $('#receiver').val();

        $.ajax({
        	data : JSON.stringify({
        	networkID : ethereum.networkVersion,
            sender_address : ethereum.selectedAddress,
        	receiver_address : $('#receiver').val(),
        		}),
        	type : 'POST',
        	url : '/api/chk_addr_validity',
        	dataType: 'json',
        	contentType: 'application/json',
		headers: {'sender_address': ethereum.selectedAddress, 'receiver_address':$('#receiver').val(), 'X-CSRFToken':csrf_token}
        }).done(function(data) {
        $('#output').text(data.output).show();

        // Show Message Status Success/Failure
        if (data.error != undefined){
        	console.log(data.error);
        }
        else{
        	console.log(data.output);
        }
        

        if (data.msg_status=='SUCCESS'){
            // PUSH data to IPFS & WEB2 Storage
            $.ajax({
                data : JSON.stringify({
                   sender : g_wallet_address,
                   receiver: $('#receiver').val(),
                   message: $('#message').val(),
                       }),
                   type : 'POST',
                   url : '/api/send_msg',
                   dataType: 'json',
                   contentType: 'application/json',
                   headers: {'Wallet_Address':g_wallet_address, 'Receiver':$('#receiver').val(),'X-CSRFToken':csrf_token}
                  })
              .done(function(data) {
                $('#output').text(data.output).show();
            
                // Show Message Status Success/Failure
                if (data.error != undefined){
                    console.log(data.error);
                }
            
                document.getElementById("msg-send-confirm").textContent = data.msg_status;
                document.getElementById("msg-send-confirm").style.color = data.color;
            
                setTimeout(function() {
                    document.getElementById("msg-send-confirm").textContent = '';
                }, 1000);
                
            
                
                    $('<li class="sent"><img src="'+$("#profile-img")[0]['src']+'" alt="" /><p>' + message + '</p></li>').appendTo($('.messages ul'));
                    $('#message').val(null);
                    $('.contact.active .preview').html('<span>You: </span>' + message);
                    $(".messages").animate({ scrollTop: $(document).height() }, "fast");
                });
            }
            else if (data.msg_status=='FAILED'){
                document.getElementById("msg-send-confirm").textContent = data.msg_status;
                document.getElementById("msg-send-confirm").style.color = data.color;
            
                setTimeout(function() {
                    document.getElementById("msg-send-confirm").textContent = '';
                    $('#message').val(null);
                }, 1000);
                
            };
        
        });
    };


    
};


$(document).ready(function() {

    $('#send-message').on('submit', function(event) {
        message = $('#message').val();
        receiver =  $('#receiver').val();
         
        if(($.trim(message) == '') || ($.trim(receiver) == '')){
            return false;
        }

        $.ajax({
            data : JSON.stringify({
                chk_access : 'api'
                   }),
               type : 'POST',
               url : '/api/access_chk',
               dataType: 'json',
               contentType: 'application/json',
               //contentType: 'application/x-www-form-urlencoded',
               headers: {'chk-access' : 'api', 'X-CSRFToken':csrf_token}
              })
          .done(function(data) {});

        // // If message == '' then it will not send request to the api
        // let name = $(this).data("name")
        // message = $('#message').val();
         
        // if($.trim(message) == '') {
        //     return false;
        // }
        // console.log('Message Type', msg_type)
        // // err_occur = 0;
        // if (msg_type!='paid'){
        //     get_api_response(err_occur);
        // }

        console.log("Entering to Tx send zone")
        event.preventDefault();
     });
    
    
    $('.free-msg').click(function() {
        message = $('#message').val();
        receiver =  $('#receiver').val();
         
        if(($.trim(message) == '') || ($.trim(receiver) == '')) {
            return false;
        }
        get_api_response(0);
    });

    $('.paid-msg').click(function() {

        // If message == '' then it will not send request to the api
        message = $('#message').val();
        receiver =  $('#receiver').val();

        if(($.trim(message) == '') || ($.trim(receiver) == ''))  {
            return false;
        }


        price = $(this).data("price")
        wallet_name = $(this).data("name")
        // msg_type = $(this).data("msg_type")
        // console.log(name,price)
        eth_wei = ethUnit.toWei(price, 'ether');
        console.log('RESULT ='+eth_wei)
        console.log('Wallet ='+currentAccount)
        console.log('RESULT IN HEX ='+eth_wei.toString(16))
        let invoice_id = 'INV-'+makeid(5)
        console.log(invoice_id)

        const transactionParameters = {
              nonce: '0x00', // ignored by MetaMask
              gasPrice: '0x09184e72a000', // customizable by user during MetaMask confirmation.
              gas: '0x22710', // customizable by user during MetaMask confirmation.
              to: $('#receiver').val(), // Required except during contract publications.
              from: g_wallet_address, // must match user's active address.
              value: eth_wei.toString(16),
              data:utf8ToHex($('#message').val()),
              networkID: '0x3', // Used to prevent transaction reuse across blockchains. Auto-filled by MetaMask.
        };
            console.log(transactionParameters)
            
        if(currentAccount != null) {
            document.getElementById("msg-send-confirm").textContent = 'Processing ...';
            document.getElementById("msg-send-confirm").style.color = '#f1c40f';
            const txHash = ethereum.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            })
            .then(function(tx){
                console.log('Transaction Hash ='+tx)
                console.log('Wallet Inside ='+g_wallet_address)
                console.log('Product Name ='+wallet_name)
                console.log('Invoice ID = '+invoice_id)
                console.log('Message = '+$('#message').val())
                get_api_response(0)
                // addOrder(currentAccount,tx,name,invoice_id)
            })
            .catch((error) => {
                console.log('Error during the transaction')
                console.log(error);
                get_api_response(1)

            });
            // 
        }

    });

    //  m = detectMetaMask()
    // if(m) {
    //     $('#enablewallet').removeClass('meta-gray')
    //     $('#enablewallet').addClass('meta-normalcurrentAccount')
    //     $('#enablewallet').attr('disabled',false)
    //     connect()

    // } else {
    //     $('#enablewallet').attr('disabled',true)
    //     $('#enablewallet').removeClass('meta-normal')
    //     $('#enablewallet').addClass('meta-gray')
    // }

    // $('#enablewallet').click(function() {
    //     connect()
    // });

     
});


// function paid_msg(name, price){

//     // If message == '' then it will not send request to the api
//     message = $('#message').val();
        
//     if($.trim(message) == '') {
//         return false;
//     }


//     // let price = $(this).data("price")
//     // let name = $(this).data("name")
//     console.log(name,price)
//     eth_wei = ethUnit.toWei(price, 'ether');
//     console.log('RESULT ='+eth_wei)
//     console.log('Wallet ='+currentAccount)
//     console.log('RESULT IN HEX ='+eth_wei.toString(16))
//     let invoice_id = 'INV-'+makeid(5)
//     console.log(invoice_id)

//     const transactionParameters = {
//             nonce: '0x00', // ignored by MetaMask
//             gasPrice: '0x09184e72a000', // customizable by user during MetaMask confirmation.
//             gas: '0x22710', // customizable by user during MetaMask confirmation.
//             to: $('#receiver').val(), // Required except during contract publications.
//             from: g_wallet_address, // must match user's active address.
//             value: eth_wei.toString(16),
//             data:utf8ToHex($('#message').val()),
//             networkID: '0x3', // Used to prevent transaction reuse across blockchains. Auto-filled by MetaMask.
//         };
//         console.log(transactionParameters)
        
//         if(currentAccount != null) {
//             const txHash = ethereum.request({
//                 method: 'eth_sendTransaction',
//                 params: [transactionParameters],
//             })
//             .then(function(tx){
//                 console.log('Transaction Hash ='+tx)
//                 console.log('Wallet Inside ='+g_wallet_address)
//                 console.log('Product Name ='+name)
//                 console.log('Invoice ID = '+invoice_id)
//                 console.log('Message = '+$('#message').val())
//                 // addOrder(currentAccount,tx,name,invoice_id)
//             })
//             .catch((error) => {
//                 console.log('Error during the transaction')
//                 console.log(error)
//             });
//         }
// }

$( document ).ready(function() {

    m = detectMetaMask()
    if(m) {
        $('#enablewallet').removeClass('meta-gray')
        $('#enablewallet').addClass('meta-normalcurrentAccount')
        $('#enablewallet').attr('disabled',false)
        connect()

    } else {
        $('#enablewallet').attr('disabled',true)
        $('#enablewallet').removeClass('meta-normal')
        $('#enablewallet').addClass('meta-gray')
    }

    $('#enablewallet').click(function() {
        connect()
    });

//     $('.btn-buy').click(function() {
//         let price = $(this).data("price")
//         let name = $(this).data("name")
//         console.log(name,price)
//         eth_wei = ethUnit.toWei(price, 'ether');
//         console.log('RESULT ='+eth_wei)
//         console.log('Wallet ='+currentAccount)
//         console.log('RESULT IN HEX ='+eth_wei.toString(16))
//         let invoice_id = 'INV-'+makeid(5)
//         console.log(invoice_id)

//         const transactionParameters = {
//               nonce: '0x00', // ignored by MetaMask
//               gasPrice: '0x09184e72a000', // customizable by user during MetaMask confirmation.
//               gas: '0x22710', // customizable by user during MetaMask confirmation.
//               to: MERCHANT_ACCOUNT, // Required except during contract publications.
//               from: currentAccount, // must match user's active address.
//               value: eth_wei.toString(16),
//               data:utf8ToHex(invoice_id),
//               networkID: '0x3', // Used to prevent transaction reuse across blockchains. Auto-filled by MetaMask.
//             };
//             console.log(transactionParameters)

//             if(currentAccount != null) {
//                 const txHash = ethereum.request({
//                  method: 'eth_sendTransaction',
//                  params: [transactionParameters],
//                 })
//                 .then(function(tx){
//                     console.log('Transaction Hash ='+tx)
//                     console.log('Wallet Inside ='+currentAccount)
//                     console.log('Product Name ='+name)
//                     console.log('Invoice ID = '+invoice_id)
//                     addOrder(currentAccount,tx,name,invoice_id)
//                 })
//                 .catch((error) => {
//                     console.log('Error during the transaction')
//                     console.log(error)
//                 });
//             }

//     });
})

function handleAccountsChanged(accounts) {
    console.log('Calling HandleChanged')
    show_message_UI('show')
    if (accounts.length === 0) {
        console.log('Please connect to MetaMask.');
    } else if (accounts[0] !== currentAccount) {
        currentAccount = accounts[0];
        $('#enablewallet').html('<img width="50" height="50" src="data:image/jpeg;base64,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" alt=""> Connected')
        $('#wallet_address').val(currentAccount)
        set_wallet_address(currentAccount)
        $('#status').html('')

        if(currentAccount != null) {
            // Set the button label
            $('#enablewallet').html('<img width="50" height="50" src="data:image/jpeg;base64,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" alt=""> Connected')            
        }
    }
    load_on_startup();
    console.log('WalletAddress in HandleAccountChanged = '+currentAccount);
    // fetch_contactList();
    // Function Exist in 'beta_msg.js' file
    
}


// If user didn't connect with the wallet then it will not display the message UI
function show_message_UI(modal) {
    if(modal === null) {
      document.getElementsByClassName("message-ui")[0].style.display = "none";
      document.getElementById("wallet-not-connect").style.display = "block";
    } else {
     document.getElementsByClassName("message-ui")[0].style.display = "block";
     document.getElementsByClassName('wallet-access-chk')[0].style.display = "none"
    }
  }