project = "Kevin Ortega — Proyectos"
copyright = "2026, Kevin Ortega"
author = "Kevin Ortega"

extensions = ["myst_parser"]
source_suffix = {
    ".md": "markdown",
}
root_doc = "index"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = project
html_baseurl = "https://kevin-ortega2724.github.io/"

myst_enable_extensions = ["colon_fence"]
