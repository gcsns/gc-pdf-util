import os

MARKDOWN_TO_PDF_GENERATION_TEMPLATE = os.environ.get("MARKDOWN_TO_PDF_GENERATION_TEMPLATE", """
\\documentclass{article}
\\title{Using the markdown package}
\\usepackage[smartEllipses]{markdown}
\\usepackage[a4paper, left=0.5in, right=0.5in, top=0.75in, bottom=0.75in]{geometry}

% Prevent section numbering
\\usepackage{titlesec}
\\titleformat{\\section}{\\normalfont\\Large\\bfseries}{}{0pt}{} % Removes numbering for sections
\\titleformat{\\subsection}{\\normalfont\\large\\bfseries}{}{0pt}{} % Removes numbering for subsections
\\titleformat{\\subsubsection}{\\normalfont\\normalsize\\bfseries}{}{0pt}{} % Removes numbering for subsubsections

\\begin{document}

\\begin{markdown}
<mdString>
\\end{markdown}
                                                     

\\end{document}
""")
