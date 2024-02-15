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
/* Hiding the labels for cleaner look */
$('label[for="id_default_country"]').hide();
$('label[for="id_profile_image"]').hide();
$('#hint_id_new_password1').hide();


//JS for dealing with custom input field for profile image
$('#new-image').change(function () {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});

//JS for dealing with zooming of profile image
function zoomIn(element) {
    element.classList.add('zoomed');
}

function zoomOut(element) {
    element.classList.remove('zoomed');
}