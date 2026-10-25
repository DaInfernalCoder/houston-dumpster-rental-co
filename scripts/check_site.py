#!/usr/bin/env python3
"""Check generated routes, truth constraints, metadata and sitemap membership."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
BASE='https://houstondumpsterrentalco.shop'
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.tags=[];self.active=False;self.raw='';self.schemas=[]
 def handle_starttag(self,t,a):
  d=dict(a);self.tags.append((t,d))
  if t=='script' and d.get('type')=='application/ld+json':self.active=True;self.raw=''
 def handle_data(self,d):
  if self.active:self.raw+=d
 def handle_endtag(self,t):
  if t=='script' and self.active:self.schemas.append(json.loads(self.raw));self.active=False
pages=list(ROOT.rglob('index.html'));urls=set();titles=set();descs=set();links=set()
for f in pages:
 text=f.read_text();q=Parse();q.feed(text);rel=f.relative_to(ROOT).as_posix();url=BASE+'/'+rel.removesuffix('index.html');urls.add(url)
 assert sum(t=='h1' for t,d in q.tags)==1,(rel,'H1 count')
 title=re.search('<title>(.*?)</title>',text).group(1);assert title not in titles; titles.add(title)
 desc=next(d['content'] for t,d in q.tags if t=='meta' and d.get('name')=='description');assert desc not in descs;descs.add(desc)
 assert [d['href'] for t,d in q.tags if t=='link' and d.get('rel')=='canonical']==[url],(rel,'canonical')
 assert q.schemas,(rel,'schema')
 for schema in q.schemas:
  assert schema['@context']=='https://schema.org';graph=schema['@graph'];ids={n['@id'] for n in graph}
  for ref in re.findall(r'"@id":\s*"([^"]+)"',json.dumps(schema)):assert ref in ids,(rel,'schema reference',ref)
  business=[n for n in graph if isinstance(n.get('@type'),list) and 'LocalBusiness' in n['@type']];assert len(business)==1
  b=business[0];assert b['telephone']=='+13466602743';assert b['address']['streetAddress']=='2812 Center St';assert b['address']['postalCode']=='77007'
  assert not any(k in b for k in ['aggregateRating','review','openingHours','priceRange'])
 for t,d in q.tags:
  for key in ['href','src','poster','data-src']:
   value=d.get(key,'')
   if not value or value.startswith(('http:','https:','tel:','mailto:','data:')):continue
   path=urlsplit(value).path
   if key=='href' and path.startswith('/'):links.add(BASE+path)
   target=ROOT/path.lstrip('/') if path.startswith('/') else f.parent/path
   target=Path(unquote(str(target)))
   if path:assert target.exists(),(rel,'missing reference',value)
   if value.startswith('#') and len(value)>1:assert f'id="{value[1:]}"' in text,(rel,'missing anchor',value)
 assert 'tel:+13466602743' in text and '2812 Center St' in text
 assert not ('cal.com' in text or 'mailto:' in text or '<form' in text)
 print('PASS',rel)
for d in json.loads((ROOT/'content.json').read_text()):
 words=len(re.findall(r'\b[\w’]+\b',html_text:=re.sub('<[^>]+>',' ',d['body'])))
 floor=800 if d['kind']=='service' else 500 if d['kind']=='area' else 0
 assert words>=floor,(d['slug'],'content gate',words,floor)
 print('CONTENT',d['slug'],words)
listed=[x.text for x in ET.parse(ROOT/'sitemap.xml').findall('.//{*}loc')]
assert len(listed)==len(set(listed))==len(urls)==18
assert set(listed)==urls
assert (ROOT/'sitemap.xml').read_bytes()==(ROOT/'sitemaps.xml').read_bytes()
assert '18 canonical pages' in (ROOT/'sitemap.css').read_text()
assert urls-{BASE+'/'}<=links,('orphan pages',urls-links)
assert BASE+'/sitemap.xml' in (ROOT/'robots.txt').read_text()
print('PASS: 18 canonical pages, unique metadata, schema, references, content gates, phone/address, no orphans, matching styled sitemaps')
