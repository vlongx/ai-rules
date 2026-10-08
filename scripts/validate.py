from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
folder=root/'rules'/'surge'
files=sorted(x for x in folder.glob('*.list') if x.name!='all.list')
assert files, 'No service files'
pattern=re.compile(r'^(DOMAIN|DOMAIN-SUFFIX),[a-z0-9.-]+$')
all_lines=[]
for file in files:
    rules=[line.strip() for line in file.read_text().splitlines() if line.strip() and not line.startswith('#')]
    assert len(set(rules))==len(rules), f'Duplicates: {file}'
    for rule in rules:
        assert pattern.fullmatch(rule), f'Invalid: {file}: {rule}'
    all_lines.extend(rules)
actual=[x.strip() for x in (folder/'all.list').read_text().splitlines() if x.strip() and not x.startswith('#')]
expected=list(dict.fromkeys(all_lines))
assert set(actual)==set(expected), 'Aggregated rules differ from service rules'
assert len(actual)==len(set(actual)), 'Duplicates in all.list'
print(f'PASS: {len(files)} services, {len(actual)} unique rules; all.list consistent')
