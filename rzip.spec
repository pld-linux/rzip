Summary:	A large-file compression program
Summary(pl):	Program do kompresowania du¿ych plików
Name:		rzip
Version:	2.0
Release:	0.1
License:	GPL
Group:		Applications/Archiving
Source0:	http://rzip.samba.org/ftp/rzip/%{name}-%{version}.tar.gz
# Source0-md5:	8a88b445afba919b122a3899d6d26b2a
Patch0:		%{name}-destdir-mandir.patch
URL:		http://rzip.samba.org/
BuildRequires:	autoconf
BuildRequires:	bzip2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rzip is a file compression program designed to do particularly well
on very large files containing long distance redundency.

%prep
%setup -q -n %{name}-%{version}
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

%postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
