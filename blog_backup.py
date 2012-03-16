import os
import html2text
import markdown2
os.environ['DJANGO_SETTINGS_MODULE'] = "philwadeorg.settings"
import philwadeorg.philblog.models


h = html2text.HTML2Text()
print h.handle("<h1>Hello world!</h1>")
print markdown2.markdown("*Hello world!*")
