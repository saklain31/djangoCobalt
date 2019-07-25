console.log("loaded");
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// var csrftoken1 = $('input[name="csrfmiddlewaretoken"]').val();
//console.log("TEST ",csrftoken1);
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


function sampleGetRequest()
{
    var username = document.getElementById('username').value;
    console.log("Changing ",username);
    $.ajax({
        url: '/ajax/validate_username/',
        data: {
            'username': username
        },

        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                swal("A user with this username already exists.");
            }
            else
                console.log("Available")
        }
    });
}

function samplePostRequest(data)
{
    $.ajax({
        type:"POST",
        url: '/ajax/validate_zip/',
        data: {
            'zip': data
        },
        dataType: 'json',
        success: function (response) {
            console.log("Received ",response)
        }
    });
}

var csrftoken = getCookie('csrftoken');