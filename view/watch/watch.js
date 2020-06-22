

const myForum = document.getElementById("search-form");

myForum.addEventListener("submit", (e) => {
    e.preventDefault();

    var q = document.getElementById("q").value;
    console.log(q);

    fetch('/search?q='+q,
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
                    }, 100);
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
              openDropdown.classList.remove('show');
          }
      }
  }
}


function resizeGridItem(item){
   grid = document.getElementsByClassName("grid")[0];
   rowHeight = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-auto-rows'));
   rowGap = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-row-gap'));
   rowSpan = Math.ceil((item.querySelector('.content').getBoundingClientRect().height+rowGap)/(rowHeight+rowGap));
   item.style.gridRowEnd = "span "+rowSpan ;
}

function resizeAllGridItems(){
   allItems = document.getElementsByClassName("item");
   for(x=0;x<allItems.length;x++){
      resizeGridItem(allItems[x]);
   }
}

window.onload = resizeAllGridItems();


window.addEventListener("resize", resizeAllGridItems);

setTimeout(function(){
    resizeAllGridItems()
}, 10);
