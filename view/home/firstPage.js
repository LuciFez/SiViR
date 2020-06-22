
function openDropdown() {
    document.getElementById("dropdown").classList.toggle("show");
}

window.onclick = function(event) {
    if(!event.target.matches('.user-container')) {
        var dropdowns = document.getElementsByClassName("dropdown-items");
        var i;
        for(i=0; i<dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if(openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function clear(ceva) {

}

function search() {
    var q = document.getElementById("q").value;
    console.log(q)

    fetch('/search?q='+q,
        {credentials: "include"}
    ).then( response => {
         if( response.status === 200) {
                response.json().then(function (response) {
                    var videos = response['videos']
                    var element = document.getElementById("youtube");
                    element.innerHTML = '';
                    for (let i = 0; i < videos.length; i++) {
                        console.log(videos[i])
                        element.innerHTML +=
                            '<div class="video">' +
                            '    <a href="/watch?v='+ videos[i]["id"] +'"><img src="' + videos[i]["thumbnail"] +'"></a>' +
                            '    <h1>' + videos[i]["title"] + '</h1>' +
                            '    <p>' + videos[i]["description"] + '</p>' +
                            '</div> ';
                     }

                });
            }
            else {
                response.json().then( function (response) {
                    alert(response.message);
                });
            }
            }).catch(function (error) {
        console.error(error);
    })
}
