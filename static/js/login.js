var globalAccount;
var globalSignature;
var globalNonce;
var csrf;

window.onload = function() {
    // web3 instance for signature recovery
    const web3 = new Web3(window.ethereum);
    var csrf = document.getElementsByName('csrfmiddlewaretoken')[0].content;

    if (typeof window.ethereum !== 'undefined') {
        console.log('MetaMask is installed!');
    } else {
        console.log('MetaMask is not installed!');
    }

    const signButton = document.querySelector('.signButton');
    signButton.addEventListener('click', () => {
        signMessage();
    });

    var nonce = function getNonce() {
        $.ajax({
            type: 'GET',
            url: '/api/generate_nonce',
            headers: {
                'X-CSRFToken': csrf
            },
            dataType: 'json',
            success: function(data) {
                console.log(data.nonce)
                globalNonce = data.nonce
            }
        })
    }()

    async function signMessage() {
       // const message = globalNonce;
        try {
            const from = globalAccount;
            console.log('from : ' + from);
           // const msg = `${bops.from(message, 'utf8').toString('hex')}`;
            //console.log('msg : ' + msg);
            const sign = await ethereum.request({
                method: 'personal_sign',
                params: [globalNonce, from, 'Random text'],
            });
            console.log('sign : ' + sign);
            globalSignature = sign;
            init_login();
        } catch (err) {
            console.error(err);
        }
    }

    function init_login(){
        $.ajax({
            type:'POST',
            url:'/api/web3login',
            dataType: 'json',
            headers:{'X-CSRFToken':csrf},
            contentType: 'application/json',
            data:JSON.stringify({"signature":globalSignature,"wallet_address":globalAccount}),
            success: function(data){
                id_token = data.id_token
                redirect_uri = data.redirect_uri
                sessionStorage.setItem("id_token",id_token)
                window.location.href = redirect_uri;
            }
        })
    }

    
}

var acc  =  async function getAccount() {
        const accounts = await ethereum.request({
            method: 'eth_requestAccounts'
        });
        const account = accounts[0];
        globalAccount = accounts[0];
        //showAccount.innerHTML = "Account: " + account;
        //  document.getElementById("metaMaskState").innerHTML = JSON.stringify(window.ethereum._state);
    }()