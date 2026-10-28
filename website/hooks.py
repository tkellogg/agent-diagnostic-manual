"""Add site presentation to the portable Markdown after MkDocs renders it."""
import re
from lxml import etree as ET
from lxml import html


def on_page_content(content, page, **kwargs):
    root=html.fragment_fromstring(content,create_parent='div')
    # Keep the homepage's descriptive rows; compact references within entries.
    if page.meta.get('id'):
        for link in root.xpath('.//a[@href]'):
            match=re.fullmatch(r'([SDI][0-9]{3,}) — (.+)',link.text_content())
            if not match or re.match(r'[a-z]+:',link.get('href'),re.I):continue
            entry_id,title=match.groups()
            link.text=None
            for child in list(link):link.remove(child)
            link.set('class','adm-entry-ref')
            ET.SubElement(link,'span',{'class':'adm-ref-id'}).text=entry_id
            ET.SubElement(link,'span',{'class':'visually-hidden'}).text=' — '
            ET.SubElement(link,'span',{'class':'adm-ref-title'}).text=title
        for listing in root.xpath('.//ul'):
            if all(len(li)==1 and li[0].tag=='a' and li[0].get('class')=='adm-entry-ref'
                   and not (li.text or '').strip() and not (li[0].tail or '').strip()
                   for li in listing):
                listing.set('class','adm-entry-refs')
    # Example provenance belongs beside its heading, without another paragraph.
    for badge in root.xpath('.//span[@class="adm-example-kind"]'):
        paragraph=badge.getparent()
        heading=paragraph.getprevious()
        if paragraph.tag=='p' and heading is not None and heading.tag in ('h3','h4'):
            heading.append(badge)
            if not paragraph.text_content().strip():paragraph.getparent().remove(paragraph)

    headings=root.xpath('.//h3[@data-adm-harness]')
    if headings:
        controls=ET.Element('div',{'class':'adm-harness-controls','hidden':'','data-pagefind-ignore':''})
        ET.SubElement(controls,'label',{'for':'adm-harness-select'}).text='Harness'
        select=ET.SubElement(controls,'select',{'id':'adm-harness-select','aria-describedby':'adm-harness-status'})
        ET.SubElement(select,'option',{'value':'all'}).text='All harnesses'
        status=ET.SubElement(controls,'p',{'id':'adm-harness-status','role':'status'})
        status.text='Shared instructions above apply to every harness. Your choice is remembered in this browser.'
        for heading in headings:
            key=heading.attrib.pop('data-adm-harness')
            title=(heading.text or '').strip()
            ET.SubElement(select,'option',{'value':key}).text=title
            wrapper=ET.Element('section',{'class':'adm-harness-note','data-harness':key,'aria-labelledby':heading.get('id')})
            start=heading
            previous=heading.getprevious()
            if previous is not None and previous.xpath('./a[@id="harness-notes/'+key+'"]'):
                start=previous
            parent=start.getparent()
            parent.insert(parent.index(start),wrapper)
            node=start
            while node is not None:
                if node is not start and (node.tag=='h2' or node.get('data-adm-harness') or
                    node.xpath('./a[starts-with(@id,"harness-notes/") or @id="evaluation"]')):break
                following=node.getnext()
                wrapper.append(node)
                node=following
        first=root.xpath('.//section[@data-harness]')[0]
        first.addprevious(controls)
    return (root.text or '')+''.join(html.tostring(child,encoding='unicode') for child in root)
