
const myForum = document.getElementById("loginForum");

myForum.addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    var myArticle = document.querySelector('article');



    fetch('getkey', {
        method: 'get'
    })  .then(response => response.text())
        .then(function (response) {
        var publicKey = forge.pki.publicKeyFromPem(response);

        var encrypted = publicKey.encrypt(formData.get("passw"), "RSA-OAEP", {
            md: forge.md.sha256.create(),
            mgf1: forge.mgf1.create()
        });

        var base64 = forge.util.encode64(encrypted);
        document.cookie = "passw  =" + base64 + ";" ;
        document.cookie =" uname = " + formData.get("uname");

        fetch('login', {
            method: 'GET', // aci trebuie post cu body username si pass, fara cookie
            credentials: "include"
        }).then ( response => {
            if( response.status === 200) {
                response.text().then(function (response) {
                    document.cookie =  "jwt  =" + response + ";" ;
                    location.href="questionsPage";
                });

            }
            else {
                response.json().then( function (response) {
                    alert(response.message);
                });
            }
        })
        .catch(function (error) {
        console.error(error);
    })
        }) .catch(function (error) {
        console.error(error);
        });});