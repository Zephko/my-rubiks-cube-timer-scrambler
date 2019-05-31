//Define vars to hold time values
let tenths_second = 0;
let seconds = 0;
let minutes = 0;

//define vars to hold display values
let display_seconds = 0;
let display_minutes = 0;

//var to hold setInterval() function
let interval = null;

//holds stopwatch status
let status = "stopped";

//stopwatch function(logic to determine when to increment next value etc.)
function stopWatch() {
    tenths_second++;

    //logic to determine when to increment value
    if (tenths_second === 100) {
        tenths_second = 0;
        seconds++;

        if (seconds === 60) {
            seconds = 0;
            minutes++;
        }
    }

    if (seconds < 10) {
        display_seconds = '0' + seconds.toString()
    } else {
        display_seconds = seconds
    }

    if (minutes < 10) {
        display_minutes = '0' + minutes.toString()
    } else {
        display_minutes = minutes
    }


    //display updated time values to user
    document.getElementById("display").innerHTML = display_minutes + ":" + display_seconds + "." + tenths_second;
}


function startStop() {
    if (status === "stopped") {
        interval = window.setInterval(stopWatch, 10);
        document.getElementById("startStop").innerHTML = "Stop";
        status = "started";
    } else {
        window.clearInterval(interval);
        document.getElementById("startStop").innerHTML = "Start";
        status = "stopped";
    }
}

function reset() {
    tenths_second = 0;
    seconds = 0;
    minutes = 0;
    document.getElementById("display").innerHTML = "00:00:00"
}
