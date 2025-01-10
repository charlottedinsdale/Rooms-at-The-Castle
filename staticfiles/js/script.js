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

const testimonialCard = document.querySelectorAll('.testimonial-card');
const prevButton = document.getElementById('prev-button');
const nextButton = document.getElementById('next-button');

let currentIndex = 0;

function showTestimonial(index) {
  testimonialCard.forEach((testimonialCard, i) => {
    if (i === index) {
      testimonialCard.style.display = 'block';
    } else {
      testimonialCard.style.display = 'none';
    }
  });
}

function showNextTestimonial() {
  currentIndex++;
  if (currentIndex >= testimonialCard.length) {
    currentIndex = 0;
  }
  showTestimonial(currentIndex);
}

function showPreviousTestimonial() {
  currentIndex--;
  if (currentIndex < 0) {
    currentIndex = testimonialCard.length - 1;
  }
  showTestimonial(currentIndex);
}

prevButton.addEventListener('click', showPreviousTestimonial);
nextButton.addEventListener('click', showNextTestimonial);

showTestimonial(currentIndex);