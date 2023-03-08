import os
import mimetypes
import datetime

URL = "https://sunspiral.city"
ICON = "porygon.gif"
PAGE_TITLE = "⭕ sunspiral city"

def get_image_names_and_timestamps_as_list():
  new_image_list = []
  for filename in os.listdir('img'):
    new_image_list.append([filename, os.path.getmtime('img/' + filename)])
  return new_image_list

def generate_html_header():
  return f'''<!DOCTYPE html>
  <html lang="en">
    <head>
      <title>{PAGE_TITLE}</title>
      <meta http-equiv="content-type" content="text/html; charset=UTF-8">
      <meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
      <meta name='robots' content='noindex,follow'>
      <link rel="icon" type="image/gif" href="{ICON}">
      <link rel="alternate" type="application/rss+xml" href="rss" title="{PAGE_TITLE}">
    </head>
    <body>
      <ul>\n'''

def generate_html_list_part(filename):
  return f'        <li><a href = "./img/{filename}">{filename}</a></li>\n'

def generate_html_footer():
  return '''      </ul>

      <p>This is a work of fiction.
      <br>
      Names, characters, places and incidents either are products of the author’s imagination or are used fictitiously.
      <br>
      Any resemblance to actual events or locales or persons, living or dead, is entirely coincidental.</p>
      <a href = "rss">rss</a>
    </body>
  </html>
  '''

def generate_html():
  with open('index.html', 'w', encoding="utf-8") as f:
    f.write(generate_html_header())

    for filename in sorted(os.listdir('img')):
      f.write(generate_html_list_part(filename))
     
    f.write(generate_html_footer())

def generate_rss_header():
  return f'''<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
  <channel>
    <title>{PAGE_TITLE}</title>
    <link>{URL}</link>
    <language>en-gb</language>
    <skipHours>
      <hour>1</hour>
      <hour>2</hour>
      <hour>3</hour>
      <hour>4</hour>
      <hour>5</hour>
      <hour>6</hour>
      <hour>7</hour>
      <hour>8</hour>
      <hour>9</hour>
      <hour>10</hour>
    </skipHours>
    <image>
      <url>{ICON}</url>
      <title>{PAGE_TITLE}</title>
      <link>{URL}</link>
    </image>
    <description>{PAGE_TITLE}</description>
    '''

def generate_rss_part(item):
  return f'''\n    <item>
      <title>{item[0]}</title>
      <link>{URL}/img/{item[0]}</link>
      <url>{URL}/img/{item[0]}</url>
      <description>
        <![CDATA[
                <img src="{URL}/img/{item[0]}" alt="" />
            ]]>
      </description>
      <guid>{item[0]} {item[1]}</guid>
    </item>'''

def generate_rss_footer():
  return """</channel>
</rss> """

def generate_rss(image_list):
  items_in_order = get_twenty_newest_images_as_list(image_list)
  with open('rss', 'w', encoding="utf-8") as f:
    f.write(generate_rss_header())

    for item in items_in_order:
      f.write(generate_rss_part(item))

    f.write(generate_rss_footer())

def update_image_list():
  with open('current', 'w', encoding="utf-8") as f:
     for filename in os.listdir('img'):
        f.write(f'{filename}END_NAME{os.path.getctime("img/" + filename)}\n')

def get_twenty_newest_images_as_list(image_list):
  image_list = sorted(image_list, key=lambda t: t[1])
  image_list = list(reversed(image_list))
  image_list = image_list[0:20]
  return image_list

def main():
  image_list = get_image_names_and_timestamps_as_list()
  print("got image list")

  generate_html()
  print("generated html")

  generate_rss(image_list)
  print("generated rss")

main()
