image_list = []

import os



with open('index.html', 'w', encoding="utf-8") as f:
   f.write('''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>⭕ GALLERY</title>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
    <meta name='robots' content='noindex,follow' />
    <style>
      body {
        font-family: monospace;
        background-color: black;
      }

      a {
        color: rgb(255, 0, 0)
      }

      a:visited {
        color: rgb(128, 0, 255)
      }
    </style>
  </head>
  <body>
    <span style="color: rgb(255, 0, 0);">TED A. GALLERY</span> ⭕<span style="color: rgb(128, 0, 255);">△</span>🌊&nbsp;
    <ul>''')
   for filename in os.listdir('img'):
      f.write(f'     <li><a href = "./img/{filename}">{filename}</a></li>\n') 
   f.write('''    </ul>
    🐍📡☀️🌿🩸⚡🛢️🏔️🧬🔨💥🪱
  </body>
</html>
''')
