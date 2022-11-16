Name:		texlive-listofitems
Version:	51923
Release:	1
Summary:	Grab items in lists using user-specified sep char
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/listofitems
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listofitems.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listofitems.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This simple package is designed to read a list of items whose
parsing character may be selected by the user. Once the list is
read, its items are stored in a structure that behaves as a
dimensioned array. As such, it becomes very easy to access an
item in the list by its number. For example, if the list is
stored in the macro \foo, the item #3 is designated by \foo[3].
A component may, in turn, be a list with a parsing delimiter
different from the parent list, paving the way for nesting and
employing a syntax reminiscent of an array of several
dimensions of the type \foo[3,2] to access the item #2 of the
list contained within the item #3 of the top-tier list.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/listofitems
%doc %{_texmfdistdir}/doc/generic/listofitems

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
