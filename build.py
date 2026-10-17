import json,os
d=os.path.dirname(os.path.abspath(__file__))+'/app/'
he=open(d+'index.html').read(); en=open(d+'index.en.html').read()
q=lambda s:json.dumps(s,ensure_ascii=False).replace('</','<\\/').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
out='''<!doctype html><html lang="he"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DoughMate</title></head><body style="margin:0;background:#f6efe3"><script>
var H=%s,E=%s,L='he';
try{L=localStorage.getItem('dm-lang')||''}catch(e){}
if(!L)L=/^dm-en/.test(window.name)?'en':(/^dm-he/.test(window.name)?'he':'he');
document.open();document.write(L==='en'?E:H);document.close();
</script></body></html>'''%(q(he),q(en))
os.makedirs(d+'../dist',exist_ok=True)
open(d+'../dist/index.html','w').write(out)
print(len(out))
