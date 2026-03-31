filepath = r"C:\Sistemas\IA\SIL3000_IA_WIN\ .agent\rules\GEMINI.md".replace(" ", "")

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

custom_protocol = """### 🇧🇷 Brazil Custom Protocol (MANDATORY)

1. **Language**: ALWAYS respond in Portuguese.
2. **Conciseness**: Show the minimum details possible, only if critical for the user.
3. **Completion**: ALWAYS end the final response with: `===> TERMINEI <===` (Bold, uppercase).
4. **Shortcut E-P**: If the user types ONLY "E-P" (case-insensitive), immediately terminate any running instance of the project and restart it using `python SIL_IA_WIN.py`.
5. **Autonomy**: Resolve tasks solo without asking for confirmation, unless the Socratic Gate strictly requires it for ambiguity.
6. **Layout Protection**: NEVER change any layout or Approved Designs without explicit user permission. Preserve the existing visual structure.
7. **Scope Control**: Fix ONLY the specific problem requested. No "proactive" unrelated improvements.

"""

if '### 🌐 Language Handling' in text:
    text = text.replace('### 🌐 Language Handling', custom_protocol + '### 🌐 Language Handling')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Success: Updated GEMINI.md rules")
