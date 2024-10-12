from pathlib import Path

with open("scratch.txt", "w") as scratch:
    gallery = Path("./gallery")

    for dir, season in (
        ("xuan", "Xuân"),
        ("ha", "Hạ"),
        ("thu", "Thu"),
        ("dong", "Đông"),
    ):
        scratch.write(
            f"""\
<div class="season" id="{dir}">
<h1>*{season} *</h1>
<div class="gallery" id="{dir}-gallery">
"""
        )
        for pic in (gallery / dir).glob("*.JPG"):
            file = pic.name
            scratch.write(
                f'<a href="{dir}/{file}"><img src="{dir}/{file}.thumb.jpg"/></a>\n'
            )
        scratch.write("</div>\n</div>\n\n")
