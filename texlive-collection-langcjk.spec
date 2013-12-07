# revision 32105
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langcjk
Epoch:		1
Version:	20131201
Release:	2
Summary:	Chinese/Japanese/Korean
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langcjk.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-adobemapping
Requires:	texlive-arphic
Requires:	texlive-bxbase
Requires:	texlive-bxcjkjatype
Requires:	texlive-bxjscls
Requires:	texlive-c90
Requires:	texlive-cjk
Requires:	texlive-cjk-ko
Requires:	texlive-cjkpunct
Requires:	texlive-cjkutils
Requires:	texlive-cns
Requires:	texlive-convbkmk
Requires:	texlive-ctex
Requires:	texlive-ctex-faq
Requires:	texlive-dnp
Requires:	texlive-fandol
Requires:	texlive-garuda-c90
Requires:	texlive-hyphen-chinese
Requires:	texlive-ipaex
Requires:	texlive-japanese
Requires:	texlive-japanese-otf
Requires:	texlive-japanese-otf-uptex
Requires:	texlive-jfontmaps
Requires:	texlive-jsclasses
Requires:	texlive-kotex-oblivoir
Requires:	texlive-kotex-plain
Requires:	texlive-kotex-utf
Requires:	texlive-kotex-utils
Requires:	texlive-latex-notes-zh-cn
Requires:	texlive-lshort-chinese
Requires:	texlive-lshort-japanese
Requires:	texlive-lshort-korean
Requires:	texlive-luatexja
Requires:	texlive-nanumtype1
Requires:	texlive-norasi-c90
Requires:	texlive-ptex
Requires:	texlive-ptex2pdf
Requires:	texlive-pxbase
Requires:	texlive-pxchfon
Requires:	texlive-pxcjkcat
Requires:	texlive-pxjahyper
Requires:	texlive-pxrubrica
Requires:	texlive-texlive-zh-cn
Requires:	texlive-uhc
Requires:	texlive-uptex
Requires:	texlive-wadalab
Requires:	texlive-xcjk2uni
Requires:	texlive-xpinyin
Requires:	texlive-zhmetrics
Requires:	texlive-zhnumber
Requires:	texlive-zhspacing
Requires:	texlive-zxjafbfont
Requires:	texlive-zxjafont
Requires:	texlive-zxjatype

%description
CJK (Chinese, Japanese, Korean) macros, fonts, documentation.
Also Thai in the c90 encoding, since there is some overlap in
those fonts.  Standard Thai support is in collection-langother.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
