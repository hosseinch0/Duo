let rightarrow = document.getElementById('right');
let leftarrow = document.getElementById('left');

let leftdoublearrow = document.getElementById('leftres');
let rightdoublearrow = document.getElementById('rightres');

let turnon1 = document.getElementById('turnon1');
let turnoff1 = document.getElementById('turnoff1');

let turnon2 = document.getElementById('turnon2');
let turnoff2 = document.getElementById('turnoff2');

let turnon3 = document.getElementById('turnon3');
let turnoff3 = document.getElementById('turnoff3');

let turnon = document.getElementById('turnon');
let turnoff = document.getElementById('turnoff');

let turnon4 = document.getElementById('turnon4');
let turnoff4 = document.getElementById('turnoff4');

turnon.onclick= turn;
turnoff.onclick = off;

turnon2.onclick= turn2;
turnoff2.onclick = off2;

turnon1.onclick= turn1;
turnoff1.onclick = off1;

turnon3.onclick= turn3;
turnoff3.onclick = off3;

turnon4.onclick= turn4;
turnoff4.onclick = off4;

rightarrow.onclick = rightside;
leftarrow.onclick = leftside;

rightdoublearrow.onclick = responrightside;
leftdoublearrow.onclick = responleftside;
        


function leftside(){
    var firstbox = document.getElementById('one');
    var secondbox = document.getElementById('two');
    var thirdbox = document.getElementById('three');
 
    
 
    
        firstbox.style.animationName='reverseanimationone';
        firstbox.style.left='71.25%';

        secondbox.style.animationName='reverseanimationtwo';
        secondbox.style.width='25%';
        secondbox.style.height='50%';
        secondbox.style.left='3.75%';
        secondbox.style.filter='blur(3px)';
      


        thirdbox.style.animationName= 'reverseanimationthree';
        thirdbox.style.width='35%';
        thirdbox.style.height='80%';
        thirdbox.style.left='32.5%';
        thirdbox.style.filter='none';


        firstbox.id='three';
        secondbox.id ='one';
        thirdbox.id ='two';
    
   
}

function rightside(){

    var firstbox = document.getElementById('one');
    var secondbox = document.getElementById('two');
    var thirdbox = document.getElementById('three');

   
        
    firstbox.style.animationName = 'animationone';
    firstbox.style.width ='35%';
    firstbox.style.height = '80%';
    firstbox.style.left ='32.5%';
    firstbox.style.filter='none';
    

    secondbox.style.animationName ='animationtwo';
    secondbox.style.width='25%';
    secondbox.style.height='50%';
    secondbox.style.left= '71.25%';
    secondbox.style.filter='blur(3px)';
   

    thirdbox.style.animationName = 'animationthree';
    thirdbox.style.left='3.75%';

    thirdbox.id ='one';
    secondbox.id ='three';
    firstbox .id = 'two';

};

function responrightside()
{
    var box = document.getElementById('solo');
    var box4 = document.getElementById('sec');
    box.style.animationName='responsiveswitchright';
    box.style.width ='60%';
    box.style.left='20%';
    box.style.zIndex='-5';
    box.style.height='60%';
    box.style.filter='blur(3px)';
    box4.style.animationName='responsiveswitchleft';

    box4.style.width='75%';
    box4.style.left = '12.5%';
    box4.style.zIndex= '5';
    box4.style.height= '80%';
    box4.style.filter='blur(0px)';

    box.id ='sec';
    box4.id ='solo';



}

function responleftside()
{
    var box = document.getElementById('solo');
    var box4 = document.getElementById('sec');
    box.style.animationName='reverseresponsiveswitchleft';
    box4.style.animationName='reverseresponsiveswitchright';
    box.style.filter='blur(3px)';
    box.style.width ='60%';
    box.style.left='20%';
    box.style.zIndex='-5';
    box.style.height='60%';

    box4.style.width='75%';
    box4.style.left = '12.5%';
    box4.style.zIndex= '5';
    box4.style.height= '80%';
    box4.style.filter='blur(0px)';

    box.id ='sec';
    box4.id ='solo';
}
function turn(){
    document.getElementById('up').style.display='flex';
    document.getElementById('up').style.animationName='up';
}

function off(){
    document.getElementById('up').style.display='none';

}
function turn2(){
    document.getElementById('up2').style.display='flex';
    document.getElementById('up2').style.animationName='up';
}

function off2(){
    document.getElementById('up2').style.display='none';

}


function turn3(){
    document.getElementById('up3').style.display='flex';
    document.getElementById('up3').style.animationName='up';
}

function off3(){
    document.getElementById('up3').style.display='none';

}

function turn4(){
    document.getElementById('up4').style.display='flex';
    document.getElementById('up4').style.animationName='up';
}

function off4(){
    document.getElementById('up4').style.display='none';

}


function turn1(){
    document.getElementById('up1').style.display='flex';
    document.getElementById('up1').style.animationName='up';
}

function off1(){
    document.getElementById('up1').style.display='none';

}
let ball= document.getElementById('ball');
let icon= document.getElementById('icon');
let menuicon= document.getElementById('menu');

let navbot = document.getElementById('navbot');

ball.onclick = switchtheme;

menuicon.onclick = showmenu;
function switchtheme(){

    if(icon.innerHTML=="dark_mode")
    {
        ball.style.left='3px';
        icon.innerHTML='light_mode';
        ball.style.animationName='reverseball';
        document.getElementById('body').style.backgroundColor='white';
    }
    else
    {
        ball.style.left='75px';
         icon.innerHTML='dark_mode';
         ball.style.animationName='ball';
         document.getElementById('body').style.backgroundColor='#323232';
    }
}  
function showmenu(){

    if(navbot.style.top=="-24vh")
    {
        navbot.style.animationName='showmenu';
        navbot.style.top='10vh';
        document.getElementById('nav').style.height='34vh';
    }
    else{
        navbot.style.animation='hidemenu';
        navbot.style.top='-24vh';
        document.getElementById('nav').style.height='10vh';
    }
}      
