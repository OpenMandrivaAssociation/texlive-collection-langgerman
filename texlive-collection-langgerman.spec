# revision 25356
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langgerman
Epoch:		1
Version:	20120224
Release:	2
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


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780416
- Update to latest release.
- Import texlive-collection-langgerman
- Import texlive-collection-langgerman

