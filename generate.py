image_list = []

import os

with open('index.html', 'w', encoding="utf-8") as f:
   f.write('''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>⭕ GALLERY</title>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
    <meta name='robots' content='noindex,follow'>
  </head>
  <body>
    <ul>
''')
   for filename in os.listdir('img'):
      f.write(f'        <li><a href = "./img/{filename}">{filename}</a></li>\n')
   f.write('''    </ul>
    <p>This is a work of fiction.
    <br>
    Names, characters, places and incidents either are products of the author’s imagination or are used fictitiously.
    <br>
    Any resemblance to actual events or locales or persons, living or dead, is entirely coincidental.</p>
  </body>
</html>
''')
