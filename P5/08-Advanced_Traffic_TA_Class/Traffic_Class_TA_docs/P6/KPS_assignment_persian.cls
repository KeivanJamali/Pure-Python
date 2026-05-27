\NeedsTeXFormat{LaTeX2e}
% {KeivanJamali}[2024/10/02 دانشگاه صنعتی شریف، تکالیف مهندسی]

\LoadClass[11pt, letterpaper]{article}

% تنظیمات ابعاد صفحه
\setlength{\textwidth}{6.5in}
\setlength{\textheight}{9.in}
\setlength{\oddsidemargin}{0in}
\setlength{\headheight}{0in}

% بسته xepersian برای پشتیبانی از فارسی
\RequirePackage{amsmath}
\RequirePackage{graphicx}
\RequirePackage{fancybox}
\RequirePackage[margin=2cm]{geometry}
\RequirePackage{multicol}
\RequirePackage{pstricks}
\RequirePackage{amssymb}
\RequirePackage{color}
\RequirePackage{listings}
\RequirePackage{epsfig,graphicx}
\RequirePackage{multicol,pst-plot}
\RequirePackage{amsfonts}
\RequirePackage{eucal}
\usepackage{lipsum}
\usepackage{float}
\usepackage{svg}
\RequirePackage[extrafootnotefeatures]{xepersian}
% رنگ‌بندی برای کدها
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

% تنظیمات بسته listings برای نمایش کد
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
% قالب‌بندی صفحه عنوان
\renewcommand\maketitle{
    \begin{flushright}
        \textbf{نام دانشجو:} \name \\
        \textbf{شماره دانشجویی:} \id \\
        \textbf{استاد درس:} \professor \\
        \textbf{تاریخ:} \cdate
    \end{flushright}

    \begin{flushleft}\vspace{-3cm}
        \includegraphics[height=2cm]{logo.png} \hspace{10cm}
    \end{flushleft}
    \begin{flushleft}
        \vspace{-8mm} \hspace{300cm} دانشگاه صنعتی شریف
    \end{flushleft}

    \begin{center}\vspace{-1cm}
        \textbf{\large \course}\\
        \assignment
    \end{center}

    \rule{\linewidth}{0.1mm}

    \bigskip
    \bigskip
}

% بسته فونت فارسی
\input{font-persian}
