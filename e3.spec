Summary:	Tiny edytor
Summary(pl):	Mikroedytorek
Name:		e3
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
#URL:		
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Small bootloader

%prep
%setup  -q
%patch0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install e3 $RPM_BUILD_ROOT%{_bindir}
install e3 $RPM_BUILD_ROOT%{_bindir}
install e3.man $RPM_BUILD_ROOT%{_mandir}/man1/e3.1
for i in ws em pi vi ne; do ln -sf e3 $RPM_BUILD_ROOT%{_bindir}/e3${i}; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
