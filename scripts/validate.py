from pathlib import Path
import ipaddress
import re

root = Path(__file__).resolve().parents[1]
folder = root / 'rules' / 'surge'
files = sorted(x for x in folder.glob('*.list') if x.name != 'all.list')
files += sorted((folder / 'extensions').glob('*.list'))
assert files, 'No service rules or extensions found'

domain = re.compile(r'^(DOMAIN|DOMAIN-SUFFIX|DOMAIN-KEYWORD),[a-z0-9.-]+$')
logical = re.compile(r'^AND,[(][(](DOMAIN|DOMAIN-SUFFIX|DOMAIN-KEYWORD),[a-z0-9.-]+[)],[(](DOMAIN|DOMAIN-SUFFIX|DOMAIN-KEYWORD),[a-z0-9.-]+[)][)]$')

def valid_rule(rule):
    if domain.fullmatch(rule) or logical.fullmatch(rule):
        return True
    fields = rule.split(',')
    if len(fields) == 3 and fields[0] in ('IP-CIDR', 'IP-CIDR6') and fields[2] == 'no-resolve':
        try:
            network = ipaddress.ip_network(fields[1], strict=False)
            return network.version == (4 if fields[0] == 'IP-CIDR' else 6)
        except ValueError:
            return False
    return False

all_lines = []
for file in files:
    rules = [line.strip() for line in file.read_text(encoding='utf-8').splitlines()
             if line.strip() and not line.lstrip().startswith('#')]
    assert len(set(rules)) == len(rules), f'Duplicates: {file}'
    for rule in rules:
        assert valid_rule(rule), f'Invalid Surge rule: {file}: {rule}'
    all_lines.extend(rules)

actual = [line.strip() for line in (folder / 'all.list').read_text(encoding='utf-8').splitlines()
          if line.strip() and not line.lstrip().startswith('#')]
expected = list(dict.fromkeys(all_lines))
assert len(actual) == len(set(actual)), 'Duplicates in all.list'
assert set(actual) == set(expected), 'Aggregated rules differ from service and extension rules'
for rule in actual:
    assert valid_rule(rule), f'Invalid aggregate rule: {rule}'
print(f'PASS: {len(files)} files, {len(actual)} unique rules; all.list consistent')
