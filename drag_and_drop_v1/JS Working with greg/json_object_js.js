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