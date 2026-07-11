%global tl_name listofitems
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.65
Release:	%{tl_revision}.1
Summary:	Grab items in lists using user-specified sep char
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/listofitems
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listofitems.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listofitems.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This simple package is designed to read a list of items whose parsing
character may be selected by the user. Once the list is read, its items
are stored in a structure that behaves as a dimensioned array. As such,
it becomes very easy to access an item in the list by its number. For
example, if the list is stored in the macro \foo, the item #3 is
designated by \foo[3]. A component may, in turn, be a list with a
parsing delimiter different from the parent list, paving the way for
nesting and employing a syntax reminiscent of an array of several
dimensions of the type \foo[3,2] to access the item #2 of the list
contained within the item #3 of the top-tier list.

