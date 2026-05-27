\NeedsTeXFormat{LaTeX2e}
% {KeivanJamali}[10/2/2024 Sharif University of Technology engineering assignments]

\LoadClass[11pt, letterpaper]{article}

\setlength{\textwidth}{6.5in}
\setlength{\textheight}{9.in}
\setlength{\oddsidemargin}{0in}
\setlength{\headheight}{0in}

\RequirePackage[margin=2cm]{geometry}

\RequirePackage{color}
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\RequirePackage{listings}
\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\footnotesize,
    breakatwhitespace=false,
    breaklines=true,
    captionpos=b,
    keepspaces=true,
    numbers=left,
    numbersep=5pt,
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=2
}
\lstset{style=mystyle}

\RequirePackage{graphicx}
\RequirePackage{fancybox}
\RequirePackage[utf8]{inputenc}
\RequirePackage{epsfig,graphicx}
\RequirePackage{multicol,pst-plot}
\RequirePackage{pstricks}
\RequirePackage{amsmath}
\RequirePackage{amsfonts}
\RequirePackage{amssymb}
\RequirePackage{eucal}

\DeclareMathOperator{\tr}{Tr}
\newcommand*{\op}[1]{\check{\mathbf#1}}
\newcommand{\bra}[1]{\langle #1 |}
\newcommand{\ket}[1]{| #1 \rangle}
\newcommand{\braket}[2]{\langle #1 | #2 \rangle}
\newcommand{\mean}[1]{\langle #1 \rangle}
\newcommand{\opvec}[1]{\check{\vec #1}}
\renewcommand{\sp}[1]{$${\begin{split}#1\end{split}}$$}

\renewcommand\maketitle{
    \begin{flushleft}
        Instructor: \professor \\
        Date: \cdate 
    \end{flushleft}

    \begin{flushright}\vspace{-20mm} \hspace{145mm}
        \centering
        \includegraphics[height=2cm]{logo.png} \hspace{10cm}
    \end{flushright}
    \begin{flushright}
        \centering
        \vspace{-3mm} \hspace{145mm} Sharif University
        \vspace{-1mm} \hspace{145mm} of Technology
    \end{flushright}

    \begin{center}\vspace{-1cm}
        \textbf{\large \course}\\
        \assignment
    \end{center}

    \rule{\linewidth}{0.1mm}

    \bigskip
    \bigskip
}
