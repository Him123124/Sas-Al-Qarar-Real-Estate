import html
def h(tag, ar, en, cls='', extra=''):
    c = f' class="{cls}"' if cls else ''
    return f'<{tag}{c} {extra} data-ar="{html.escape(ar)}" data-en="{html.escape(en)}">{ar}</{tag}>'
NAV=[('index','الرئيسية','Home'),('services','خدماتنا','Services'),('contact','تواصل معنا','Contact')]
def page(slug, tar, ten, body):
    nav=''.join(f'<a href="{s}.html"{" class=active" if s==slug else ""} data-ar="{a}" data-en="{e}">{a}</a>' for s,a,e in NAV)
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{tar} | ساس القرار العقارية</title>
<meta name="description" content="مكتب ساس القرار العقاري في الهفوف، الأحساء: بيع وشراء وإيجار وإدارة أملاك.">
<link rel="icon" href="images/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;700&display=swap">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<div id="bar"></div>
<header class="site"><div class="wrap bar">
  <a class="brand" href="index.html"><img src="images/logo.svg" alt="" width="40" height="40">{h("span","ساس القرار العقارية","Sas Al-Qarar Real Estate")}</a>
  <button id="menu" aria-label="Menu" aria-expanded="false">☰</button>
  <nav id="nav">{nav}<button id="theme" aria-label="Theme">◐</button><button id="lang" aria-label="Language">English</button></nav>
</div></header>
<main>
{body}
</main>
<footer class="site"><div class="wrap foot">
  {h("span","© ساس القرار العقارية، المزروعية، العمرية، الهفوف 36441","© Sas Al-Qarar Real Estate, Al Muzruiyyah, Al Omairiyah, Al Hofuf 36441")}
  <a dir="ltr" href="tel:+966559117177">055 911 7177</a>
</div></footer>
<button id="top-btn" aria-label="Back to top">↑</button>
<script src="js/main.js"></script>
</body>
</html>
'''
def card(t_ar,t_en,p_ar,p_en): return f'<div class="card">{h("h3",t_ar,t_en)}{h("p",p_ar,p_en)}</div>'
S=[("البيع والشراء","Buying & selling","عرض العقارات، والتفاوض على السعر، ومتابعة الإجراءات حتى نقل الملكية.","Listings, price negotiation, and follow-through until ownership is transferred."),
   ("الإيجار","Rentals","عقارات للإيجار في الأحساء مع خيارات دفع مرنة.","Properties for rent across Al-Ahsa with flexible payment options."),
   ("إدارة الأملاك","Property management","إدارة منظمة للعقار والمستأجرين، وسرعة في الاستجابة.","Organised management of your property and tenants, with quick responses.")]
home=f'''<section class="hero"><div class="wrap hero-grid">
  <div class="hero-text">
    {h("h1","قرارك العقاري، بثقة.","Property decisions, made with confidence.")}
    {h("p","مكتب عقاري في الهفوف، الأحساء. بيع وإيجار وإدارة أملاك، مع تعامل واضح من أول تواصل حتى إفراغ الصك.","A real estate office in Al Hofuf, Al-Ahsa. Sales, rentals and property management, with clear dealing from first call to ownership transfer.")}
    <div class="btns"><a class="btn" href="tel:+966559117177" dir="ltr">055 911 7177</a><a class="btn ghost" href="https://wa.me/966559117177" rel="noopener">{h("span","واتساب","WhatsApp")}</a></div>
  </div>
  <div class="hero-art"><img src="images/hero.svg" alt="">
    <div class="badge"><b dir="ltr" id="rate" data-v="4.8">4.8</b>{h("span","من 99 تقييمًا على خرائط جوجل","from 99 Google Maps reviews")}</div></div>
</div></section>
<section class="sec reveal"><div class="wrap">{h("h2","خدماتنا","Our services")}
  <div class="cards">{"".join(card(*x) for x in S)}</div>
  <p class="more"><a href="services.html" data-ar="تفاصيل الخدمات" data-en="See service details">تفاصيل الخدمات</a></p></div></section>
<section class="sec alt reveal"><div class="wrap">{h("h2","ماذا يقول عملاؤنا","What clients say")}
  <blockquote>{h("p","«خدمتهم ممتازة في إدارة العقار وخيارات الدفع المرنة. خدمتهم أسرع وأكثر تنظيمًا من غيرهم، وأنصح بالإيجار من عقاراتهم.»","“Excellent service managing the property and flexible payment options. Faster and more organised than others. I highly recommend renting from them.”")}
  {h("cite","جهاد الأحمر، مراجعة على خرائط جوجل","Jehad Alahmar, Google Maps review")}</blockquote></div></section>
<section class="cta reveal"><div class="wrap">{h("h2","هل تبحث عن عقار؟","Looking for a property?")}
  <a class="btn light" href="contact.html">{h("span","تواصل معنا","Contact us")}</a></div></section>'''
steps=[("أخبرنا بطلبك","Tell us what you need","بيع أو شراء أو إيجار، ونوع العقار والميزانية.","Sale, purchase or rent, property type and budget."),
 ("شاهد الخيارات","See the options","نعرض عليك العقارات المناسبة ونرتب المعاينة.","We show suitable properties and arrange viewings."),
 ("اتفق على السعر والشروط","Agree price and terms","تفاوض واضح على السعر وشروط الدفع.","Clear negotiation on price and payment terms."),
 ("أتمم الإجراءات","Complete the paperwork","متابعة الإجراءات حتى نقل الملكية أو توقيع العقد.","Follow-through to ownership transfer or lease signing.")]
sv=''.join(f'<article class="svc reveal">{h("h2",a,b)}{h("p",c,d)}</article>' for a,b,c,d in S)
st=''.join(f'<li>{h("strong",a,b)}{h("span",c,d)}</li>' for a,b,c,d in steps)
services=f'''<section class="sec"><div class="wrap">{h("h1","خدماتنا","Our services",extra='')}<div class="svcs">{sv}</div></div></section>
<section class="sec alt reveal"><div class="wrap">{h("h2","كيف نعمل","How it works")}<ol class="steps">{st}</ol></div></section>'''
contact=f'''<section class="sec"><div class="wrap two">
  <div>{h("h1","تواصل معنا","Contact us")}
   <dl>{h("dt","العنوان","Address")}{h("dd","المزروعية، العمرية، الهفوف 36441","Al Muzruiyyah, Al Omairiyah, Al Hofuf 36441")}
   {h("dt","الهاتف","Phone")}<dd dir="ltr"><a href="tel:+966559117177">055 911 7177</a></dd></dl>
   <p><a href="https://www.google.com/maps/search/?api=1&query=9H6H%2BVQ+Al+Hofuf" rel="noopener" data-ar="افتح الموقع في خرائط جوجل" data-en="Open in Google Maps">افتح الموقع في خرائط جوجل</a></p></div>
  <form id="f" novalidate>
   <fieldset class="chips"><label><input type="radio" name="t" value="buy" checked><span data-ar="شراء" data-en="Buy">شراء</span></label>
   <label><input type="radio" name="t" value="sell"><span data-ar="بيع" data-en="Sell">بيع</span></label>
   <label><input type="radio" name="t" value="rent"><span data-ar="إيجار" data-en="Rent">إيجار</span></label>
   <label><input type="radio" name="t" value="manage"><span data-ar="إدارة أملاك" data-en="Management">إدارة أملاك</span></label></fieldset>
   <input id="n" name="name" autocomplete="name" placeholder="الاسم" data-ph-ar="الاسم" data-ph-en="Your name">
   <input id="p" name="phone" type="tel" dir="auto" autocomplete="tel" placeholder="رقم الجوال" data-ph-ar="رقم الجوال" data-ph-en="Mobile number">
   <textarea id="m" name="message" rows="4" placeholder="ماذا تبحث عنه؟" data-ph-ar="ماذا تبحث عنه؟" data-ph-en="What are you looking for?"></textarea>
   <button class="btn" type="submit" data-ar="أرسل" data-en="Send">أرسل</button><p id="st" role="status"></p></form>
</div></section>'''
for slug,ta,te,b in [('index','الرئيسية','Home',home),('services','خدماتنا','Services',services),('contact','تواصل معنا','Contact',contact)]:
    open(f'{slug}.html','w',encoding='utf-8').write(page(slug,ta,te,b))
