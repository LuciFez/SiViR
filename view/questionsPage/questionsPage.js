function reset() {
  document.getElementsById("questions-from").reset();
  window.location.assign("http://localhost:8000/firstPage");
}

function redirect() {
    var q1 = document.querySelector('input[name="question1"]:checked').value;
    var q2 = document.querySelector('input[name="question2"]:checked').value;
    var q3 = document.querySelector('input[name="question3"]:checked').value;
  
    document.cookie = " question1Response = " + q1;
    document.cookie = " question2Response = " + q2;
    document.cookie = " question3Response = " + q3;

    window.location.replace("firstPage");
    return false;
}
