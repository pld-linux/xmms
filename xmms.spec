#
# Conditional build:
%bcond_with	gtk2	# experimental GTK+2 port (and probably broken/incomplete)
			# (deprecated - many plugins won't work, use beep instead)
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Summary(es):	Editor de sonido con GUI semejante al de WinAmp
Summary(ja):	XMMS - X Window System¾å¤ÇÆ°ºî¤¹¤ë¥Þ¥ë¥Á¥á¥Ç¥£¥¢¥×¥ì¡¼¥ä¡¼
Summary(ko):	Unix º£ÀÌ½º ½Ã½ºÅÛÀ» À§ÇÑ winamp ¸ð¾çÀÇ À½¾Ç ¿¬ÁÖ±â
Summary(pl):	Odtwarzacz d¼wiêku z interfejsem WinAmpa
Summary(pt_BR):	Tocador de som com GUI semelhante ao do WinAmp
Summary(ru):	ðÒÏÉÇÒÙ×ÁÔÅÌØ ÍÕÚÙËÉ Ó WinAmp GUI
Summary(uk):	ðÒÏÇÒÁ×ÁÞ ÍÕÚÉËÉ Ú WinAmp GUI
Summary(zh_CN):	XMMS - X ¶Ë¶àÃ½Ìå²¥·ÅÆ÷
Name:		xmms
Version:	1.2.10
Release:	6
Epoch:		2
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://www.xmms.org/files/1.2.x/%{name}-%{version}.tar.bz2
# Source0-md5:	03a85cfc5e1877a2e1f7be4fa1d3f63c
Source1:	%{name}-icons.tar.gz
# Source1-md5:	14fc5a0bb3679daf1c3900e3a30674e9
Source2:	mp3license
Source3:	%{name}.desktop
Source4:	wm%{name}.desktop
Source5:	%{name}-skins.tar.bz2
# Source5-md5:	39d6de4bf2c37c17b868df3596871c59
Source6:	%{name}-gnome-mime-info
Source7:	%{name}.png
Patch0:		%{name}-warn_about_unplayables.patch
Patch1:		%{name}-am18.patch
Patch2:		%{name}-gtk2.patch
Patch3:		%{name}-gcc4.patch
Patch4:		%{name}-alsa-mono-vol-adjust.patch
URL:		http://www.xmms.org/
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel >= 0.9.5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	libmikmod-devel > 3.1.7
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	libxml-devel >= 1.7.0
BuildRequires:	perl-base
BuildRequires:	zlib-devel
%if %{with gtk2}
BuildRequires:	gtk+2-devel >= 2:2.2.0
# broken/incomplete patch? links with both GTK+ versions
BuildRequires:	gtk+-devel >= 1.2.2
%else
BuildRequires:	gtk+-devel >= 1.2.2
Requires:	glib >= 1.2.2
Requires:	gtk+ >= 1.2.2
%endif
Requires:	xmms-output-plugin
Obsoletes:	x11amp
Obsoletes:	xmms-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
XMMS is a sound player written from scratch. Since it uses the WinAmp
GUI, it can use WinAmp skins, and play MP3s, mods, s3ms, and other
formats. It now has support for input, output, and general plugins,
and has also been GPL'd.

%description -l es
Editor de sonido con GUI semejante al de WinAmp.

%description -l pl
XMMS jest odtwarzaczem d¼wiêku napisanym od zera. Jako ¿e wykorzystuje
interfejs WinAmpa, mo¿e równie¿ u¿ywaæ jego 'skórek'. Odtwarza pliki w
formatach MP3, mod, s3m i wielu innych. Teraz obs³uguje tak¿e pluginy
do wej¶cia, wyj¶cia oraz ogólne; zosta³ tak¿e zGPL-izowany.

%description -l pt_BR
XMMS é um sound player escrito a partir do zero. Como ele utiliza a
interface do WinAmp, ele pode utilizar "skins" do WinAmp, e tocar
arquivos .MP3, .mod, .s3m, e outros formatos. Agora ele suporta
plugins de entrada, saída e outros plugins de uso geral, e sua licença
se tornou GPL.

%description -l ru
XMMS - ÐÒÏÉÇÒÙ×ÁÔÅÌØ ÍÕÚÙËÉ Ó ÇÒÁÆÉÞÅÓËÉÍ ÉÎÔÅÒÆÅÊÓÏÍ, ÎÁÐÏÍÉÎÁÀÝÉÍ
ÉÎÔÅÒÆÅÊÓ WinAmp. ïÎ ÍÏÖÅÔ ÉÓÐÏÌØÚÏ×ÁÔØ "ÓËÉÎÙ" WinAmp, ÐÒÏÉÇÒÙ×ÁÔØ
MP3, mod, s3m É ÄÒÕÇÉÅ ÆÏÒÍÁÔÙ. ôÅÐÅÒØ ÏÎ ÐÏÄÄÅÒÖÉ×ÁÅÔ ÐÏÄËÌÀÞÁÅÍÙÅ
ÍÏÄÕÌÉ ÄÌÑ ÏÂÒÁÂÏÔËÉ ××ÏÄÁ, ×Ù×ÏÄÁ, ÏÂÝÅÇÏ ÎÁÚÎÁÞÅÎÉÑ É ×ÉÚÕÁÌÉÚÁÃÉÉ.

%description -l uk
XMMS - ÐÒÏÇÒÁ×ÁÞ ÍÕÚÉËÉ Ú ÇÒÁÆ¦ÞÎÉÍ ¦ÎÔÅÒÆÅÊÓÏÍ, ÝÏ ÎÁÇÁÄÕ¤ ¦ÎÔÅÒÆÅÊÓ
WinAmp. ÷¦Î ÍÏÖÅ ×ÉËÏÒÉÓÔÏ×Õ×ÁÔÉ" ÓË¦ÎÉ" WinAmp, ÐÒÏÇÒÁ×ÁÔÉ MP3, mod,
s3m ÔÁ ¦ÎÛ¦ ÆÏÒÍÁÔÉ. ôÅÐÅÒ ×¦Î Ð¦ÄÔÒÉÍÕ¤ Ð¦Ä'¤ÄÎÕ×ÁÎ¦ ÍÏÄÕÌ¦ ÏÂÒÏÂËÉ
××ÏÄÕ, ×É×ÏÄÕ, ÍÏÄÕÌ¦ ÚÁÇÁÌØÎÏÇÏ ÐÒÉÚÎÁÞÅÎÎÑ ÔÁ ×¦ÚÕÁÌ¦ÚÁÃ¦§.

%package wm
Summary:	XMMS applet for WindowMaker
Summary(pl):	Aplet XMMS dla WindowMakera
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description wm
XMMS applet for WindowMaker.

%description wm -l pl
Aplet XMMS dla WindowMakera.

%package skins
Summary:	XMMS - Skins
Summary(pl):	XMMS - Skórki
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}
Requires:	unzip

%description skins
Additional skins for XMMS.

%description skins -l pl
Dodatkowe 'skórki' dla XMMS-a.

%package libs
Summary:	XMMS library
Summary(pl):	Biblioteka XMMS
Group:		X11/Applications/Sound

%description libs
XMMS library.

%description libs -l pl
Biblioteka XMMS.

%package devel
Summary:	XMMS - libraries and header files
Summary(es):	Bibliotecas y archivos de inclusión, necesarios para compilar plugins de XMMS
Summary(ja):	XMMS - ³«È¯ÍÑ¥Õ¥¡¥¤¥ë
Summary(ko):	XMMS - ¶óÀÌºê·¯¸®¿Í Çì´õ ÆÄÀÏµé
Summary(pl):	XMMS - biblioteki i pliki nag³ówkowe
Summary(pt_BR):	Bibliotecas e arquivos de inclusão necessários para se compilar plugins do XMMS
Summary(ru):	.h-ÆÁÊÌÙ ÄÌÑ XMMS
Summary(uk):	.h-ÆÁÊÌÉ ÄÌÑ XMMS
Summary(zh_CN):	XMMS - ¿ª·¢¿â
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
# broken/incomplete gtk2 patch? libxmms is still linked with old GTK+
Requires:	gtk+-devel

%description devel
Libraries and header files required for compiling XMMS plugins.

%description devel -l es
Bibliotecas y archivos de inclusión, necesarios para compilar plugins
de XMMS.

%description devel -l pl
Biblioteki i pliki nag³ówkowe wymagane do budowania wtyczek dla
XMMS-a.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão necessários para se compilar
plugins do XMMS.

%description devel -l ru
.h-ÆÁÊÌÙ ÄÌÑ ÐÏÓÔÒÏÅÎÉÑ ÐÏÄËÌÀÞÁÅÍÙÈ ÍÏÄÕÌÅÊ ÄÌÑ XMMS.

%description devel -l uk
.h-ÆÁÊÌÉ ÄÌÑ ÐÏÂÕÄÏ×É Ð¦Ä'¤ÄÎÕ×ÁÎÉÈ ÍÏÄÕÌ¦× ÄÌÑ XMMS.

%package static
Summary:	XMMS - static libraries
Summary(es):	Static libraries for XMMS development
Summary(pl):	XMMS - biblioteki statyczne
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com XMMS
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ XMMS
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ XMMS
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libraries required for compiling XMMS plugins.

%description static -l es
Static libraries for XMMS development.

%description static -l pl
Biblioteki statyczne XMMS-a.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com o XMMS.

%description static -l ru
óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÐÏÓÔÒÏÅÎÉÑ ÐÏÄËÌÀÞÁÅÍÙÈ ÍÏÄÕÌÅÊ ÄÌÑ XMMS.

%description static -l uk
óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÐÏÂÕÄÏ×É Ð¦Ä'¤ÄÎÕ×ÁÎÉÈ ÍÏÄÕÌ¦× ÄÌÑ XMMS.

%package gnome-mime-info
Summary:	MIME functions for GNOME
Summary(pl):	Funkcje MIME dla GNOME
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnome-mime-data

%description gnome-mime-info
MIME functions for GNOME.

%description gnome-mime-info -l pl
Funkcje MIME dla GNOME.

%package input-mikmod
Summary:	XMMS - Input plugin to play MODs
Summary(es):	Login de entrada para que XMMS alcance MODs (.MOD,.XM,.S3M, etc)
Summary(ja):	XMMS - MODs¤òºÆÀ¸¤¹¤ë¤¿¤á¤ÎÆþÎÏ¥×¥é¥°¥¤¥ó
Summary(pl):	XMMS - wtyczka do odtwarzania MODów
Summary(pt_BR):	Plugin de entrada para o XMMS tocar MODs (.MOD,.XM,.S3M, etc)
Summary(zh_CN):	XMMS - ²¥·Å M0Ds ÎÄ¼þµÄÊäÈë²å¼þ
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

%description input-mikmod -l es
Login de entrada para que XMMS alcance MODs (.MOD,.XM,.S3M, etc).

%description input-mikmod -l pl
Wtyczka dla XMMS-a do odtwarzania MODów (.MOD,.XM,.S3M, etc). B±d¼
¶wiadom, ¿e ta wtyczka jest bardzo s³aba (byæ mo¿e z powodu jako¶ci
libmikmod) - nie potrafi odtworzyæ poprawnie wielu modu³ów. Zainstaluj
lepiej xmms-input-modplug.

%description input-mikmod -l pt_BR
Plugin de entrada para o XMMS tocar MODs (.MOD,.XM,.S3M, etc).

%package input-tonegen
Summary:	XMMS - Input plugin to generate sound of given frequency
Summary(pl):	XMMS - wtyczka generuj±ca d¼wiêk o zadanej czêstotliwo¶ci
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xmms-tonegen

%description input-tonegen
Input plugin for XMMS to generate sound of given frequency.

%description input-tonegen -l pl
Wtyczka dla XMMS-a generuj±ca d¼wiêk o zadanej czêstotliwo¶ci.

%package input-vorbis
Summary:	XMMS - Ogg Vorbis input plugin
Summary(ja):	XMMS - Oggs¤òºÆÀ¸¤¹¤ë¤¿¤á¤ÎÆþÎÏ¥×¥é¥°¥¤¥ó
Summary(pl):	XMMS - wtyczka do odtwarzania plików Ogg Vorbis
Summary(zh_CN):	XMMS - ²¥·Å 0GGs ±àÂëÎÄ¼þµÄÊäÈë²å¼þ
Group:		X11/Applications/Sound
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description input-vorbis
Ogg Vorbis input plugin for XMMS.

%description input-vorbis -l pl
Wtyczka do odtwarzania plików w formacie Ogg Vorbis.

%package input-cdaudio
Summary:	XMMS - cdaudio input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plyt CD-audio
Group:		X11/Applications/Sound
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description input-cdaudio
CD audio input plugin for XMMS.

%description input-cdaudio -l pl
Wtyczka do odtwarzania p³yt CD-audio.

%package input-mpg123
Summary:	XMMS - mpg123 input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plikow MP3
Group:		X11/Applications/Sound
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description input-mpg123
mpg123 input plugin for XMMS.

%description input-mpg123 -l pl
Wtyczka dla XMMS-a do obs³ugi mpg123.

%package input-wav
Summary:	XMMS - WAV input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plików WAV
Group:		X11/Applications/Sound
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description input-wav
WAV input plugin for XMMS.

%description input-wav -l pl
Wtyczka dla XMMS-a do obs³ugi plików WAV.

%package output-OSS
Summary:	XMMS - OSS output plugin
Summary(pl):	XMMS - plugin obs³ugi sterowników OSS
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xmms-output-plugin

%description output-OSS
OSS output plugin for XMMS.

%description output-OSS -l pl
Obs³uga sterowników OSS dla XMMS-a.

%package output-ALSA
Summary:	XMMS - ALSA output plugin
Summary(pl):	XMMS - plugin obs³ugi sterowników Alsa
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xmms-output-plugin
Obsoletes:	xmms-output-aalsa
Obsoletes:	xmms-output-alsa

%description output-ALSA
ALSA output plugin for XMMS.

%description output-ALSA -l pl
Obs³uga sterowników ALSA dla XMMS-a.

%package output-esd
Summary:	XMMS - Output plugin for use with the esound package
Summary(es):	Plugin de salida para XMMS para uso con el paquete eSound
Summary(ja):	XMMS - esound¤òÍøÍÑ¤¹¤ë½ÐÎÏ¥×¥é¥°¥¤¥ó
Summary(pl):	XMMS - wtyczka umo¿liwiaj±ca korzystanie z esound
Summary(pt_BR):	Plugin de saida para o XMMS para uso com o pacote eSound
Summary(zh_CN):	XMMS - Óë esound Èí¼þ°üÒ»ÆðÊ¹ÓÃµÄÊä³ö²å¼þ
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	esound >= 0.2.8
Provides:	xmms-output-plugin
Obsoletes:	xmms-esd

%description output-esd
Output plugin for XMMS for use with the esound package.

%description output-esd -l es
Plugin de salida para XMMS para uso con el paquete eSound.

%description output-esd -l pl
Wtyczka dla XMMS-a umo¿liwiaj±ca wykorzystanie esound przy odtwarzaniu
d¼wiêków.

%description output-esd -l pt_BR
Plugin de saída para o XMMS trabalhar com o esd.

%package output-disk
Summary:	XMMS - disk-writer output plugin
Summary(pl):	XMMS - wtyczka do zapisywania danych na dysk
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xmms-output-plugin

%description output-disk
disk-wirter output plugin for XMMS.

%description output-disk -l pl
Wtyczka dla XMMS-a zapisuj±ca dane wyj¶ciowe na dysk.

%package visualization-GL
Summary:	XMMS - Visualization plugins that use the OenGL library
Summary(ja):	XMMS - OpenGL¤òÍøÍÑ¤·¤¿¥°¥é¥Õ¥£¥«¥ë¤Ê»ë³Ð²½¥×¥é¥°¥¤¥ó
Summary(pl):	XMMS - wtyczki do wizualizacji z u¿yciem OpenGL
Summary(ru):	XMMS - ÐÏÄËÌÀÞÁÅÍÙÅ ÍÏÄÕÌÉ ×ÉÚÕÁÌÉÚÁÃÉÉ, ÉÓÐÏÌØÚÕÀÝÉÅ ÂÉÂÌÉÏÔÅËÕ OenGL
Summary(uk):	XMMS - Ð¦Ä'¤ÄÎÕ×ÁÎ¦ ÍÏÄÕÌ¦ ×¦ÚÕÁÌ¦ÚÁÃ¦§, ÑË¦ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ Â¦ÂÌ¦ÏÔÅËÕ OpenGL
Summary(zh_CN):	XMMS - ¿ÉÊÓ»¯²å¼þ
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	OpenGL
Obsoletes:	xmms-mesa

%description visualization-GL
XMMS - Visualization plugins that use the OpenGL library.

%description visualization-GL -l pl
Wtyczki graficzne wykorzystuj±ce bibliotekê OpenGL.

%description visualization-GL -l ru
XMMS - ÐÏÄËÌÀÞÁÅÍÙÅ ÍÏÄÕÌÉ ×ÉÚÕÁÌÉÚÁÃÉÉ, ÉÓÐÏÌØÚÕÀÝÉÅ ÂÉÂÌÉÏÔÅËÕ
OpenGL.

%description visualization-GL -l uk
XMMS - Ð¦Ä'¤ÄÎÕ×ÁÎ¦ ÍÏÄÕÌ¦ ×¦ÚÕÁÌ¦ÚÁÃ¦§, ÑË¦ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ Â¦ÂÌ¦ÏÔÅËÕ
OpenGL.

%prep
%setup -q -a1 -a5
%patch0 -p1
%patch1 -p1
#patch2 -p1
%patch3 -p1
%patch4 -p1

cp -f %{SOURCE2} .

mv -f po/{no,nb}.po
%{__perl} -pi -e 's/ no / nb /' po/LINGUAS
# allow (re)building, incl. nb.gmo
rm -f po/stamp-po

%if %{with gtk2}
%patch2 -p1

rm -f po/*.gmo
for F in po/*.po
do
	ENC=`cat $F | grep "charset=" | cut -d= -f2 | cut -d'\' -f1`
	case $ENC in
		iso-8859-1|ISO-8859-1) E=ISO8859-1 ; ;;
		iso-8859-2|ISO-8859-2) E=ISO8859-2 ; ;;
		iso-8859-3) E=ISO8859-3 ; ;;
		iso-8859-5) E=ISO8859-5 ; ;;
		ISO-8859-7) E=ISO8859-7 ; ;;
		ISO-8859-9) E=ISO8859-9 ; ;;
		ISO-8859-11) E=ISO8859-11 ; ;;
		iso-8859-13) E=ISO8859-13 ; ;;
		windows-1251) E=WINDOWS-1251 ; ;;
		utf-8|UTF-8) E="" ; ;;
		EUC-JP) E="" ; ;;
		euc-kr) E="" ; ;;
		koi8-r) E=KOI8-R ; ;;
		koi8-u) E=KOI8-U ; ;;
		tcvn-5712) E=TCVN-5712 ; ;;
		gb2312) E="" ; ;;
		big5) E="" ; ;;
		*) echo "Unknown encoding: $ENC"; exit 1
	esac
	if [ "$E" != "" ]; then
		mv $F tmp.po
		cat tmp.po | egrep -v '^#\.' | sed -e "s/\(charset=\)$ENC/\1UTF-8/" | \
			iconv -f $E -t UTF-8 -o $F
	fi
done
%endif

install -d m4
# get only XMMS_FUNC_POSIX
head -n39 libxmms/acinclude.m4 > m4/xmms-func-posix.m4

%build
# kill copies of many macros
rm -f acinclude.m4
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

cd libxmms
# kill old libtool.m4
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
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/mime-info/xmms.keys
install %{SOURCE7} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
echo "Remember to install appropriate xmms-input-* packages for files you want"
echo "to play."

[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README mp3license FAQ
%attr(755,root,root) %{_bindir}/xmms
%attr(755,root,root) %{_libdir}/xmms/Effect/*
%attr(755,root,root) %{_libdir}/xmms/General/*
%attr(755,root,root) %{_libdir}/xmms/Visualization/libbscope*
%attr(755,root,root) %{_libdir}/xmms/Visualization/libsanalyzer*
%dir %{_datadir}/xmms
%dir %{_datadir}/xmms/Skins
%dir %{_libdir}/xmms/Effect
%dir %{_libdir}/xmms/General
%dir %{_libdir}/xmms/Output
%dir %{_libdir}/xmms/Visualization
%{_datadir}/xmms/*gif
%{_datadir}/xmms/x*xpm
%{_desktopdir}/xmms.desktop
%{_mandir}/*/xmms*
%{_pixmapsdir}/xmms*

%files wm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wmxmms
%{_datadir}/xmms/wmxmms*xpm
%{_desktopdir}/wmxmms.desktop
%{_mandir}/*/wmxmms*

%files skins
%defattr(644,root,root,755)
%{_datadir}/xmms/Skins/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmms.so.*.*
%dir %{_libdir}/xmms
%dir %{_libdir}/xmms/Input

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmms-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files gnome-mime-info
%defattr(644,root,root,755)
%{_datadir}/mime-info/xmms.keys

%files input-mikmod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libmikmod*

%files input-tonegen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libtonegen*

%files input-cdaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libcdaudio*

%files input-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libvorbis*

%files input-mpg123
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libmpg123*

%files input-wav
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/libwav*

%files output-OSS
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libOSS*

%files output-ALSA
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libALSA*

%files output-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libesdout*

%files output-disk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libdisk_writer*

%files visualization-GL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Visualization/libogl_spectrum*
