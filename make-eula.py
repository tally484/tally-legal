"""Flatten the published terms page into the plain text ASC's custom EULA field takes."""
import re, html, io
from urllib.parse import urljoin

src = io.open('/Users/martyelenjikkal/tally-legal/terms.html', encoding='utf-8').read()
body = src.split('<body>', 1)[1].split('</body>')[0]

out = []
for m in re.finditer(r'<(h1|h2|h3|p|li)([^>]*)>(.*?)</\1>', body, re.S):
    tag, inner = m.group(1), m.group(3)
    # Keep actual legal links when flattening HTML for App Store Connect.
    inner = re.sub(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>',
                   lambda a: a.group(2) if a.group(1).startswith('mailto:')
                   else a.group(2) + ' (' + urljoin('https://tally484.github.io/tally-legal/', a.group(1)) + ')',
                   inner, flags=re.S)
    t = re.sub(r'<[^>]+>', '', inner)
    t = html.unescape(t).replace(' ', ' ')
    t = re.sub(r'\s+', ' ', t).strip()
    if not t:
        continue
    if tag == 'h1':
        out += [t.upper(), '']
    elif tag == 'h2':
        out += ['', t.upper(), '']
    elif tag == 'h3':
        # A subsection: titled, but not shouted like a top-level heading.
        out += ['', t, '']
    elif tag == 'li':
        out.append('- ' + t)
    else:
        # A paragraph straight after a list needs the blank line the list didn't add.
        if out and out[-1].startswith('- '):
            out.append('')
        out += [t, '']

txt = re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip() + '\n'
io.open('eula.txt', 'w', encoding='utf-8').write(txt)
print('chars: %d  lines: %d' % (len(txt), txt.count('\n')))
print('non-ascii:', sorted({c for c in txt if ord(c) > 127}))
