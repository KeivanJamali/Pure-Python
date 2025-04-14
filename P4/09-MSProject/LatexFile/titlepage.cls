\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{KeivanJamali}[2024/10/02]

\LoadClass[11pt, a4paper]{article}

% First load the necessary packages for text formatting
\RequirePackage{amsmath}
\RequirePackage{graphicx}
\RequirePackage{fancybox}
\RequirePackage{geometry}
\RequirePackage{multicol}
\RequirePackage{pstricks}
\RequirePackage{amssymb}
\usepackage{pgf}
\usepackage{pgfpages}
\usepackage{fancyhdr}
\usepackage{etoolbox}
\usepackage{lipsum}
\usepackage{xstring}
\usepackage{atbegshi}

% Load xepersian package last to handle Persian text properly
\RequirePackage[extrafootnotefeatures]{xepersian}

% Page layout
\setlength{\textwidth}{6.5in}
\setlength{\textheight}{9.5in}
\setlength{\oddsidemargin}{0in}
\setlength{\evensidemargin}{0in}
\setlength{\topmargin}{-0.5in}
\setlength{\headheight}{0in}
\setlength{\headsep}{1cm}

% Adding a border to the first page
% Declare a custom layout with a border
\pgfpagesdeclarelayout{boxed}
{
  \edef\pgfpageoptionborder{0pt} % Set the border size to 0pt to avoid default border
}
{
  \pgfpagesphysicalpageoptions
  {%
    logical pages=1,% Only one logical page (first page)
  }
  \pgfpageslogicalpageoptions{1}
  {
    % Draw the border around the page with 2pt thickness
    border code=\pgfsetlinewidth{3pt}\pgfstroke,% Border thickness
    border shrink=\pgfpageoptionborder,% Adjust the border size
    resized width=.95\pgfphysicalwidth,% Resize the page width by 95% for inner border
    resized height=.95\pgfphysicalheight,% Resize the page height by 95% for inner border
    center=\pgfpoint{.5\pgfphysicalwidth}{.5\pgfphysicalheight}% Center the content
  }%
}

% Use the custom layout
\pgfpagesuselayout{boxed}

% Settings for title page
\renewcommand\maketitle{
    \begin{titlepage}
        % Title content
        \begin{center}
            \vspace*{1cm}
            \fontsize{16pt}{18pt}\selectfont
            بسمه تعالی

            \vspace{1.5cm}
            \includegraphics[width=1.69in,height=1.63in]{logo.png}

            \vspace{1cm}
            دانشگاه صنعتی شریف \\
            دانشکده مهندسی عمران

            \vspace{1cm}
            پیشنهاد پایان نامه کارشناسی ارشد \\
            گرایش مهندسی حمل و نقل

            \vspace{1.25cm}
            عنوان\\
            \textbf{\mytitle}

            \vspace{1cm}
            نگارنده \\
            \textbf{\myname}

            \vspace{1cm}
            استاد راهنما \\
            \textbf{\myfrofessor}

            \vfill
            \mydate
        \end{center}
    
        
    \end{titlepage}
}

% Font setup for Persian and English
\input{Persian-Font-Code}