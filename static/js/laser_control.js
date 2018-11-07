// page js initialisation
$( document ).ready(function() {
    console.log("Petstation laser control page.");
});

// keydown events
// transmit key state to server through XMLHttpRequest
$(document).keydown(function(e){
    var keycode = e.which
    console.log(keycode);
    switch (keycode) {
        case 87: // w
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/w1", true);
            xhttp.send();
            break;
        case 65: // a
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/a1", true);
            xhttp.send();
            break;
        case 83: // s
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/s1", true);
            xhttp.send();
            break;
        case 68: // d
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/d1", true);
            xhttp.send();
            break;
        case 13: // enter
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/laser1", true);
            xhttp.send();
            break;
        default:
            break;
    }
});

// keyup events
// transmit key state to server through XMLHttpRequest
$(document).keyup(function(e){
    var keycode = e.which
    switch (keycode) {
        case 87: // w
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/w0", true);
            xhttp.send();
            break;
        case 65: // a
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/a0", true);
            xhttp.send();
            break;
        case 83: // s
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/s0", true);
            xhttp.send();
            break;
        case 68: // d
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/d0", true);
            xhttp.send();
            break;
        case 13: // enter
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/laser0", true);
            xhttp.send();
            break;
        default:
            break;
    }});
