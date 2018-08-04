#
# Gist Embed code to Blogger html script
#

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
