"""Exports the Apple-style artboard (Apple.dc.html) as a standalone static site for Vercel.

The artboard runs inside the design canvas's component runtime: refs and click handlers are template holes, the
mobile menu is a conditional block, and images are canvas asset URLs. This rewrites those few runtime features into
plain HTML and a small bootstrap script so the page runs on its own, with no runtime and no build step.

Usage: python3 export.py <Apple.dc.html> <blob dir> <output dir>
"""
import os, re, shutil, sys

src, blobs, out = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()

# Readable names for the canvas assets the page uses, keyed by asset id.
ASSETS = {
    'f7284fefb739208928cf2238c5daa463': 'video/promo-loop.mp4',
    '5e48e37d18aea246b5ca1388ab2bff4b': 'img/auto-integration.jpg',
    '3b77e0f9d5cc9c726fe969c4b117df9e': 'img/auto-plc.jpg',
    'df20c7d82b60377a7651e5d63aafb466': 'img/auto-hmi.jpg',
    '3584c3a310a90472ae0fb328651f0a77': 'img/auto-drives.jpg',
    'f9455651754c0afce89b700d93e90434': 'img/auto-panels.jpg',
    '94c6d10c72f08926a9eadef3597e8ae2': 'img/auto-migrations.jpg',
    '2fccb482585e157df99359688205c0ca': 'img/net-design.jpg',
    '52a45a3babad123ab710429eb62915d8': 'img/net-fiber.jpg',
    '3baf5eca3dfdafab6f2e0f2e5f711f88': 'img/net-remote-access.jpg',
    'a92492d46128c0b16f1e1de729822900': 'img/net-remote-support.jpg',
    '94981d834968020f241449c591b129f5': 'img/net-surveillance.jpg',
    '00caa9117b80dbf562b76b208049ded4': 'img/net-site-monitoring.jpg',
    '2b9e980fb02b2e7d9c44056cd94aded1': 'img/logo-gateway-sight-sound.png',
    '612430c919f79b1dacf86b0c3e35380f': 'img/maintenance-technician.jpg',
    'a2c4ca6c1213410369edd07227f37043': 'img/gateway-building.png',
    'cc7071cb43e4c364e18f845d978d47a0': 'img/logo-gateway-apps.png',
}

head = s[s.index('<helmet>') + len('<helmet>'):s.index('</helmet>')].strip()
body = s[s.index('</helmet>') + len('</helmet>'):s.index('</x-dc>')].strip()
m = re.search(r'<script type="text/x-dc"[^>]*>(.*?)</script>', s, re.S)
logic = m.group(1).strip()

# Template holes become plain attributes the bootstrap script can find.
body, n = re.subn(r'ref="\{\{(\w+)Ref\}\}"', r'data-ref="\1"', body)
assert n > 20, n
body = body.replace('onClick="{{openMenu}}"', 'data-action="open-menu"')
body = body.replace('onClick="{{closeMenu}}"', 'data-action="close-menu"')
body = re.sub(r'<sc-if value="\{\{menuOpen\}\}"[^>]*>', '<div data-menu hidden>', body)
body = body.replace('</sc-if>', '</div>')
assert '{{' not in body and '<sc-' not in body, re.findall(r'\{\{[^}]*\}\}|<sc-[^>]*>', body)[:5]

# There is no contact page yet, so contact links go to the footer's contact details.
body = body.replace('href="/contact"', 'href="#contact"')

for k, name in ASSETS.items():
    body = body.replace('/_blob/' + k, 'assets/' + name)
    head = head.replace('/_blob/' + k, 'assets/' + name)
assert '/_blob/' not in body + head

# The canvas check (a window over 1400px tall) would also catch real 4K screens, so the live page never uses it.
logic, n = re.subn(r'this\.canvas = h > 1400;', 'this.canvas = false;', logic)
assert n == 1

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gateway Engineering | Industrial automation experts</title>
<meta name="description" content="Control systems, networks and skilled people that keep Midsouth plants running. Gateway Engineering, Jonesboro, Arkansas.">
<!-- Design preview: keep it out of search results until it replaces the live site. -->
<meta name="robots" content="noindex, nofollow">
{head}
</head>
<body>
{body}
<script>
// Stand-in for the design canvas's component base class: the page's logic only uses props, state and setState.
class DCLogic {{
  constructor() {{ this.props = {{ railSide: 'Left' }}; this.state = {{}}; }}
  setState(patch) {{ Object.assign(this.state, patch); this.renderMenu(); }}
  renderMenu() {{ const m = document.querySelector('[data-menu]'); if (m) m.hidden = !this.state.menu; }}
}}

{logic}

(() => {{
  const page = new Component();
  page.renderVals();
  document.querySelectorAll('[data-ref]').forEach((node) => {{ page.el[node.dataset.ref] = node; }});
  // Menu links close the menu and still follow their anchor, so only the buttons' default is irrelevant here.
  document.addEventListener('click', (e) => {{
    const a = e.target.closest('[data-action]');
    if (a) page.setState({{ menu: a.dataset.action === 'open-menu' }});
  }});
  page.componentDidMount();
}})();
</script>
</body>
</html>
'''

os.makedirs(out, exist_ok=True)
open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page)
for k, name in ASSETS.items():
    found = [f for f in os.listdir(blobs) if f.startswith(k)]
    assert found, k
    dst = os.path.join(out, 'assets', name)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(os.path.join(blobs, found[0]), dst)
print('wrote', os.path.join(out, 'index.html'), len(page))
