function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }

const jobs = document.getElementById("jobs")

document.getElementById("goToJobs").onclick = function () {
  ScrollingTo(document.documentElement, jobs, 1250);   
}

  function ScrollingTo(element, to = 0, duration= 1000, scrollToDone = null) {
    const start = element.scrollTop;
    const change = to - start;
    const increment = 20;
    let currentTime = 0;

    const animateScroll = (() => {

      currentTime += increment;

      const val = Math.easeInOutQuad(currentTime, start, change, duration);

      element.scrollTop = val;

      if (currentTime < duration) {
        setTimeout(animateScroll, increment);
	} else {
		if (scrollToDone) scrollToDone();
	}
    });

    animateScroll();
  };

  Math.easeInOutQuad = function (t, b, c, d) {

    t /= d/2;
    if (t < 1) return c/2*t*t + b;
    t--;
    return -c/2 * (t*(t-2) - 1) + b;
  };