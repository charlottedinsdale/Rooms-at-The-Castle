const editButtons = document.getElementsByClassName("btn-edit");
const testimonialText = document.getElementById("id_content");
const testimonialForm = document.getElementById("TestimonialForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

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
    let testimonialContent = document.getElementById(`testimonial${testimonialId}`).innerText;
    testimonialText.value = testimonialContent;
    submitButton.innerText = "Update";
    testimonialForm.setAttribute("action", `edit_testimonial/${testimonialId}`);
  });
}

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
      let testimonialId = e.target.getAttribute("testimonial_id");
      console.log('testimonial id: ', testimonialId)
      deleteConfirm.href = `delete_testimonial/${testimonialId}`;
      deleteModal.show();
  });
}
