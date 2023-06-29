import re

ban_word = 'fuck'

with open('sql_insertions.sql', 'r') as f:
    lines = f.readlines()

print("Finished reading sql_insertions.sql")

seen_lines = set()

with open('updated_sql_insertions.sql', 'w') as f:
    for line in lines:
        word_match = re.search(r"\('(.+?)',", line)
        if word_match and ban_word in word_match.group(1).lower():
            line = re.sub(r"True, True, False\s*\)", "True, False, True )", line)
        if line not in seen_lines:
            f.write(line)
            seen_lines.add(line)

print("Finished writing updated_sql_insertions.sql")
