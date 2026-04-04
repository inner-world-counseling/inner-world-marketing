from bs4 import BeautifulSoup

html = """<script type="application/ld+json">{"a": "<hello>"}</script>"""
soup = BeautifulSoup(html, 'html.parser')
s = soup.find('script')
s.string = '{"a": "<hello&world>"}'
print(str(soup))
