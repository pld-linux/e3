Summary:	Tiny editor
Summary(pl):	Mikroedytorek
Name:		e3
Version:	1.61
Release:	5
License:	GPL
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores
Source0:	http://www.sax.de/~adlibit/%{name}-%{version}.tar.gz
Source1:	%{name}-editor.sh
Patch0:		%{name}-short_jump.patch
Patch1:		%{name}-%{version}-Polish_letters.patch
URL:		http://www.sax.de/~adlibit/
BuildRequires:	perl
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	uClibc-devel
BuildRequires:	uClibc-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define no_install_post_strip 1

%define embed_path	/usr/lib/embed
%define embed_cc	%{_arch}-uclibc-cc
%define embed_cflags	%{rpmcflags} -Os

%description
e3 is a text micro editor with a code size less than 10000 bytes.
Except for 'undo' and 'syntax highlighting', e3 supports all of the
basic functions one expects. If you have installed the stream editor
'sed' or 'ex' you can use these tools as sub-processes, getting the
full power of regular expressions. e3 can use Wordstar-, EMACS-,
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

%package embed
Summary:	e3 for bootdisk
Summary(pl):	e3 na bootkietkê
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores

%description embed
e3 for bootdisk.

%description embed -l pl
e3 na bootkietkê.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
# gzexe makes problems
# we gain 3K only
perl -pi -e 's/^.*gzexe e3.*$//' Makefile

%build
%ifarch %{ix86}
%{__make}
%endif
%{embed_cc} %{embed_cflags} -DLIBDIR=\"%{_libdir}\" e3c/e3.c -o e3c.shared
%{embed_cc} %{embed_cflags} -DLIBDIR=\"%{_libdir}\" -static e3c/e3.c -o e3c.static

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{embed_path}/{static,shared,%{_libdir}} \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}}

%ifarch %{ix86}
install e3 $RPM_BUILD_ROOT%{embed_path}/static/e3
install e3 $RPM_BUILD_ROOT%{embed_path}/shared/e3
install e3 $RPM_BUILD_ROOT%{_bindir}/e3
%else
ln -sf e3c $RPM_BUILD_ROOT%{embed_path}/static/e3
ln -sf e3c $RPM_BUILD_ROOT%{embed_path}/shared/e3
ln -sf e3c $RPM_BUILD_ROOT%{_bindir}/e3
%endif

install e3c.static $RPM_BUILD_ROOT%{embed_path}/static/e3c
install e3c.shared $RPM_BUILD_ROOT%{embed_path}/shared/e3c
install e3c.static $RPM_BUILD_ROOT%{_bindir}/e3c

install %{SOURCE1} $RPM_BUILD_ROOT%{embed_path}/shared/editor.sh
install %{SOURCE1} $RPM_BUILD_ROOT%{embed_path}/static/editor.sh
install e3.man $RPM_BUILD_ROOT%{_mandir}/man1/e3.1
install e3c/e3c.man $RPM_BUILD_ROOT%{_mandir}/man1/e3c.1

install e3c/*.{hlp,res} $RPM_BUILD_ROOT%{_libdir}
install e3c/*.{hlp,res} $RPM_BUILD_ROOT%{embed_path}%{_libdir}

for i in ws em pi vi ne; do
	ln -sf e3 $RPM_BUILD_ROOT%{_bindir}/e3${i}
	ln -sf e3 $RPM_BUILD_ROOT%{embed_path}/static/e3${i}
	ln -sf e3 $RPM_BUILD_ROOT%{embed_path}/shared/e3${i}
done

for i in emacs vi pico ne ws; do
	ln -sf editor.sh $RPM_BUILD_ROOT%{embed_path}/static/$i
	ln -sf editor.sh $RPM_BUILD_ROOT%{embed_path}/shared/$i
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{embed_path}%{_libdir}/*

%files embed
%defattr(644,root,root,755)
%attr(755,root,root) %{embed_path}/s*/*
%{embed_path}%{_libdir}/*
