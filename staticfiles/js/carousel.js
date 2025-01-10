const testimonialCard = document.querySelectorAll('.testimonial-card');
const prevButton = document.getElementById('prev-btn');
const nextButton = document.getElementById('next-btn');

let currentIndex = 0;

function showTestimonial(index) {
  debugger;
  testimonialCard.forEach((card, i) => {
    if (i === index) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
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