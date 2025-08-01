Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Summary(es.UTF-8):	Editor de sonido con GUI semejante al de WinAmp
Summary(ja.UTF-8):	XMMS - X Window System上で動作するマルチメディアプレーヤー
Summary(ko.UTF-8):	Unix 베이스 시스템을 위한 winamp 모양의 음악 연주기
Summary(pl.UTF-8):	Odtwarzacz dźwięku z interfejsem WinAmpa
Summary(pt_BR.UTF-8):	Tocador de som com GUI semelhante ao do WinAmp
Summary(ru.UTF-8):	Проигрыватель музыки с WinAmp GUI
Summary(uk.UTF-8):	Програвач музики з WinAmp GUI
Summary(zh_CN.UTF-8):	XMMS - X 端多媒体播放器
Name:		xmms
Version:	1.2.11
Release:	9
Epoch:		2
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://www.xmms.org/files/1.2.x/%{name}-%{version}.tar.bz2
# Source0-md5:	f3e6dbaf0b3f571a532ab575656be506
Source1:	%{name}-icons.tar.gz
# Source1-md5:	14fc5a0bb3679daf1c3900e3a30674e9
Source2:	%{name}-skins.tar.bz2
# Source2-md5:	39d6de4bf2c37c17b868df3596871c59
Source3:	%{name}.desktop
Source4:	wm%{name}.desktop
Source5:	%{name}-gnome-mime-info
Source6:	%{name}.png
Patch0:		%{name}-warn_about_unplayables.patch
Patch1:		%{name}-gcc4.patch
Patch2:		%{name}-no-esd.patch
#Patch1:		%{name}-gtk2.patch
URL:		http://www.xmms.org/
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel >= 0.9.5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	libmikmod-devel > 3.1.7
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	libxml-devel >= 1.7.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zlib-devel
Requires:	glib >= 1.2.2
Requires:	gtk+ >= 1.2.2
Requires:	xmms-output-plugin
Suggests:	xmms-input-FMRadio
Suggests:	xmms-input-cdaudio
Suggests:	xmms-input-faad2
Suggests:	xmms-input-flac
Suggests:	xmms-input-midi
Suggests:	xmms-input-mikmod
Suggests:	xmms-input-mpg123
Suggests:	xmms-input-musepack
Suggests:	xmms-input-sap
Suggests:	xmms-input-shn
Suggests:	xmms-input-smpeg
Suggests:	xmms-input-sndfile
Suggests:	xmms-input-uade
Suggests:	xmms-input-vorbis
Suggests:	xmms-input-wav
Obsoletes:	x11amp
Obsoletes:	xmms-gnome
Obsoletes:	xmms-output-esd
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
XMMS is a sound player written from scratch. Since it uses the WinAmp
GUI, it can use WinAmp skins, and play MP3s, mods, s3ms, and other
formats. It now has support for input, output, and general plugins,
and has also been GPL'd.

%description -l es.UTF-8
Editor de sonido con GUI semejante al de WinAmp.

%description -l pl.UTF-8
XMMS jest odtwarzaczem dźwięku napisanym od zera. Jako że wykorzystuje
interfejs WinAmpa, może również używać jego 'skórek'. Odtwarza pliki w
formatach MP3, mod, s3m i wielu innych. Teraz obsługuje także pluginy
do wejścia, wyjścia oraz ogólne; został także zGPL-izowany.

%description -l pt_BR.UTF-8
XMMS é um sound player escrito a partir do zero. Como ele utiliza a
interface do WinAmp, ele pode utilizar "skins" do WinAmp, e tocar
arquivos .MP3, .mod, .s3m, e outros formatos. Agora ele suporta
plugins de entrada, saída e outros plugins de uso geral, e sua licença
se tornou GPL.

%description -l ru.UTF-8
XMMS - проигрыватель музыки с графическим интерфейсом, напоминающим
интерфейс WinAmp. Он может использовать "скины" WinAmp, проигрывать
MP3, mod, s3m и другие форматы. Теперь он поддерживает подключаемые
модули для обработки ввода, вывода, общего назначения и визуализации.

%description -l uk.UTF-8
XMMS - програвач музики з графічним інтерфейсом, що нагадує інтерфейс
WinAmp. Він може використовувати" скіни" WinAmp, програвати MP3, mod,
s3m та інші формати. Тепер він підтримує під'єднувані модулі обробки
вводу, виводу, модулі загального призначення та візуалізації.

%package wm
Summary:	XMMS applet for WindowMaker
Summary(pl.UTF-8):	Aplet XMMS dla WindowMakera
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description wm
XMMS applet for WindowMaker.

%description wm -l pl.UTF-8
Aplet XMMS dla WindowMakera.

%package skins
Summary:	XMMS - Skins
Summary(pl.UTF-8):	XMMS - Skórki
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}
Requires:	unzip

%description skins
Additional skins for XMMS.

%description skins -l pl.UTF-8
Dodatkowe 'skórki' dla XMMS-a.

%package libs
Summary:	XMMS library
Summary(pl.UTF-8):	Biblioteka XMMS
Group:		X11/Applications/Sound

%description libs
XMMS library.

%description libs -l pl.UTF-8
Biblioteka XMMS.

%package devel
Summary:	XMMS - libraries and header files
Summary(es.UTF-8):	Bibliotecas y archivos de inclusión, necesarios para compilar plugins de XMMS
Summary(ja.UTF-8):	XMMS - 開発用ファイル
Summary(ko.UTF-8):	XMMS - 라이브러리와 헤더 파일들
Summary(pl.UTF-8):	XMMS - biblioteki i pliki nagłówkowe
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão necessários para se compilar plugins do XMMS
Summary(ru.UTF-8):	.h-файлы для XMMS
Summary(uk.UTF-8):	.h-файли для XMMS
Summary(zh_CN.UTF-8):	XMMS - 开发库
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gtk+-devel

%description devel
Libraries and header files required for compiling XMMS plugins.

%description devel -l es.UTF-8
Bibliotecas y archivos de inclusión, necesarios para compilar plugins
de XMMS.

%description devel -l pl.UTF-8
Biblioteki i pliki nagłówkowe wymagane do budowania wtyczek dla
XMMS-a.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão necessários para se compilar
plugins do XMMS.

%description devel -l ru.UTF-8
.h-файлы для построения подключаемых модулей для XMMS.

%description devel -l uk.UTF-8
.h-файли для побудови під'єднуваних модулів для XMMS.

%package static
Summary:	XMMS - static libraries
Summary(es.UTF-8):	Static libraries for XMMS development
Summary(pl.UTF-8):	XMMS - biblioteki statyczne
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com XMMS
Summary(ru.UTF-8):	Статические библиотеки для XMMS
Summary(uk.UTF-8):	Статичні бібліотеки для XMMS
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libraries required for compiling XMMS plugins.

%description static -l es.UTF-8
Static libraries for XMMS development.

%description static -l pl.UTF-8
Biblioteki statyczne XMMS-a.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com o XMMS.

%description static -l ru.UTF-8
Статические библиотеки для построения подключаемых модулей для XMMS.

%description static -l uk.UTF-8
Статичні бібліотеки для побудови під'єднуваних модулів для XMMS.

%package gnome-mime-info
Summary:	MIME functions for GNOME
Summary(pl.UTF-8):	Funkcje MIME dla GNOME
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnome-mime-data

%description gnome-mime-info
MIME functions for GNOME.

%description gnome-mime-info -l pl.UTF-8
Funkcje MIME dla GNOME.

%package input-mikmod
Summary:	XMMS - Input plugin to play MODs
Summary(es.UTF-8):	Login de entrada para que XMMS alcance MODs (.MOD,.XM,.S3M, etc)
Summary(ja.UTF-8):	XMMS - MODsを再生するための入力プラグイン
Summary(pl.UTF-8):	XMMS - wtyczka do odtwarzania MODów
Summary(pt_BR.UTF-8):	Plugin de entrada para o XMMS tocar MODs (.MOD,.XM,.S3M, etc)
Summary(zh_CN.UTF-8):	XMMS - 播放 M0Ds 文件的输入插件
Group:		X11/Applications/Sound
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	libmikmod >= 3.1.7
Obsoletes:	xmms-input-modplug
Obsoletes:	xmms-mikmod

%description input-mikmod
Input plugin for XMMS to play MODs (.MOD,.XM,.S3M, etc). Be aware that
this plugin sucks (possibly due to quality of libmikmod) - it is
unable to play correctly a lot of modules. Use xmms-input-modplug
instaed.

%description input-mikmod -l es.UTF-8
Login de entrada para que XMMS alcance MODs (.MOD,.XM,.S3M, etc).

%description input-mikmod -l pl.UTF-8
Wtyczka dla XMMS-a do odtwarzania MODów (.MOD,.XM,.S3M, etc). Bądź
świadom, że ta wtyczka jest bardzo słaba (być może z powodu jakości
libmikmod) - nie potrafi odtworzyć poprawnie wielu modułów. Zainstaluj
lepiej xmms-input-modplug.

%description input-mikmod -l pt_BR.UTF-8
Plugin de entrada para o XMMS tocar MODs (.MOD,.XM,.S3M, etc).

%package input-tonegen
Summary:	XMMS - Input plugin to generate sound of given frequency
Summary(pl.UTF-8):	XMMS - wtyczka generująca dźwięk o zadanej częstotliwości
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xmms-tonegen

%description input-tonegen
Input plugin for XMMS to generate sound of given frequency.

%description input-tonegen -l pl.UTF-8
Wtyczka dla XMMS-a generująca dźwięk o zadanej częstotliwości.

%package input-vorbis
Summary:	XMMS - Ogg Vorbis input plugin
Summary(ja.UTF-8):	XMMS - Oggsを再生するための入力プラグイン
Summary(pl.UTF-8):	XMMS - wtyczka do odtwarzania plików Ogg Vorbis
Summary(zh_CN.UTF-8):	XMMS - 播放 0GGs 编码文件的输入插件
Group:		X11/Applications/Sound
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description input-vorbis
Ogg Vorbis input plugin for XMMS.

%description input-vorbis -l pl.UTF-8
Wtyczka do odtwarzania plików w formacie Ogg Vorbis.

%package input-cdaudio
Summary:	XMMS - cdaudio input plugin
Summary(pl.UTF-8):	XMMS - wtyczka do odtwarzania plyt CD-audio
Group:		X11/Applications/Sound
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description input-cdaudio
CD audio input plugin for XMMS.

%description input-cdaudio -l pl.UTF-8
Wtyczka do odtwarzania płyt CD-audio.

%package input-mpg123
Summary:	XMMS - mpg123 input plugin
Summary(pl.UTF-8):	XMMS - wtyczka do odtwarzania plikow MP3
Group:		X11/Applications/Sound
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description input-mpg123
mpg123 input plugin for XMMS.

%description input-mpg123 -l pl.UTF-8
Wtyczka dla XMMS-a do obsługi mpg123.

%package input-wav
Summary:	XMMS - WAV input plugin
Summary(pl.UTF-8):	XMMS - wtyczka do odtwarzania plików WAV
Group:		X11/Applications/Sound
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description input-wav
WAV input plugin for XMMS.

%description input-wav -l pl.UTF-8
Wtyczka dla XMMS-a do obsługi plików WAV.

%package output-OSS
Summary:	XMMS - OSS output plugin
Summary(pl.UTF-8):	XMMS - plugin obsługi sterowników OSS
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xmms-output-plugin

%description output-OSS
OSS output plugin for XMMS.

%description output-OSS -l pl.UTF-8
Obsługa sterowników OSS dla XMMS-a.

%package output-ALSA
Summary:	XMMS - ALSA output plugin
Summary(pl.UTF-8):	XMMS - plugin obsługi sterowników Alsa
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xmms-output-plugin
Obsoletes:	xmms-output-aalsa
Obsoletes:	xmms-output-alsa

%description output-ALSA
ALSA output plugin for XMMS.

%description output-ALSA -l pl.UTF-8
Obsługa sterowników ALSA dla XMMS-a.

%package output-disk
Summary:	XMMS - disk-writer output plugin
Summary(pl.UTF-8):	XMMS - wtyczka do zapisywania danych na dysk
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xmms-output-plugin

%description output-disk
disk-wirter output plugin for XMMS.

%description output-disk -l pl.UTF-8
Wtyczka dla XMMS-a zapisująca dane wyjściowe na dysk.

%package visualization-GL
Summary:	XMMS - Visualization plugins that use the OenGL library
Summary(ja.UTF-8):	XMMS - OpenGLを利用したグラフィカルな視覚化プラグイン
Summary(pl.UTF-8):	XMMS - wtyczki do wizualizacji z użyciem OpenGL
Summary(ru.UTF-8):	XMMS - подключаемые модули визуализации, использующие библиотеку OenGL
Summary(uk.UTF-8):	XMMS - під'єднувані модулі візуалізації, які використовують бібліотеку OpenGL
Summary(zh_CN.UTF-8):	XMMS - 可视化插件
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xmms-mesa

%description visualization-GL
XMMS - Visualization plugins that use the OpenGL library.

%description visualization-GL -l pl.UTF-8
Wtyczki graficzne wykorzystujące bibliotekę OpenGL.

%description visualization-GL -l ru.UTF-8
XMMS - подключаемые модули визуализации, использующие библиотеку
OpenGL.

%description visualization-GL -l uk.UTF-8
XMMS - під'єднувані модулі візуалізації, які використовують бібліотеку
OpenGL.

%prep
%setup -q -a1 -a2
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

mv -f po/{no,nb}.po
%{__perl} -pi -e 's/ no / nb /' po/LINGUAS
# allow (re)building, incl. nb.gmo
rm -f po/stamp-po

install -d m4
# get only XMMS_* macros
head -n60 libxmms/acinclude.m4 > m4/xmms-macros.m4

%build
# kill old libtool.m4 copy
rm -f acinclude.m4
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

cd libxmms
# kill old libtool.m4 copy
rm -f acinclude.m4
%{__aclocal} -I ../m4
%{__autoconf}
%{__autoheader}
# don't use --force here
automake -a -c --foreign
cd ..

%configure \
	--disable-vorbistest \
%ifarch %{ix86}
	--enable-simd
%endif

%{__make} \
	AS="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/{mime-info,xmms/Skins}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}
install icons/*    $RPM_BUILD_ROOT%{_datadir}/xmms
install Skins/*    $RPM_BUILD_ROOT%{_datadir}/xmms/Skins
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/mime-info/xmms.keys
install %{SOURCE6} $RPM_BUILD_ROOT%{_pixmapsdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/xmms/*/*.la

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
        mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README FAQ
%attr(755,root,root) %{_bindir}/xmms
%dir %{_libdir}/xmms/Effect
%attr(755,root,root) %{_libdir}/xmms/Effect/*.so
%dir %{_libdir}/xmms/General
%attr(755,root,root) %{_libdir}/xmms/General/*.so
%dir %{_libdir}/xmms/Output
%dir %{_libdir}/xmms/Visualization
%attr(755,root,root) %{_libdir}/xmms/Visualization/libbscope.so
%attr(755,root,root) %{_libdir}/xmms/Visualization/libsanalyzer.so
%dir %{_datadir}/xmms
%dir %{_datadir}/xmms/Skins
%{_datadir}/xmms/*gif
%{_datadir}/xmms/x*xpm
%{_desktopdir}/xmms.desktop
%{_pixmapsdir}/xmms.png
%{_mandir}/man1/xmms.1*

%files wm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wmxmms
%{_datadir}/xmms/wmxmms*.xpm
%{_desktopdir}/wmxmms.desktop
%{_mandir}/man1/wmxmms.1*

%files skins
%defattr(644,root,root,755)
%{_datadir}/xmms/Skins/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmms.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmms.so.1
%dir %{_libdir}/xmms
%dir %{_libdir}/xmms/Input

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmms-config
%attr(755,root,root) %{_libdir}/libxmms.so
%{_libdir}/libxmms.la
%{_includedir}/xmms
%{_aclocaldir}/xmms.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libxmms.a

%files gnome-mime-info
%defattr(644,root,root,755)
%{_datadir}/mime-info/xmms.keys

%files input-mikmod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libmikmod.so

%files input-tonegen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libtonegen.so

%files input-cdaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libcdaudio.so

%files input-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libvorbis.so

%files input-mpg123
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libmpg123.so

%files input-wav
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libwav.so

%files output-OSS
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libOSS.so

%files output-ALSA
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libALSA.so

%files output-disk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libdisk_writer.so

%files visualization-GL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Visualization/libogl_spectrum.so
