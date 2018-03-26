#https://www.crummy.com/software/BeautifulSoup/

from bs4 import BeautifulSoup

html = """
<td class='title'>
    <div class='tit3' id='hong'>
        <a href='www.abcd.com' title='abcd'>미녀와 야수</a>
    </div>
</td>
"""
soup = BeautifulSoup(html, 'html.parser')
print(type(soup), soup)

print('='*50)
tag = soup.td
print(type(tag), tag)
print(tag['class'])
print('='*50)

tag.find('div', attrs={'class':'tit3'})
print(tag)
tag = soup.div
print(tag)
 
print('='*50)
tag = soup.a
print(tag)
