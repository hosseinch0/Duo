let x = document.getElementById('circle');
let y = document.getElementById('icon');
let m = document.getElementById('login');
document.getElementById('burgermenu').onclick =sidemenu;
let n=document.getElementById('burgermenu');
function button(){
    if( x.className === "circle"){
        
        x.className="after";
        y.className="material-symbols-outlined";
        y.innerHTML="arrow_insert";
        
    
        
    }
    else{
        x.className="circle";
        y.className="material-symbols-outlined";
        y.innerHTML="arrow_outward";
   
    }
    if(m.className==="loginform"){

        m.className="signform";
    }
    else{
        m.style.animationName='none';
        m.className="loginform";
    }
}
if(screen.width<'992 px')
{
    document.getElementById('sidebar').style.display='none';
}

function sidemenu(){
    if(n.innerHTML==="menu_open")
    {
        document.getElementById('sidebar').style.display='block';
        document.getElementById('sidebar').style.right='0';
        document.getElementById('sidebar').style.animationName ='opensidemenu';
        document.getElementById('burgermenu').innerHTML = "cancel"; 
    }
    else{
        document.getElementById('sidebar').style.right='-40%';
        document.getElementById('sidebar').style.animationName ='closesidemenu';
        document.getElementById('burgermenu').innerHTML = "menu_open";
       // document.getElementById('sidebar').style.display='none';
    }    
}


