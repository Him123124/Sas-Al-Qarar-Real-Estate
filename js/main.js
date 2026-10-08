(function(){
var R=document.documentElement,cur='ar',$=function(i){return document.getElementById(i)};
R.classList.add('js');
function ls(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}}
function setLang(l){
  cur=l;R.lang=l;R.dir=l==='ar'?'rtl':'ltr';
  document.querySelectorAll('[data-ar]').forEach(function(e){e.innerHTML=e.getAttribute('data-'+l)});
  document.querySelectorAll('[data-ph-ar]').forEach(function(e){e.placeholder=e.getAttribute('data-ph-'+l)});
  $('lang').textContent=l==='ar'?'English':'العربية';ls('lang',l);
}
$('lang').onclick=function(){setLang(cur==='ar'?'en':'ar')};
if(ls('lang')==='en')setLang('en');

$('theme').onclick=function(){
  var dark=R.dataset.theme?R.dataset.theme==='dark':matchMedia('(prefers-color-scheme:dark)').matches;
  R.dataset.theme=dark?'light':'dark';ls('theme',R.dataset.theme)};
if(ls('theme'))R.dataset.theme=ls('theme');

$('menu').onclick=function(){var o=$('nav').classList.toggle('open');this.setAttribute('aria-expanded',o)};

var hd=document.querySelector('header.site'),bar=$('bar'),tb=$('top-btn');
function onScroll(){var y=scrollY,h=R.scrollHeight-innerHeight;
  hd.classList.toggle('scrolled',y>10);bar.style.transform='scaleX('+(h>0?y/h:0)+')';tb.classList.toggle('show',y>600)}
addEventListener('scroll',onScroll,{passive:true});onScroll();
tb.onclick=function(){scrollTo({top:0,behavior:'smooth'})};

var io=new IntersectionObserver(function(es){es.forEach(function(e){
  if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
document.querySelectorAll('.reveal').forEach(function(e){io.observe(e)});

var rate=$('rate');
if(rate&&!matchMedia('(prefers-reduced-motion:reduce)').matches){var t0=null;
  (function tick(t){t0=t0||t;var p=Math.min((t-t0)/1200,1);
    rate.textContent=(4.8*(1-Math.pow(1-p,3))).toFixed(1);if(p<1)requestAnimationFrame(tick)})(performance.now());}

var f=$('f');
if(f){var st=$('st');
  var say=function(ar,en){st.textContent=cur==='ar'?ar:en};
  f.oninput=function(e){e.target.classList.remove('bad');st.textContent=''};
  f.onsubmit=function(e){
    e.preventDefault();
    var n=$('n'),p=$('p'),m=$('m'),ok=true;
    [n,m].forEach(function(x){if(x.value.trim().length<2){x.classList.add('bad');ok=false}});
    if(!/^[0-9+\s-]{7,16}$/.test(p.value.trim())){p.classList.add('bad');ok=false}
    if(!ok){say('يرجى تعبئة الاسم ورقم الجوال والرسالة.','Please fill in your name, mobile number and message.');return}
    var kind=f.querySelector('input[name=t]:checked');
    var body={type:kind.value,label:kind.nextElementSibling.textContent,name:n.value.trim(),phone:p.value.trim(),message:m.value.trim()};
    say('جارٍ الإرسال...','Sending...');
    fetch('/api/contact',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)})
      .then(function(r){if(!r.ok)throw 0;return r.json()})
      .then(function(){f.reset();say('وصلتنا رسالتك، وسنتواصل معك قريبًا.','Message received. We will contact you soon.')})
      .catch(function(){ /* no server (opened as plain files): fall back to WhatsApp */
        var t=body.label+'\n'+body.name+' ('+body.phone+'): '+body.message;
        window.open('https://wa.me/966559117177?text='+encodeURIComponent(t),'_blank','noopener');
        say('تم فتح واتساب لإرسال رسالتك.','WhatsApp opened to send your message.')});
  };}
})();
