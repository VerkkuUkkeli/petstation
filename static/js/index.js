// page js initialisation
$( document ).ready(function() {
    console.log("Petstation index page.");

    // set handler for audio dropdown form submit
    $("#audio-form").submit(function(event) {
        // parse XMLHttpRequest string
        var request = "/play_audio/" + String($("#audio-dropdown").val());

        // make XMLHttpRequest
        var xhttp = new XMLHttpRequest();
        xhttp.open("GET", request, true);
        xhttp.send();
        event.preventDefault(); // prevent form submission (causes page refresh)
    });
});
