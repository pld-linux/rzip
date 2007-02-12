Summary:	A large-file compression program
Summary(pl.UTF-8):	Program do kompresowania dużych plików
Name:		rzip
Version:	2.1
Release:	0.1
License:	GPL
Group:		Applications/Archiving
Source0:	http://rzip.samba.org/ftp/rzip/%{name}-%{version}.tar.gz
# Source0-md5:	0a3ba55085661647c12f2b014c51c406
Patch0:		%{name}-destdir-mandir.patch
URL:		http://rzip.samba.org/
BuildRequires:	autoconf
BuildRequires:	bzip2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rzip is a file compression program designed to do particularly well
on very large files containing long distance redundency.

%description -l pl.UTF-8
rzip to program do kompresji plików zaprojektowany tak, aby dobrze
działał w szczególności dla dużych plików zawierających redundancję w
dużej odległości.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
