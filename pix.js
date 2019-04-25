var position=1;

function prev(){
    changeout(position);
    setTimeout("changein(position)", 500);
    var befo=position;
    setTimeout(function(){document.getElementById(befo).style.display="none";}, 450);
    position--;
    if(position==0)
    {
        position=maxpos;
    }
    document.getElementById("control").innerHTML=""+position+"/"+maxpos;
    
}
function next(){
    changeout(position);
    setTimeout("changein(position);", 450);
    var befo=position;
    setTimeout(function(){document.getElementById(befo).style.display="none";}, 450);
    position++;
    if(position==maxpos+1)
    {
        position=1;
    }
    document.getElementById("control").innerHTML=""+position+"/"+maxpos;
    
}


function changein(id) {
    document.getElementById(id).style.display="";
    setTimeout(function(){document.getElementById(id).style.opacity="1";}, 50);
}
function changeout(id) {
    document.getElementById(id).style.opacity="0"; 
}