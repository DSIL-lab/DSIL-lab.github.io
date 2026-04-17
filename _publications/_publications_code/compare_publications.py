import re
from pathlib import Path

# Load provided text
with open(r'C:\LabHomepage_Edit\DSIL-lab.github.io\provided_publications.txt', 'r', encoding='utf-8') as f:
    provided_text = f.read()

# Parse provided text into a dict
provided = {
    'Journal Articles': {},
    'International Conference Proceedings': {},
    'Invited Talks': {}
}
current_section = 'Journal Articles'  # Start with Journal Articles
current_item = None

lines = provided_text.splitlines()
i = 0
while i < len(lines):
    line = lines[i].strip()
    if not line:
        i += 1
        continue
    if line == 'International Conference Proceedings':
        current_section = 'International Conference Proceedings'
        i += 1
        continue
    if line == 'Invited Talks':
        current_section = 'Invited Talks'
        i += 1
        continue
    match = re.match(r'^\[(\d+)\]\s*(.+)$', line)
    if match:
        num = int(match.group(1))
        title = match.group(2)
        current_item = {'title': title}
        provided[current_section][num] = current_item
        i += 1
        # Next line is authors
        if i < len(lines):
            authors_line = lines[i].strip()
            current_item['authors'] = authors_line
            i += 1
        # Next line is status or venue
        if i < len(lines):
            status_venue = lines[i].strip()
            if status_venue.startswith('Under Review') or status_venue.startswith('Accepted') or status_venue.startswith('Early access') or status_venue.endswith('2026') or status_venue.endswith('2025') or status_venue.endswith('2024') or status_venue.endswith('2023') or status_venue.endswith('2022') or status_venue.endswith('2021') or status_venue.endswith('2020') or status_venue.endswith('2019') or status_venue.endswith('2018') or status_venue.endswith('2017') or status_venue.endswith('2016'):
                current_item['status_venue'] = status_venue
                i += 1
            else:
                current_item['status'] = status_venue
                i += 1
                if i < len(lines):
                    venue_line = lines[i].strip()
                    if venue_line:
                        current_item['venue'] = venue_line
                        i += 1
    else:
        i += 1

# Now, read files and compare
root = Path(r'C:\LabHomepage_Edit\DSIL-lab.github.io\_publications')

def clean_authors(authors_str):
    # Remove HTML tags and quotes
    authors_str = re.sub(r'<[^>]+>', '', authors_str)
    authors_str = re.sub(r'^"|"$', '', authors_str)  # Remove surrounding quotes
    authors_str = re.sub(r'\s+', ' ', authors_str).strip()
    return authors_str

def parse_front_matter(content):
    front_matter = content.split('---')[1]
    data = {}
    for line in front_matter.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
    return data

def compare_item(file_path, provided_item):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    data = parse_front_matter(content)
    
    issues = []
    
    # Title
    file_title = data.get('title', '').strip('"')
    provided_title = provided_item['title']
    if file_title != provided_title:
        issues.append(f"Title mismatch: file='{file_title}' provided='{provided_title}'")
    
    # Authors
    file_authors_clean = clean_authors(data.get('authors', ''))
    provided_authors = provided_item['authors']
    if file_authors_clean != provided_authors:
        issues.append(f"Authors mismatch: file='{file_authors_clean}' provided='{provided_authors}'")
    
    # Status
    file_status = data.get('status', '')
    provided_status = provided_item.get('status', '')
    if 'status_venue' in provided_item:
        # Parse status_venue
        sv = provided_item['status_venue']
        if ' (Accepted)' in sv:
            provided_status = 'accepted'
            provided_venue = sv.replace(' (Accepted)', '')
        elif ' (Early access)' in sv:
            provided_status = 'accepted'  # or something
            provided_venue = sv.replace(' (Early access)', '')
        else:
            provided_status = 'published'
            provided_venue = sv
    else:
        provided_status = provided_item.get('status', '')
        provided_venue = provided_item.get('venue', '')
    
    if file_status != provided_status:
        issues.append(f"Status mismatch: file='{file_status}' provided='{provided_status}'")
    
    # Venue
    file_venue_clean = re.sub(r'<[^>]+>', '', data.get('venue', ''))
    file_venue_clean = re.sub(r'^"|"$', '', file_venue_clean).strip()
    if file_venue_clean != provided_venue:
        issues.append(f"Venue mismatch: file='{file_venue_clean}' provided='{provided_venue}'")
    
    return issues

# Map file types to sections
file_to_section = {
    'jour': 'Journal Articles',
    'conf': 'International Conference Proceedings',
    'inv': 'Invited Talks'
}

modified = []
for path in sorted(root.glob('*.md')):
    match = re.match(r'(\w+)-(\d+)\.md', path.name)
    if match:
        type_prefix = match.group(1)
        num = int(match.group(2))
        section = file_to_section.get(type_prefix)
        if section and num in provided[section]:
            issues = compare_item(path, provided[section][num])
            if issues:
                print(f"{path.name}:")
                for issue in issues:
                    print(f"  {issue}")
                modified.append(path.name)

print('Files with issues:', modified)