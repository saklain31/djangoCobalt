/**
 *
 * Created by Fahim Arefin on 7/4/2017.
 */

var lat=0;
var lng=0;

//var x=document.getElementById("error");
function callLocation() {
    var txt='failed';

    swal({
        text: "Is the delivery address same as your current location ? (Please allow us to access your location)",
        type: 'info',
        showCancelButton: true,
        confirmButtonColor: '#FEDC3D',
        cancelButtonColor: '#A9A9A9',
        confirmButtonText: 'Yes',
        cancelButtonText: 'No'
    }).then(function () {
            getLocation();
            txt='thanks'
        },function (dismiss) {
            // dismiss can be 'cancel', 'overlay',
            // 'close', and 'timer'

            x.innerHTML= "Sorry, we could not get your location!";

        }

    );
    console.log(txt);
}


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        console.log( "Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    lat=position.coords.latitude;
    lng=position.coords.longitude;
    console.log(lat+ " "+lng);
}


function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            x.innerHTML = "User denied the request for Geolocation.";
            break;
        case error.POSITION_UNAVAILABLE:
            x.innerHTML = "Location information is unavailable.";
            break;
        case error.TIMEOUT:
            x.innerHTML = "The request to get user location timed out.";
            break;
        case error.UNKNOWN_ERROR:
            x.innerHTML = "An unknown error occurred.";
            break;
    }
}

function getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2) {
  var R = 6371; // Radius of the earth in km
  var dLat = deg2rad(lat2-lat1);  // deg2rad below
  var dLon = deg2rad(lon2-lon1); 
  var a = 
    Math.sin(dLat/2) * Math.sin(dLat/2) +
    Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * 
    Math.sin(dLon/2) * Math.sin(dLon/2)
    ; 
  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
  var d = R * c; // Distance in km
  return d;
}

function deg2rad(deg) {
  return deg * (Math.PI/180)
}


function pageLoadingTesting(){
    alert("page loaded"); 
}