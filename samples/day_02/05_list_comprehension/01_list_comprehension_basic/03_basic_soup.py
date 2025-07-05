import re

html = """
<h1>Welcome to My Blog</h1>
<p>This is the first paragraph.</p>
<p>Contact me at info@example.com</p>
"""
lines = html.splitlines()
lines = [re.sub(r'<.*?>', '', line) for line in lines]
lines = [line.strip() for line in lines if line.strip()]

print(lines)




