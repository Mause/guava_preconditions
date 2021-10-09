from pathlib import Path

import pdoc

context = pdoc.Context()

module = pdoc.Module(".", context=context)
pdoc.link_inheritance(context)

README = Path("README.md")

with README.open(encoding="utf-8") as fh:
    contents = fh.read()

marker = "<!-- docs follow -->"
assert marker in contents

contents, *_ = contents.split(marker)

contents = contents.strip() + "\n" + marker + "\n" + module.text()

with README.open("w", encoding="utf-8") as fh:
    fh.write(contents)
