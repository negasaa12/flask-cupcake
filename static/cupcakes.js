

// This should return an HTML page (via render_template). This page should be entirely static (the route should just render the template, without providing any information on cupcakes in the database). It should show simply have an empty list where cupcakes should appear and a form where new cupcakes can be added.

// Write Javascript (using axios and jQuery) that:

// queries the API to get the cupcakes and adds to the page
// handles form submission to both let the API know about the new cupcake and updates the list on the page to show it
// (You do not need to use WTForms to make this form; this is a possibility in the further study.)


$('.delete-cupcake').click(deleteCupcake)


async function deleteCupcake(){
    const id = $(this).data('id')
    await axios.delete(`/api/cupcakes/${id}`)
   $(this).parent().remove()
}