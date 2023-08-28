# python_markdown

This are my settings/extensions for the markdown command to generate a proper html file:

``` py 
html = markdown.markdown(text, extensions=['fenced_code', 'toc',
			'codehilite', 'meta', 'tables'], output_format="html5")
```


# Example:

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.5.0/themes/prism.min.css"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.17.1/prism.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.17.1/components/prism-python.min.js"></script>

## Table Of Contents (does not work in Github)
[TOC]

# Markdown Test
This is a markown test, to check if the python markdown html conversiont works correctly

## Listing Test
``` python 
def convert_markdown_2_html(inputfile):
    with open(inputfile, 'r') as f:
        text = f.read()
        html = markdown.markdown(text, extensions=[FencedCodeExtension()])

    temp = inputfile.strip('.')
    outputfile = temp[0] + '.html'

    with open(outputfile, 'w') as f:
        f.write(html)
```

## Image Test
### Link in Markdown
![test_image](https://static.vecteezy.com/system/resources/previews/019/767/928/non_2x/batman-logo-batman-logo-transparent-free-png.png)
### Link in HTML
<img src ="https://static.vecteezy.com/system/resources/previews/019/767/928/non_2x/batman-logo-batman-logo-transparent-free-png.png" alt = "test_image" width="300px">

## Table Test
### Markdown
| Cell1  | Cell2  |
|---|---|


### HTML
<table>
    <tr>
        <td>
            Cell1
        </td>
        <td>
            Cell2
        </td>
    </tr>
</table>

## Lists
Ordered List

1. one
2. two
1. test
3. three

unordered List

- asdf
- aff
- ad
- e
- adsdf
