# revision 34022
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langcjk
Epoch:		1
Version:	20140621
Release:	3
Summary:	Chinese/Japanese/Korean (base)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langcjk.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-adobemapping
Requires:	texlive-c90
Requires:	texlive-cjk
Requires:	texlive-cjkpunct
Requires:	texlive-cjkutils
Requires:	texlive-dnp
Requires:	texlive-garuda-c90
Requires:	texlive-norasi-c90
Requires:	texlive-xcjk2uni
Requires:	texlive-zxjafont

%description
Packages supporting a combination of Chinese, Japanese, Korean,
including macros, fonts, documentation.  Also Thai in the c90
encoding, since there is some overlap in those fonts; standard
Thai support is in collection-langother.  Additional packages
for CJK are in their individual language collections.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
