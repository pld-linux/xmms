Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Summary(pl):	Odtwarzacz d¼wiêku z interfejsem WinAmpa
Name:		xmms
Version:	1.2.3
Release:	2
Epoch:		2
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	ftp://ftp.xmms.org/xmms/1.2.x/%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.gz
Source2:	mp3license
Source3:	%{name}.desktop
Source4:	wm%{name}.desktop
Source5:	%{name}-skins.tar.bz2
Source6:	%{name}-gnome-mime-info
Patch0:		%{name}-audio.patch
Patch1:		%{name}-opt-flags.patch
Patch2:		%{name}-pluggedup.patch
Patch3:		%{name}-gettext.patch
URL:		http://www.xmms.org/
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	esound-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-core-devel
BuildRequires:	OpenGL
BuildRequires:	libmikmod-devel > 3.1.7
BuildRequires:	libxml-devel
BuildRequires:	zlib-devel
BuildRequires:	OpenGL-devel
Requires:	glib >= 1.2.2
Requires:	gtk+ >= 1.2.2
Obsoletes:	x11amp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
XMMS is a sound player written from scratch. Since it uses the WinAmp
GUI, it can use WinAmp skins, and play mp3s, mods, s3ms, and other
formats. It now has support for input, output, and general plugins,
and has also been GPL'd.

%description -l pl
XMMS jest odtwarzaczem d¼wiêku napisanym od zera. Jako, ¿e
wykorzystuje interfejs WinAmpa, mo¿e równie¿ u¿ywaæ jego 'skórek'.
Odtwarza pliki w formatach mp3, mod, s3m i wielu innych.

%package mikmod
Summary:	XMMS - Input plugin to play MODs
Summary(pl):	XMMS - wtyczka do odtwarzania MODów
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
Requires:	libmikmod >= 3.1.7

%description mikmod
Input plugin for XMMS to play MODs (.MOD,.XM,.S3M, etc)

%description mikmod -l pl
Wtyczka dla XMMS do odtwarzania MODów (.MOD,.XM,.S3M, etc).

%package tonegen
Summary:	XMMS - Input plugin to generate sound of given frequency
Summary(pl):	XMMS - wtyczka generuj±ca d¼wiêk o zadanej czêstotliwo¶ci
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}

%description tonegen
Input plugin for XMMS to generate sound of given frequency.

%description tonegen -l pl
Wtyczka dla XMMS generuj±ca d¼wiêk o zadanej czêstotliwo¶ci.

%package esd
Summary:	XMMS - Output plugin for use with the esound package
Summary(pl):	XMMS - wtyczka umo¿liwiaj±ca korzystanie z esound
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
Requires:	esound >= 0.2.8

%description esd
Output plugin for xmms for use with the esound package.

%description esd -l pl
Wtyczka dla XMMS umo¿liwiaj±ca wykorzystanie esound przy odtwarzaniu
d¼wiêków.

%package gnome
Summary:	XMMS - applet for controlling xmms from the GNOME panel
Summary(pl):	XMMS - aplet umo¿liwiaj±cy sterowanie xmms z panelu GNOME
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
Requires:	gnome-libs >= 1.0.0

%description gnome
GNOME applet for controlling xmms from the GNOME panel.

%description gnome -l pl
Aplet GNOME umo¿liwiaj±cy sterowanie xmms z panelu GNOME.

%package mesa
Summary:	XMMS - OpenGL visualization plugins
Summary(pl):	XMMS - wtyczki OpenGL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
Requires:	OpenGL

%description mesa
Visualization plugins that use the Mesa3d library.

%description mesa -l pl
Wtyczki graficzne wykorzystuj±ce bibliotekê Mesa3d.

%package skins
Summary:	XMMS - Skins
Summary(pl):	XMMS - Skórki
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}

%description skins
Additional skins for xmms.

%description skins -l pl
Dodatkowe 'skórki' dla xmms.

%package devel
Summary:	XMMS - libraries and header files
Summary(pl):	XMMS - biblioteki i pliki nag³ówkowe
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and header files required for compiling xmms plugins.

%description devel -l pl
Biblioteki i pliki nag³ówkowe wymagane do budowania wtyczek xmms.

%package static
Summary:	XMMS - static libraries
Summary(pl):	XMMS - biblioteki statyczne
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries required for compiling xmms plugins.

%description static -l pl
Biblioteki statyczne xmms.

%prep
%setup -q -a1 -a5
%patch0 -p1
%patch1 -p1
%patch2 -p1

cp %{SOURCE2} .

%build
aclocal; autoconf; automake
(cd libxmms; aclocal; autoconf; automake)
gettextize --copy --force

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Multimedia,DockApplets} \
	$RPM_BUILD_ROOT%{_datadir}/{mime-info,xmms/Skins}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/mime-info/xmms.keys
install icons/*    $RPM_BUILD_ROOT%{_datadir}/xmms
install Skins/*	   $RPM_BUILD_ROOT%{_datadir}/xmms/Skins

gzip -9nf AUTHORS ChangeLog NEWS README mp3license FAQ

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,mp3license,FAQ}.gz
%{_applnkdir}/Multimedia/xmms.desktop
%{_applnkdir}/DockApplets/wmxmms.desktop
%attr(755,root,root) %{_bindir}/xmms
%attr(755,root,root) %{_bindir}/wmxmms
%attr(755,root,root) %{_libdir}/libxmms.so.*.*

%dir %{_libdir}/xmms
%dir %{_libdir}/xmms/Input
%attr(755,root,root) %{_libdir}/xmms/Input/libcdaudio*
%attr(755,root,root) %{_libdir}/xmms/Input/libmpg123*
%attr(755,root,root) %{_libdir}/xmms/Input/libwav*
%attr(755,root,root) %{_libdir}/xmms/Input/libidcin*
%dir %{_libdir}/xmms/Output
%attr(755,root,root) %{_libdir}/xmms/Output/libOSS*
%attr(755,root,root) %{_libdir}/xmms/Output/libdisk_writer*
%dir %{_libdir}/xmms/General
%attr(755,root,root) %{_libdir}/xmms/General/*
%dir %{_libdir}/xmms/Effect
%attr(755,root,root) %{_libdir}/xmms/Effect/*
%dir %{_libdir}/xmms/Visualization
%attr(755,root,root) %{_libdir}/xmms/Visualization/libbscope*
%attr(755,root,root) %{_libdir}/xmms/Visualization/libsanalyzer*

%dir %{_datadir}/xmms
%{_datadir}/xmms/*gif
%{_datadir}/xmms/*xpm

%files mikmod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libmikmod*

%files tonegen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libtonegen*

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libesdout*

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnomexmms
%{_sysconfdir}/CORBA/servers/*
%{_datadir}/applets/Multimedia/*
%{_datadir}/mime-info/xmms.keys

%files mesa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Visualization/libogl_spectrum*

%files skins
%defattr(644,root,root,755)
%{_datadir}/xmms/Skins

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmms-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a
