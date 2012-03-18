import os
import json
from html2text import html2text
os.environ['DJANGO_SETTINGS_MODULE'] = "philwadeorg.settings"
from philwadeorg.philblog.models import Post


posts = Post.objects.all()

for post in posts:
    file = open("posts/%s.md" % post.websafe_title, 'wr')
    file.write(html2text(post.body))
    file.close()

    data_file = open("posts/%s.json" % post.websafe_title, 'wr')
    data_file.write(json.JSONEncoder().encode({   "title": post.title,
                                                "id" : post.id,
                                                "date" : str(post.pub_date),
                                                "websafe_title" : post.websafe_title
                                                }))
    data_file.close()


