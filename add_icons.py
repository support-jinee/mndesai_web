import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
def repl(m):
    global count
    count += 1
    if 'data-icon-id' in m.group(0): return m.group(0)
    return m.group(1) + f' data-icon-id="static-icon-{count}"' + m.group(2)

new_content = re.sub(r'(<i\s+class="[^"]*fa-[^"]*")([^>]*>)', repl, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Done")
