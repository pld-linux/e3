Summary:	Tiny editor
Summary(pl.UTF-8):	Mikroedytorek
Name:		e3
Version:	2.7.0
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Editors
Source0:	http://www.sax.de/~adlibit/%{name}-%{version}.tar.gz
# Source0-md5:	a76dd61c52a80a1f4d3938a4ce54c62e
Source1:	%{name}-editor.sh
Patch0:		%{name}-gcc421.patch
URL:		http://www.sax.de/~adlibit/
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	perl-base
%ifarch %{x8664}
BuildRequires:	yasm
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%description
e3 is a text micro editor with a code size less than 10000 bytes.
Except for 'undo' and 'syntax highlighting', e3 supports all of the
basic functions one expects. If you have installed the stream editor
'sed' or 'ex' you can use these tools as sub-processes, getting the
full power of regular expressions. e3 can use Wordstar-, EMACS-, Pico,
Nedit or vi-like key bindings, whichever the user chooses. e3 is
designed to be INDEPENDENT OF LIBC OR ANY OTHER library.

%description -l pl.UTF-8
e3 jest mikroskopijnym wręcz edytorem tekstu, jego rozmiar nie
przekracza 10000 bajtów. Wspiera on wszystkie podstawowe funkcje,
jakich można oczekiwać od edytora, z wyjątkiem podświetlania składni 
i cofania dokonanych zmian (undo). Jeśli chcesz skorzystać z potęgi
wyrażeń regularnych, to e3 może wywołać zewnętrzny edytor strumieni
('sed' lub 'ex'). e3 potrafi emulować ustawienia klawiszy Wordstara,
EMACSA, Pico, Nedit oraz vi. e3 nie jest zależny od żadnej biblioteki
(wliczając glibc).

%prep
%setup -q
%patch0 -p1

%build
%ifarch %{ix86}
%{__make}
%endif
%ifarch %{x8664}
%{__make} yasm64 \
	AFLAGS=-
%endif
%{__cc} %{rpmcflags} %{rpmldflags} -DLIBDIR=\"%{_libdir}\" e3c/e3.c -o e3c.bin

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}}
%ifarch %{ix86} %{x8664}
install e3 $RPM_BUILD_ROOT%{_bindir}/e3
%else
ln -sf e3c $RPM_BUILD_ROOT%{_bindir}/e3
%endif

install e3c.bin $RPM_BUILD_ROOT%{_bindir}/e3c

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/e3-editor.sh
install e3.man $RPM_BUILD_ROOT%{_mandir}/man1/e3.1
install e3c/e3c.man $RPM_BUILD_ROOT%{_mandir}/man1/e3c.1

install e3c/*.{hlp,res} $RPM_BUILD_ROOT%{_libdir}

for i in ws em pi vi ne; do
	ln -sf e3 $RPM_BUILD_ROOT%{_bindir}/e3${i}
done

for i in emacs vi pico ne ws; do
	ln -sf e3-editor.sh $RPM_BUILD_ROOT%{_bindir}/e3-$i
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog README
%attr(755,root,root) %{_bindir}/e3*
%{_mandir}/man1/e3*.1*
%{_libdir}/*.hlp
%{_libdir}/*.res
