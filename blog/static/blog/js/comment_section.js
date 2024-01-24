//Handles the no reload of the comment pages for seemless viewing of comments
$(document).on('click', '.pagination a', function (event) {
    event.preventDefault();

    var url = $(this).attr('href');

    $.get(url, function (data) {
        console.log('AJAX success:', data);

        // Targets the card body element via data-page attribute
        var targetCardBody = $('.card-body[data-page]');

        // Replace the HTML content inside the target card-body
        targetCardBody.html(data.comment_html);

        // Update the URL in the browser without reloading the page
        window.history.pushState({}, '', url);
    }).fail(function (xhr, status, error) {
        console.error('AJAX error:', status, error);
    });
});


// Auto scroll to comment section after comment posted
$(document).ready(function () {
    var hash = window.location.hash;
    if (hash) {
        // Scroll to the section with the specified hash
        $('html, body').animate({
            scrollTop: $(hash).offset().top
        }, 800);
    }
});