    var CITY;
    var CITY_ID;
    var IntervalId = 0;
    var i =  1;

    document.onkeyup = function (e) 
    {    
        
        e = e || window.event;
        if (e.keyCode === 13)
        {
            $( "#butt" ).fadeTo("slow",0.25);
            $( "#butt" ).fadeTo("slow",1.00);
            CITY  = document.getElementById("My_str").value;
            if(CITY.length == 0)
            {
                alert("Заполните поле: Город");
            }
            else
            {
                i = 1;
                clearInterval(IntervalId);
                $('#output').show();
                Take_Id();
            }
        }
        return false;
    }    


    $('#butt').click(function()
    {   
        $( "#butt" ).fadeTo("slow",0.25);
        $( "#butt" ).fadeTo("slow",1.00);        
        CITY  = document.getElementById("My_str").value;
        if(CITY.length == 0)
        {
            alert("Заполните поле: Город");
        }
        else
        {
            i = 1;
            clearInterval(IntervalId);
            $('#output').show();
            Take_Id();
        }
    });

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
var csrftoken = getCookie('csrftoken')
    
    function Take_Id()
    {
         $.ajax
        ({
            type: 'POST',
            url: '/take_id/',  
            cache: false, 
            data: 
            {
                'city': CITY,
                'csrfmiddlewaretoken': csrftoken,

            },
            success: function(res_id)
            {
                if(res_id.city == undefined)
                {
                    clearInterval(IntervalId);
                    $('#output').html("<h3>Города </h3>"+CITY+ "<h3>нет</h3>");
                }
                else
                {
                    CITY_ID = res_id.Id;
                    i = 1;
                    clearInterval(IntervalId);
                    $('#output').show();
                    show();
                    var timeInterval = 60000;
                    IntervalId = setInterval(show,timeInterval);
                }
            }
        });
        return false;
    }                      
    function show()  
    {      
        $.ajax
        ({
            type: 'POST',
            url: '/weather_info/',  
            cache: false, 
            data: 
            {
                'id': CITY_ID,
                'csrfmiddlewaretoken': csrftoken,
            },
            success: function(responseData)
            {
                
                    
                    $('#output').html(
                    '<h3> Город: <u>'+ responseData.city + '</u></h3><h4>' + responseData.stat + '</h4><h4> Температура: '+ responseData.temperature + '&#176;C;</h4><h4> Скорость ветра: '+ responseData.wind_speed +'м/с;</h4><h4>Направление ветра: </h4><h4>'+responseData.wind_der+'</h4><h4> Влажность: '+ responseData.humidity +'%;</h4><h4> Давление: '+responseData.press + 'мм. рт. ст.</h4><h4>Количество обновлений:</h4>' + i);
                    i += 1;
            }                                  
        });  
        return false;
    }  