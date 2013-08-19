var package = {
    "name" : null,
    "email" : null,
    "phone" : null,
    "message" : null
};


for (var i in package)
{
    var id = $('#id_' + i);
    console.log(id.val());
    if (id.val() === '')
    {
        alert("Fill out " + i);
        break;
    }
    
    package[i] = id.val();
}


$('input[type=submit]').on('click', function(event){
    event.preventDefault();
    
    console.log(arguments);

});




// Click Event
$('input[type=submit]').on('click', function(e){
    e.preventDefault();
    //console.log(arguments);
    
    var package = {
    "name" : null,
    "email" : null,
    "phone" : null,
    "message" : null
};


for (var i in package)
{
    var id = $('#id_' + i);
    console.log(id.val());
    if (id.val() === '')
    {
        alert("Fill out " + i);
        break;
    }
    
    package[i] = id.val();
}
    console.log(package);
    var json_obj =  JSON.stringify(package);
    console.log(json_obj);

});



// Finished The Ajax on click event and POST and RESPONSE
$('input[type=submit]').on('click', function(e){
    e.preventDefault();
    //console.log(arguments);
    
    var package = {
    "name" : null,
    "email" : null,
    "phone" : null,
    "message" : null
};


for (var i in package)
{
    var id = $('#id_' + i);
    console.log(id.val());
    if (id.val() === '')
    {
        alert("Fill out " + i);
        break;
    }
    
    package[i] = id.val();
}
    var json_obj =  JSON.stringify(package);
    
    $.ajax({
        type: "POST",
        url: "/posted/",
        data: json_obj,
        error: function(server_data)
        {
            console.log("DANGER DANGER SERVER ERROR");
        },
        
        success: function(server_data)
        {
            console.log(server_data);
        }
        
    });


});
