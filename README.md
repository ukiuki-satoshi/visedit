# Abstract
VisEdit is a visualiation library for string edit and difference between two strings.

# Main Features

* visualization edits between two strings
* generate formatted text and html


# Installation

install using pip:

```
$ pip install visedit
```

# Example Codes

## Generate formatted text or html

```
from visedit import StringEdit
source_str = "kitten"
target_str = "sitting"
se = StringEdit(source_str, target_str)
text = se.generate_text()
print(text)
# also available html as well as text
html = se.generate_html()
```

## Change color setting

```
# setting for text
e = StringEdit(source_str, target_str, text_color_settings={
"wrong": "YELLOW",
"correct": "GREEN",
"base": "WHITE",
})
# setting for html
e = StringEdit(source_str, target_str, html_color_settings={
"wrong": "YELLOW",
"correct": "GREEN",
"base": "WHITE",
})
```

available colors is:

* BLACK
* RED
* GREEN
* YELLOW
* BLUE
* PURPLE
* CYAN
* WHITE
