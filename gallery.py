from pathlib import Path

with open("scratch.txt", "w") as scratch:
    gallery = Path("./gallery")

    for dir, season in (("cuoi", "Đám cưới"),):
        scratch.write(
            f"""\
<div class="season" id="{dir}">
<h1>*{season} *</h1>
<div class="gallery" id="{dir}-gallery">
"""
        )
        for pic in (gallery / dir).glob("*.*"):
            if pic.name.endswith("thumb.jpg"):
                continue
            file = pic.name
            scratch.write(
                f'<a href="{dir}/{file}"><img src="{dir}/{file}.thumb.jpg"/></a>\n'
            )
        scratch.write("</div>\n</div>\n\n")
