# revision 25356
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langgerman
Version:	20120223
Release:	1
Summary:	German
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langgerman.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-bibleref-german
Requires:	texlive-dehyph-exptl
Requires:	texlive-dhua
Requires:	texlive-booktabs-de
Requires:	texlive-csquotes-de
Requires:	texlive-etoolbox-de
Requires:	texlive-geometry-de
Requires:	texlive-german
Requires:	texlive-germbib
Requires:	texlive-germkorr
Requires:	texlive-hausarbeit-jura
Requires:	texlive-microtype-de
Requires:	texlive-r_und_s
Requires:	texlive-tipa-de
Requires:	texlive-umlaute
Requires:	texlive-hyphen-german
Requires:	texlive-collection-basic

%description
Support for typesetting German.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
