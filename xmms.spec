Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Summary(pl):	Odtwarzacz d¼wiêku z interfejsem WinAmpa
Name:		xmms
Version:	1.2.5
Release:	4
Epoch:		2
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://www.xmms.org/files/1.2.x/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.gz
Source2:	mp3license
Source3:	%{name}.desktop
Source4:	wm%{name}.desktop
Source5:	%{name}-skins.tar.bz2
Source6:	%{name}-gnome-mime-info
Patch0:		%{name}-opt-flags.patch
Patch1:		%{name}-pluggedup.patch
Patch2:		%{name}-small.patch
Patch3:		%{name}-lazy.patch
Patch4:		%{name}-workaround.patch
Patch5:		%{name}-audio.patch
URL:		http://www.xmms.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	esound-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-core-devel
BuildRequires:	OpenGL
BuildRequires:	libmikmod-devel > 3.1.7
BuildRequires:	libxml-devel >= 1.7.0
BuildRequires:	zlib-devel
BuildRequires:	OpenGL-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
Requires:	glib >= 1.2.2
Requires:	gtk+ >= 1.2.2
Obsoletes:	x11amp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_mandi		%{_prefix}/man
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

%package input-mikmod
Summary:	XMMS - Input plugin to play MODs
Summary(pl):	XMMS - wtyczka do odtwarzania MODów
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
Requires:	libmikmod >= 3.1.7
Obsoletes:	xmms-mikmod
Obsoletes:	xmms-input-modplug

%description input-mikmod
Input plugin for XMMS to play MODs (.MOD,.XM,.S3M, etc). Be aware that
this plugin sucks (possibly due to quality of libmikmod) - it is
unable to play correctly a lot of modules. Use xmms-input-modplug
instaed.

%description input-mikmod -l pl
Wtyczka dla XMMS do odtwarzania MODów (.MOD,.XM,.S3M, etc). Bo±d¼
¶wiadom ¿e ta wtyczka jest bardzo s³aba (byæ mo¿e z powodu jaki¶ci
libmikmod) - nie potrafi odtworzyæ poprawnie wielu modu³ów. Zainstaluj
lepiej xmms-input-modplug.

%package input-tonegen
Summary:	XMMS - Input plugin to generate sound of given frequency
Summary(pl):	XMMS - wtyczka generuj±ca d¼wiêk o zadanej czêstotliwo¶ci
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
Obsoletes:	xmms-tonegen

%description input-tonegen
Input plugin for XMMS to generate sound of given frequency.

%description input-tonegen -l pl
Wtyczka dla XMMS generuj±ca d¼wiêk o zadanej czêstotliwo¶ci.

%package output-esd
Summary:	XMMS - Output plugin for use with the esound package
Summary(pl):	XMMS - wtyczka umo¿liwiaj±ca korzystanie z esound
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
Requires:	esound >= 0.2.8
Obsoletes:	xmms-esd

%description output-esd
Output plugin for xmms for use with the esound package.

%description output-esd -l pl
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

%package visualization-GL
Summary:	XMMS - OpenGL visualization plugins
Summary(pl):	XMMS - wtyczki OpenGL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
Requires:	OpenGL
Obsoletes:	xmms-mesa

%description visualization-GL
Visualization plugins that use the Mesa3d library.

%description visualization-GL -l pl
Wtyczki graficzne wykorzystuj±ce bibliotekê Mesa3d.

%package skins
Summary:	XMMS - Skins
Summary(pl):	XMMS - Skórki
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} >= %{version}

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
Requires:	gtk+-devel
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

%package input-vorbis
Summary:	XMMS - cdaudio input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plików vorbis
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} >= %{version}

%description input-vorbis
OGG Vorbis input plugin for XMMS.

%description -l pl input-vorbis
Wtyczna do odtwarzania plików w formacie OGG Vorbis.

%package input-cdaudio
Summary:	XMMS - cdaudio input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plyt CD-audio
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} >= %{version}

%description input-cdaudio
CD audio input plugin for XMMS.

%description -l pl input-cdaudio
Wtyczka do odtwarzania p³yt CD-audio.

%package input-idcin
Summary:	XMMS - idcin input plugin
Summary(pl):	XMMS - wtyczka do obs³ugi formatu idcin
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} >= %{version}

%description input-idcin
idcin input plugin for XMMS.

%description -l pl input-idcin
Wtyczka dla XMMSa do obs³ugi formatu idcin.

%package input-mpg123
Summary:	XMMS - mpg123 input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plikow *.mp3
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} >= %{version}

%description input-mpg123
mpg123 input plugin for XMMS.

%description -l pl input-mpg123
Wtyczka do XMMSa do obs³ugi mpg123.

%package input-wav
Summary:	XMMS - wav input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plikow *.wav
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} >= %{version}

%description input-wav
wav input plugin for XMMS.

%description -l pl input-wav
Wtyczka do XMMSa do obs³ugi plików wav.

%package output-OSS
Summary:	XMMS - OSS output plugin
Summary(pl):	XMMS - plugin obs³ugi sterowników OSS
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} >= %{version}

%description output-OSS
OSS output plugin for XMMS.

%description -l pl output-OSS
Obs³uga sterowników OSS dla XMMS.

%package output-disk
Summary:	XMMS - disk-writer output plugin
Summary(pl):	XMMS - wtyczka zapisywania danych na dysk.
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} >= %{version}

%description output-disk
disk-wirter output plugin for XMMS.

%description -l pl output-disk
Wtyczka dla XMMS zapisuj±ca dane wyj¶ciowe na dysk.

%prep
%setup -q -a1 -a5
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

cp %{SOURCE2} .

%build
rm missing
gettextize --copy --force
libtoolize --copy --force
aclocal
autoconf
automake -a -c

cd libxmms
libtoolize --copy --force
aclocal
autoconf
automake -a -c
cd ..

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Multimedia,Amusements} \
	$RPM_BUILD_ROOT%{_datadir}/{mime-info,xmms/Skins}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
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
%{_applnkdir}/Amusements/wmxmms.desktop
%attr(755,root,root) %{_bindir}/xmms
%attr(755,root,root) %{_bindir}/wmxmms
%attr(755,root,root) %{_libdir}/libxmms.so.*.*
%dir %{_libdir}/xmms
%dir %{_libdir}/xmms/General
%attr(755,root,root) %{_libdir}/xmms/General/*
%dir %{_libdir}/xmms/Effect
%attr(755,root,root) %{_libdir}/xmms/Effect/*
%dir %{_libdir}/xmms/Visualization
%attr(755,root,root) %{_libdir}/xmms/Visualization/libbscope*
%attr(755,root,root) %{_libdir}/xmms/Visualization/libsanalyzer*
%dir %{_libdir}/xmms/Input
%dir %{_libdir}/xmms/Output

%dir %{_datadir}/xmms
%{_datadir}/xmms/*gif
%{_datadir}/xmms/*xpm

%files input-mikmod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libmikmod*

%files input-tonegen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libtonegen*

%files output-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libesdout*

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnomexmms
%{_sysconfdir}/CORBA/servers/*
%{_datadir}/applets/Multimedia/*
%{_datadir}/mime-info/xmms.keys

%files visualization-GL
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

%files input-cdaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libcdaudio*

%files input-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libvorbis*

%files input-idcin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libidcin*

%files input-mpg123
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libmpg123*

%files input-wav
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libwav*

%files output-OSS
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libOSS*

%files output-disk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libdisk_writer*
