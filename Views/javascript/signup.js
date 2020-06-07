
const myForum = document.getElementById("signupForm");

myForum.addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);

    fetch('signup', {
        method: 'post',
        body: formData
    }) .then(function (response) {
        return response.json();
    }) .then (function (response) {
        console.log(response);
        if (response.message !== "Success!") {
            alert(response.message)
        } else {
            location.href = '\\'
        }

    }) .catch(function (error) {
        console.error(error);
    })
});