import sys

def help():
    print(
"""Usage:
  purgerepitedfiles [options]

Options:
  --help, -h               Display this help message

File Handling Options:
  --path, -p <directory>   Specify the source directory

  --destine, -d <directory> Specify the destination directory 

Extensions Selector:       Handle Extensions:
  --img, -i                : jpg, jpeg, png, gif, svg, bmp, tiff, 
                             tif, raw, psd, ai, eps

  --music, -m              : mp3, wav, flac, aac, ogg, wma, m4a, 
                             midi, opus, ac3

  --video, -v              : mp4, avi, mkv, mov, wmv, flv, m4v, 
                             mpeg, mpg, webm, 3gp, vob, swf

  --doc, -d                : doc, docx, pdf, txt, rtf, odt, xls, 
                             xlsx, ppt, pptx, csv, html, htm, pages

  --custom, -c             : "add your custom file extensions"

You can use these arguments wherever you want. The extensions are additive.
    """)
    sys.exit(0)