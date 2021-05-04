function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }

$("#goToJobs").click(function(event) {
  event.preventDefault();
  $('html, body').animate({
      scrollTop: $("#jobs").offset().top
  }, 2000);
});