Summary:	Tiny editor
Summary(pl):	Mikroedytorek
Name:		e3
Version:	1.61
Release:	1
License:	GPL
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores
Source0:	http://www.sax.de/~adlibit/%{name}-%{version}.tar.gz
Source1:	%{name}-editor.sh
URL:		http://www.sax.de/~adlibit/
BuildRequires:	nasm
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define no_install_post_strip 1

%description
e3 is a text micro editor with a code size less than 10000 bytes.
Except for 'undo' and 'syntax highlighting', e3 supports all of the
basic functions one expects. If you have installed the stream editor
'sed' or 'ex' you can use these tools as sub-processes, getting the
full power of regular expressions.  e3 can use Wordstar-, EMACS-,
Pico, Nedit or vi-like key bindings, whichever the user chooses.
e3 is designed to be INDEPENDENT OF LIBC OR ANY OTHER library.

%description -l pl
e3 jest mikroskopijnym wrêcz edytorem tekstu, jego rozmiar nie
przekracza 10000 bajtów. Wspiera on wszystkie podstawowe funkcje,
jakich mo¿na oczekiwaæ od edytora, z wyj±tkiem pod¶wietlania sk³adni
i cofania dokonanych zmian (undo). Jesli chcesz skorzystaæ z potêgi
wyra¿eñ regularnych, to e3 mo¿e wywo³aæ zewnêtrzny edytor strumieni
('sed' lub 'ex'). e3 potrafi emulowaæ ustawienia klawiszy Wordstara,
EMACSA, Pico, Nedit oraz vi. e3 nie jest zale¿ny od ¿adnej biblioteki
(wliczaj±c glibc).

%package BOOT
Summary:	e3 for bootdisk
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores

%description BOOT
e3 for bootdisk.

%prep
%setup  -q
# gzexe makes problems
# we gain 3K only
perl -pi -e 's/^.*gzexe e3.*$//' Makefile

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk/bin \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install e3 $RPM_BUILD_ROOT%{_libdir}/bootdisk/bin
install e3 $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/bootdisk/bin/editor.sh
install e3.man $RPM_BUILD_ROOT%{_mandir}/man1/e3.1

for i in ws em pi vi ne; do \
	ln -sf e3 $RPM_BUILD_ROOT%{_bindir}/e3${i}; \
	ln -sf e3 $RPM_BUILD_ROOT%{_libdir}/bootdisk/bin/e3${i}; \
done

for i in emacs vi pico ne ws; do \
	ln -sf editor.sh $RPM_BUILD_ROOT%{_libdir}/bootdisk/bin/$i; \
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bootdisk/bin/*
