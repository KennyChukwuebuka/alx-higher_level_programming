$(document).ready(function() {
    function fetchTranslation() {
        // Get the language code from the input
        var languageCode = $("#language_code").val();
        
        // Fetch the translation from the API
        $.get("https://www.fourtonfish.com/hellosalut/hello/", { lang: languageCode }, function(data) {
            // Display the translation in the div#hello
            $("#hello").text(data.hello);
        });
    }

    $("#btn_translate").click(fetchTranslation);

    $("#language_code").keypress(function(event) {
        if (event.which == 13) { // Enter key pressed
            fetchTranslation();
        }
    });
});