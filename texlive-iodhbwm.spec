Name:		texlive-iodhbwm
Version:	57773
Release:	2
Summary:	Unofficial template of the DHBW Mannheim
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/iodhbwm
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iodhbwm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iodhbwm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an unofficial template of the DHBW
Mannheim for the creation of bachelor thesis, studies or
project work with LaTeX. The aim of the package is the quick
creation of a basic framework without much effort.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/iodhbwm
%doc %{_texmfdistdir}/doc/latex/iodhbwm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
