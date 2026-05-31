from pathlib import Path
p = Path(r'e:\Uni stuff 2 bachelors\Digital fluency\Ass 4\Repo\Digital-Fluency-Assessment-4\index.html')
text = p.read_text('utf-8')
old = "\t\t\t\t\t\t\t\t\t<ul class=\"actions\">\n\t\t\t\t\t\t\t<li><a href=\"full-podcast.html\" class=\"button primary\">Listen to full episode</a></li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t<p class=\"note\">"
new = "\t\t\t\t\t\t\t\t\t<ul class=\"actions\">\n\t\t\t\t\t\t\t\t<li><a href=\"full-podcast.html\" class=\"button primary\">Listen to full episode</a></li>\n\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t<p class=\"note\">"
if old in text:
    p.write_text(text.replace(old, new, 1), 'utf-8')
    print('updated')
else:
    print('not found')
