# revision 25417
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langcjk
Version:	20120223
Release:	1
Summary:	Chinese, Japanese, Korean
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langcjk.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-adobemapping
Requires:	texlive-arphic
Requires:	texlive-c90
Requires:	texlive-cjk
Requires:	texlive-cjkpunct
Requires:	texlive-cjkutils
Requires:	texlive-cns
Requires:	texlive-ctex
Requires:	texlive-dnp
Requires:	texlive-fonts-tlwg
Requires:	texlive-garuda-c90
Requires:	texlive-hyphen-chinese
Requires:	texlive-ipaex
Requires:	texlive-japanese
Requires:	texlive-japanese-otf
Requires:	texlive-japanese-otf-uptex
Requires:	texlive-jfontmaps
Requires:	texlive-jsclasses
Requires:	texlive-norasi-c90
Requires:	texlive-ptex
Requires:	texlive-thailatex
Requires:	texlive-uhc
Requires:	texlive-wadalab
Requires:	texlive-zhmetrics
Requires:	texlive-zhspacing
Requires:	texlive-collection-basic
Requires:	texlive-collection-documentation-chinese

%description
CJK (Chinese, Japanese, Korean) macros, fonts, documentation,
also Thai since there is some overlap in the fonts.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
