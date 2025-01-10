const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("TestimonalForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated testimonial's ID upon click.
* - Fetches the content of the corresponding testimonial.
* - Populates the `testimonialText` input/textarea with the testimonial's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_testimonial/{testimonialId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let testimonialId = e.target.getAttribute("testimonial_id");
    let testimonialContent = document.getElementById(`comment${testimonialId}`).innerText;
    testimonialText.value = testimonialContent;
    submitButton.innerText = "Update";
    testimonialForm.setAttribute("action", `edit_testimonial/${testimonialId}`);
  });
}