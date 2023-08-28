import markdown


def convert_markdown_2_html(inputfile):
    with open(inputfile, 'r') as f:
        text = f.read()
        html = markdown.markdown(text, extensions=[
                                 'fenced_code', 'toc', 'codehilite', 'meta', 'tables'], output_format="html5")

    temp = inputfile.split('.')
    outputfile = temp[0] + '.html'

    with open(outputfile, 'w') as f:
        f.write(html)


if __name__ == "__main__":
    convert_markdown_2_html('markdown.md')
