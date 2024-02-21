let countrySelected = $('#id_default_country').val();
if (!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
$('#id_default_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});
// Add text to the labels before hiding them
$('label[for="id_default_country"]').text('Choose default country:');
$('label[for="id_profile_image"]').text('Choose profile image:');
$('#hint_id_new_password1').text('Enter your new password:');

// Hide the labels for cleaner look
$('label[for="id_default_country"]').addClass('d-none');
$('label[for="id_profile_image"]').addClass('d-none');
$('#hint_id_new_password1').addClass('d-none');


//JS for dealing with custom input field for profile image
$('#id_profile_image').change(function () {
    var file = $('#id_profile_image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});

//JS for dealing with zooming of profile image
function zoomIn(element) {
    element.classList.add('zoomed');
}

function zoomOut(element) {
    element.classList.remove('zoomed');
}