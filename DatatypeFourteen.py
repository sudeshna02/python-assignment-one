# Write a Python function to create the HTML string with tags around the
# word(s).

# defining a function to create html tags around
def append_tags(tag, string):
    print(f"<{tag}> {string} </{tag}>")

append_tags("h1", "sudeshna")