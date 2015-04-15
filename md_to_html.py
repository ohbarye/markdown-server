import markdown as md
import codecs
import sys
from env import *

class MarkdownConverter(object):

    def __init__(self):
        css = codecs.open(css_root + css_name,encoding=ms_encoding,mode='r')
        self.html_header = '''
            <html>
            <head>
            <style type='text/css'>
            <!--
            ''' + css.read() + \
            '''
            //-->
            </style>
            </head>
            <body>
            <div class='markdown-body'>
            '''
        self.html_footer = '''
            </div>
            </body>
            </html>
            '''

    def convert(self,file_name):
        code = md.markdown(self.read_md(file_name), extensions=[markdown_type])
        return self.write_html(file_name,code)

    def read_md(self,file_name):
        md_file = codecs.open(markdown_root + file_name,encoding=ms_encoding,mode='r')
        return md_file.read()

    def write_html(self,file_name,body):
        html_path = html_root + file_name + html_extension
        html_file = codecs.open(html_path,encoding=ms_encoding,mode='w')
        html_file.write(self.html_header + body + self.html_footer)
        return html_path

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print('specify *.md file name from command line.')
    else:
        converter = MarkdownConverter()
        converter.convert(args[1])
