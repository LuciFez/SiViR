
const myForum = document.getElementById("search-form");

myForum.addEventListener("submit", (e) => {
    e.preventDefault();
    let q = document.getElementById("q").value;
    let p = document.getElementById("platform").value;
    let params ='?q='+q+'&p='+p;

    let inputs = document.getElementById('criteria-platform').getElementsByTagName('input');
    let i;
    for (i = 0; i < inputs.length; i++) {
         params += '&' + inputs[i].name + '=' + inputs[i].value;
    }

    inputs = document.getElementById('criteria-platform').getElementsByTagName('select');
    for (i = 0; i < inputs.length; i++) {
         params += '&' + inputs[i].name + '=' + inputs[i].value;
    }

    fetch('/search' +params,
        {credentials: "include"}
    ).then( response => {
         if( response.status === 200) {
                response.json().then(function (response) {
                    var videos = response['videos'];
                    var element = document.getElementsByClassName("grid")[0];
                    element.innerHTML = '';
                    for (let i = 0; i < videos.length; i++) {
                        console.log(videos[i]);
                        element.innerHTML +=
                            '<div class="item youtube_rec">' +
                            '<div class="content">    ' +
                            '<div class="logo_platform"> </div>' +
                            '<a href="/watch?v='+ videos[i]["id"] +'"><img src="' + videos[i]["thumbnail"] +'"></a>' +
                            '    <h2>' + videos[i]["title"] + '</h2>' +
                            '    <p>' + videos[i]["description"] + '</p>' +
                            '</div>' +
                            '</div> ';
                     }
                });
                    resizeAllGridItems();
                    setTimeout(function(){
                    resizeAllGridItems()
                    }, 500);
            }
            else {
                response.json().then( function (response) {
                    alert(response.message);
                });
            }
            }).catch(function (error) {
        console.error(error);
    })
});


window.onclick = function(event) {
  if (event.target.matches('#dropdown-button')) {
      document.getElementById("dropdown").classList.toggle("show");
  }else if (event.target.matches('#username')){
      document.getElementById("dropdown-username").classList.toggle("show");
  }
  else if(event.target.matches('.dropdown-content') || event.target.matches('.dropdown-content-element')) {
      return false
  }
  else  {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
              //openDropdown.classList.remove('show');
          }
      }
  }
}


function resizeGridItem(item){
   let grid = document.getElementsByClassName("grid")[0];
   let rowHeight = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-auto-rows'));
   let rowGap = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-row-gap'));
   let rowSpan = Math.ceil((item.querySelector('.content').getBoundingClientRect().height + rowGap) / (rowHeight + rowGap));
   item.style.gridRowEnd = "span "+rowSpan ;
}

function resizeAllGridItems(){
   let allItems = document.getElementsByClassName("item");
   let x;
   for( x=0;x<allItems.length;x++){
      resizeGridItem(allItems[x]);
   }
}


window.addEventListener("resize", resizeAllGridItems);

setTimeout(function(){
    fetch('/recommendations',
        {credentials: "include"}
    ).then( response => {
         if( response.status === 200) {
                response.json().then(function (response) {
                    var videos = response['videos'];
                    var element = document.getElementsByClassName("grid")[0];
                    element.innerHTML = '';
                    for (let i = 0; i < videos.length; i++) {
                        console.log(videos[i]);
                        element.innerHTML +=
                            '<div class="item youtube_rec">' +
                            '<div class="content">' +
                            '<div class="logo_platform"> </div>' +
                            '<a href="/watch?v='+ videos[i]["id"] +'"><img src="' + videos[i]["thumbnail"] +'"></a>' +
                            '    <h2>' + videos[i]["title"] + '</h2>' +
                            '    <p>' + videos[i]["description"] + '</p>' +
                            '</div>' +
                            '</div> ';
                     }
                });
                    resizeAllGridItems();
                    setTimeout(function(){
                    resizeAllGridItems()
                    }, 500);
            }
            else {
                response.json().then( function (response) {
                    alert(response.message);
                });
            }
            }).catch(function (error) {
           console.error(error);});
        resizeAllGridItems();

        const selectElement = document.querySelector('.ice-cream');




}, 150);



const platform = document.getElementById("platform");

platform.addEventListener('change', (event) => {
    var criteria = document.getElementById("criteria-platform");

    if (event.target.value == "youtube") {
        criteria.innerHTML =
            '<select name="order" class="dropdown-content-element">'+
                        '<option value="relevance">Relevance</option>'+
                        '<option value="date">Date</option>'+
                        '<option value="rating">Rating</option>'+
                        '<option value="title">Title</option>'+
                        '<option value="videoCount">Video Count</option>'+
            '</select>';
    } else if (event.target.value == "vimeo") {
        criteria.innerHTML = "Vimeo";
    } else {
        criteria.innerHTML = "You can only search tags on Instagram";
    }
 });


