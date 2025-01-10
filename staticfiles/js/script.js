window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80 ) {
    document.getElementById("castle-title").style.fontSize = "1.5rem";
    document.getElementById("slogan").classList.add("hidden");
  } else {
    document.getElementById("castle-title").style.fontSize = "2.5rem";
    document.getElementById("slogan").classList.remove("hidden");
  }
}




