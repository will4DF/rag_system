content = open('02_clean_bylines.py').read()

old_fallback = '''BYLINE_FALLBACK_RE = re.compile(
    rf\"Written by\\\\s*.{0,150}?\\\\n+\"
    rf\"(?:(?:{MONTHS})\\\\s+\\\\d{1,2},\\\\s+\\\\d{4}|Updated\\\\s+.{0,40}?ago)\"
    rf\"\\\\s*\\\\n+\",
    re.DOTALL,
)'''

new_fallback = '''BYLINE_FALLBACK_RE = re.compile(
    rf\"Written by\\\\s*.{0,150}?\\\\n+\"
    rf\"(?:(?:{MONTHS})\\\\s+\\\\d{1,2},\\\\s+\\\\d{4}|Updated\\\\s+.{0,40}?)\"
    rf\"\\\\s*\\\\n+\",
    re.DOTALL,
)'''

if old_fallback in content:
    content = content.replace(old_fallback, new_fallback)
    open('02_clean_bylines.py', 'w').write(content)
    print('PATCHED')
else:
    print('PATTERN NOT FOUND -- run: grep -n \"BYLINE_FALLBACK_RE\" -A5 02_clean_bylines.py  and paste me the output')
