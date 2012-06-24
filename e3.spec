Summary:	Tiny editor
Summary(pl):	Mikroedytorek
Name:		e3
Version:	2.43
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://www.sax.de/~adlibit/%{name}-%{version}.tar.gz
# Source0-md5:	d053f6f6bfc4619a5a3a147a498e22a2
Source1:	%{name}-editor.sh
URL:		http://www.sax.de/~adlibit/
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip 1
%define		_use_internal_dependency_generator 0

%description
e3 is a text micro editor with a code size less than 10000 bytes.
Except for 'undo' and 'syntax highlighting', e3 supports all of the
basic functions one expects. If you have installed the stream editor
'sed' or 'ex' you can use these tools as sub-processes, getting the
full power of regular expressions. e3 can use Wordstar-, EMACS-, Pico,
Nedit or vi-like key bindings, whichever the user chooses. e3 is
designed to be INDEPENDENT OF LIBC OR ANY OTHER library.

%description -l pl
e3 jest mikroskopijnym wr�cz edytorem tekstu, jego rozmiar nie
przekracza 10000 bajt�w. Wspiera on wszystkie podstawowe funkcje,
jakich mo�na oczekiwa� od edytora, z wyj�tkiem pod�wietlania sk�adni i
cofania dokonanych zmian (undo). Jesli chcesz skorzysta� z pot�gi
wyra�e� regularnych, to e3 mo�e wywo�a� zewn�trzny edytor strumieni
('sed' lub 'ex'). e3 potrafi emulowa� ustawienia klawiszy Wordstara,
EMACSA, Pico, Nedit oraz vi. e3 nie jest zale�ny od �adnej biblioteki
(wliczaj�c glibc).

%prep
%setup -q

# gzexe makes problems
# we gain 3K only
perl -pi -e 's/^.*gzexe e3.*$//' Makefile

%build
%ifarch %{ix86}
%{__make}
%endif
%{__cc} %{rpmcflags} %{rpmldflags} -DLIBDIR=\"%{_libdir}\" e3c/e3.c -o e3c.bin

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}}  
%ifarch %{ix86}
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
%attr(755,root,root) %{_bindir}/*
%doc ChangeLog README
%{_mandir}/man1/*
%{_libdir}/*
