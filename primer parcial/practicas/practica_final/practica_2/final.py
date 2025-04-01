import markdown2
from bs4 import BeautifulSoup
import os

def markdown_to_latex(md_file_path, tex_output_path, image_dir=""):
    # Read markdown
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert Markdown to HTML using markdown2
    html = markdown2.markdown(md_text, extras=["fenced-code-blocks"])

    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')

    latex_content = []

    # Add LaTeX header
    latex_content.append(r"""\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{amsmath}
\usepackage{listings}
\usepackage{color}
\usepackage{geometry}
\geometry{margin=1in}
\title{Converted Markdown}
\date{}
\begin{document}
\maketitle
""")

    # Convert elements
    for element in soup.body:
        if element.name == "h1":
            latex_content.append(f"\\section*{{{element.text}}}")
        elif element.name == "h2":
            latex_content.append(f"\\subsection*{{{element.text}}}")
        elif element.name == "h3":
            latex_content.append(f"\\subsubsection*{{{element.text}}}")
        elif element.name == "p":
            latex_content.append(element.text + "\n")
        elif element.name == "ul":
            latex_content.append("\\begin{itemize}")
            for li in element.find_all("li"):
                latex_content.append(f"  \\item {li.text}")
            latex_content.append("\\end{itemize}")
        elif element.name == "ol":
            latex_content.append("\\begin{enumerate}")
            for li in element.find_all("li"):
                latex_content.append(f"  \\item {li.text}")
            latex_content.append("\\end{enumerate}")
        elif element.name == "pre":
            code = element.text
            latex_content.append("\\begin{lstlisting}\n" + code + "\n\\end{lstlisting}")
        elif element.name == "img":
            img_src = element['src']
            image_path = os.path.join(image_dir, img_src) if image_dir else img_src
            latex_content.append(
                f"""\\begin{{figure}}[h]
\\centering
\\includegraphics[width=0.6\\textwidth]{{{image_path}}}
\\end{{figure}}"""
            )
        elif element.name == "blockquote":
            latex_content.append(f"\\begin{{quote}}{element.text}\\end{{quote}}")
        else:
            # fallback for unhandled elements
            if hasattr(element, 'text'):
                latex_content.append(element.text)

    # Close document
    latex_content.append("\\end{document}")

    # Write to .tex file
    with open(tex_output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(latex_content))

    print(f"LaTeX file written to: {tex_output_path}")


if __name__ == "__main__":
   markdown_to_latex("practica-2.md", "practica_2.tex", image_dir="imagenes")
