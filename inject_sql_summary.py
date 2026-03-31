import re

with open('diff_backup.txt', 'r', encoding='utf-8') as f:
    diff_text = f.read()

# We look for blocks like:
# @@ -XXX,YYY +XXX,YYY @@ class ClassName(...):
# ...
# +    def get_sql_summary(self):
# +        ...
# +        return (...)
# +
# The regex can match '@@.*?class (\w+)\(.*?@@' OR just assume the class name appears in the diff chunk header.
chunks = diff_text.split('@@')

summaries = {}
current_class = None

for chunk in chunks:
    # First line of chunk might have 'class X('
    lines = chunk.split('\n')
    header = lines[0]
    
    match = re.search(r'class (\w+)\(', header)
    if match:
        current_class = match.group(1)
        
    # extract the added summary
    in_summary = False
    summ_lines = []
    
    for l in lines[1:]:
        if l.startswith('+    def get_sql_summary(self):'):
            in_summary = True
            summ_lines.append("    def get_sql_summary(self):")
            continue
            
        if in_summary:
            if l.startswith('+'):
                # remove the leading +
                line_text = l[1:]
                summ_lines.append(line_text)
                if line_text.strip() == ')':
                    # End of typical get_sql_summary structure (return (...))
                    pass
            elif l.startswith(' '):
                # End of block if it's context spaces, assuming our entire def was added at once without context spaces inside
                in_summary = False
                if current_class and summ_lines:
                    summaries[current_class] = '\n'.join(summ_lines)
            elif l.startswith('-'):
                # ignore removed lines
                pass

for k, v in summaries.items():
    print(k, "->", len(v))

# Inject into SIL_IA_WIN.py
with open('SIL_IA_WIN.py', 'r', encoding='utf-8') as f:
    code = f.read()

for cls, summ in summaries.items():
    if cls in code:
        # Check if already present to avoid duplication (might happen if diff restores an already existing method)
        if hasattr(cls, 'get_sql_summary') or 'def get_sql_summary' in code.split(f'class {cls}')[1].split('class ')[0] if len(code.split(f'class {cls}'))>1 else '':
            pass
        
        # Inject right before 'def carregar_dados' or something similar in that class
        # A safer way to inject is to find the init or something and put it right after. 
        # But 'def carregar_dados' or 'def carregar_anos' or 'def on_click' all work.
        # We will just inject it BEFORE the last method of the class. Wait. It's safer to inject it BEFORE `def carregar_dados(self):`
        pattern = rf'(class {cls}\(.*?)(    def carregar_[a-z]+)'
        if re.search(pattern, code, flags=re.DOTALL):
            code = re.sub(pattern, rf'\1{summ}\n\n\2', code, flags=re.DOTALL, count=1)
        else:
            print("Could not find insertion point for", cls)

with open('SIL_IA_WIN.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Injections complete.")
