Name:		texlive-collection-langgerman
Epoch:		1
Version:	55706
Release:	2
Summary:	German
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langgerman.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-babel-german
Requires:	texlive-bibleref-german
Requires:	texlive-booktabs-de
Requires:	texlive-csquotes-de
Requires:	texlive-dehyph-exptl
Requires:	texlive-dhua
Requires:	texlive-einfuehrung
Requires:	texlive-etoolbox-de
Requires:	texlive-fifinddo-info
Requires:	texlive-geometry-de
Requires:	texlive-german
Requires:	texlive-germbib
Requires:	texlive-germkorr
Requires:	texlive-hausarbeit-jura
Requires:	texlive-hyphen-german
Requires:	texlive-koma-script-examples
Requires:	texlive-l2picfaq
Requires:	texlive-l2tabu
Requires:	texlive-latex-bib-ex
Requires:	texlive-latex-referenz
Requires:	texlive-latex-tabellen
Requires:	texlive-lshort-german
Requires:	texlive-lualatex-doc-de
Requires:	texlive-microtype-de
Requires:	texlive-presentations
Requires:	texlive-pstricks-examples
Requires:	texlive-r_und_s
Requires:	texlive-templates-fenn
Requires:	texlive-templates-sommer
Requires:	texlive-texlive-de
Requires:	texlive-tipa-de
Requires:	texlive-translation-arsclassica-de
Requires:	texlive-translation-biblatex-de
Requires:	texlive-translation-chemsym-de
Requires:	texlive-translation-ecv-de
Requires:	texlive-translation-enumitem-de
Requires:	texlive-translation-europecv-de
Requires:	texlive-translation-filecontents-de
Requires:	texlive-translation-moreverb-de
Requires:	texlive-udesoftec
Requires:	texlive-umlaute
Requires:	texlive-voss-mathcol

%description
Support for German.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
