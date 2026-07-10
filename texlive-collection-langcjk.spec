%global tl_name collection-langcjk
%global tl_revision 78607

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Chinese/Japanese/Korean (base)
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langcjk
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langcjk.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(adobemapping)
Requires:	texlive(c90)
Requires:	texlive(cjk)
Requires:	texlive(cjk-gs-integrate)
Requires:	texlive(cjkpunct)
Requires:	texlive(cjkutils)
Requires:	texlive(collection-basic)
Requires:	texlive(dnp)
Requires:	texlive(evangelion-jfm)
Requires:	texlive(fixjfm)
Requires:	texlive(garuda-c90)
Requires:	texlive(jfmutil)
Requires:	texlive(norasi-c90)
Requires:	texlive(pxtatescale)
Requires:	texlive(xcjk2uni)
Requires:	texlive(zitie)
Requires:	texlive(zxjafont)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Packages supporting a combination of Chinese, Japanese, Korean,
including macros, fonts, documentation. Also Thai in the c90 encoding,
since there is some overlap in those fonts; standard Thai support is in
collection-langother. Additional packages for CJK are in their
individual language collections.

