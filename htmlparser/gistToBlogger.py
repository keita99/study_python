
#gistEmbedCode = '<script src="https://gist.github.com/keita99/2f0edc76505167a2844ce2222e14b5c6.js"></script>'
gistEmbedCode = str(input("Please input Gist Embed code : "))

pickGistCode = gistEmbedCode.rsplit('/')[4]
pickGistCode = pickGistCode.rpartition('.')[0]
#print(pickGistCode)

print("\n\r")

print("""<div class=\"gistLoad\" data-id=\"""",pickGistCode,"""\" id=\"gist-""",pickGistCode,"""/">""")
print(gistEmbedCode)
print("""</div>""")
print("""<script src="https://raw.github.com/moski/gist-Blogger/master/public/gistLoader.js" type="text/javascript"></script>""")

print("\n\r")
