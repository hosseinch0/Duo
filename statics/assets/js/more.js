let ball = document.getElementById('ball');
let icon = document.getElementById('icon');
let color = document.getElementById('color');
let navbar = document.getElementById('nav');
const link = document.getElementById('theme');
const bgphoto = document.getElementById('background').src;
let menu = document.getElementById('menu');
let sidenav = document.getElementById('sidenavbar');


menu.onclick = sidemenu;

document.getElementById('photo').style.backgroundImage ='url(' + bgphoto +')';


ball.onclick = switchthem;

function switchthem()
{
    if(icon.className=="fa-solid fa-sun")
    {
        ball.style.left="75px";
        icon.className="fa-solid fa-moon";
        ball.style.animationName='ball';
        link.href = "/css/moredarkmode.css";
    }
    else{
        ball.style.left = '3px';
        ball.style.animationName = 'reverseball';
        icon.className = "fa-solid fa-sun";
        link.href = "/css/more.css";
    }
}
function sidemenu (){
    if(sidenav.style.right=="0px")
    {
        sidenav.style.right='-350px';
        sidenav.style.animationName='closesidemenu';
    }
    else{
        sidenav.style.right='0px'
        sidenav.style.animationName='opensidemenu';
    }
}
