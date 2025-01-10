document.addEventListener('DOMContentLoaded', () => {
    bindCarouselEvents();
  });
  
  function bindCarouselEvents() {
    const testimonialCards = document.querySelectorAll('.testimonial-card');
    const prevButton = document.getElementById('prev-btn');
    const nextButton = document.getElementById('next-btn');
  
    if (testimonialCards.length > 0 && prevButton && nextButton) {
      let currentIndex = 0;
  
      // Show the initial testimonial
      showTestimonial(currentIndex, testimonialCards);
  
      // Next Button Click Handler
      nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex === testimonialCards.length - 1) ? 0 : currentIndex + 1;
        showTestimonial(currentIndex, testimonialCards);
      });
  
      // Previous Button Click Handler
      prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex === 0) ? testimonialCards.length - 1 : currentIndex - 1;
        showTestimonial(currentIndex, testimonialCards);
      });
    } else {
      console.error('Testimonial cards or buttons not found!');
    }
  }
  
  // Function to display the selected testimonial
  function showTestimonial(index, testimonialCards) {
    testimonialCards.forEach((card, i) => {
      card.style.display = (i === index) ? 'block' : 'none';
    });
  }