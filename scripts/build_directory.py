"""Generate the public directory from data/projects.json. Run --check in CI."""
from pathlib import Path
import argparse, html, json, re
ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'data/projects.json').read_text())
def esc(value): return html.escape(str(value), quote=True)
def markets(project):
    values = set(project.get('markets', []))
    groups = []
    for label, keys in [('Equities', {'stocks', 'us-equities'}), ('Options', {'options'}), ('Crypto & DeFi', {'crypto', 'defi', 'cex', 'perpetuals', 'hyperliquid'}), ('Prediction markets', {'prediction-markets', 'kalshi', 'polymarket'}), ('Futures & FX', {'futures', 'forex', 'commodities'}), ('Other', {'macro', 'agent-commerce', 'tradfi'})]:
        if values & keys: groups.append(label)
    return groups

def card(p):
    tags = p.get('tags', [])
    interfaces = [label for key, label in [('mcp','MCP'), ('cli','CLI'), ('sdk','SDK'), ('skills','Skills'), ('api','API')] if key in tags]
    modes = p.get('modes', [])
    mode_labels = {'research':'Research', 'backtest':'Backtest', 'paper':'Paper', 'dry-run':'Dry-run', 'live':'Live'}
    origin = {'official':'Official', 'community':'Community'}.get(p.get('origin'))
    badges = interfaces + [mode_labels[m] for m in modes]
    if origin: badges.append(origin)
    if 'experimental' in tags: badges.append('Experimental')
    if 'source-available' in tags: badges.append('Source-available')
    attrs = {'category':p['category'], 'markets':json.dumps(markets(p)), 'modes':json.dumps(modes), 'search':' '.join([p['name'],p['description'],p['category'],*p.get('markets',[]),*tags,p.get('language') or ''])}
    attr = ' '.join(f'data-{key}="{esc(value)}"' for key,value in attrs.items())
    badge_html = ''.join(f'<span class="tag{ " tag--accent" if value == "Official" else ""}">{esc(value)}</span>' for value in badges)
    if not modes: badge_html += '<span class="tag tag--muted">Mode not listed</span>'
    details = ''
    if p.get('notes'):
        license_html = f'<a href="{esc(p["license_source"])}">{esc(p["license"])} license source</a>' if p.get('license_source') else 'Hosted service'
        details = f'<details class="project-details"><summary>Access &amp; license</summary><p>{esc(p["notes"])}</p><p>{license_html} · Reviewed {esc(p["last_verified"])}</p></details>'
    return f'''<article class="project" {attr}>
  <p class="project-category">{esc(p['category'])}</p>
  <h3><a href="{esc(p['url'])}">{esc(p['name'])}<span aria-hidden="true"> ↗</span></a></h3>
  <p class="project-description">{esc(p['description'])}</p>
  <div class="tags" aria-label="Project attributes">{badge_html}</div>
{details}
</article>'''

def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--check', action='store_true'); args = parser.parse_args()
    path = ROOT / 'docs/index.html'; text = path.read_text()
    categories = ['Trading Agents','Broker & Exchange Integrations','MCP Servers & Agent Skills','Prediction Markets','Research & Backtesting','Data, Wallets & Risk Infrastructure']
    assert len({p['url'] for p in DATA}) == len(DATA), 'Duplicate project URLs'
    assert all(p['category'] in categories for p in DATA), 'Unknown category'
    buttons = '<button type="button" class="category active" data-category="" aria-pressed="true">All tools <span>'+str(len(DATA))+'</span></button>\n'
    for category in categories:
        count = sum(p['category'] == category for p in DATA)
        buttons += f'<button type="button" class="category" data-category="{esc(category)}" aria-pressed="false">{esc(category)} <span>{count}</span></button>\n'
    ordered = sorted(DATA, key=lambda p: p['name'].casefold())
    options = '<option value="">All categories</option>' + ''.join(f'<option value="{esc(c)}">{esc(c)}</option>' for c in categories)
    blocks = {'CATEGORY-OPTIONS':options, 'CATEGORIES':buttons.strip(), 'PROJECTS':'\n'.join(map(card, ordered)), 'COUNT':f'{len(DATA)} tools'}
    for marker, content in blocks.items():
        pattern = f'(<!-- {marker}:START -->).*?(<!-- {marker}:END -->)'
        text, n = re.subn(pattern, lambda m:m[1]+'\n'+content+'\n'+m[2],text,flags=re.S)
        assert n == 1, marker
    outputs = {path:text, ROOT/'docs/projects.json':json.dumps(DATA, indent=2, ensure_ascii=False)+'\n'}
    for path, content in outputs.items():
        if args.check:
            assert path.exists() and path.read_text() == content, f'{path.name} is stale; run python3 scripts/build_directory.py'
        else: path.write_text(content)
    print(f'{"Verified" if args.check else "Generated"} {len(DATA)} directory entries.')
if __name__ == '__main__': main()
