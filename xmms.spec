#
# Conditional build:
%bcond_with	gtk2	# experimental GTK+2 port (and probably broken/incomplete)
#			  (deprecated - many plugins won't work, use beep instead)
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Summary(es):	Editor de sonido con GUI semejante al de WinAmp
Summary(ja):	XMMS - X Window System얍ㅗ튼븜ㅉㅻ�裨瑜젖醒표％´婁議샵沈�
Summary(ko):	Unix 베이스 시스템을 위한 winamp 모양의 음악 연주기
Summary(pl):	Odtwarzacz d펧i�ku z interfejsem WinAmpa
Summary(pt_BR):	Tocador de som com GUI semelhante ao do WinAmp
Summary(ru):	眺鉤할墓죤턍� 鼓粕漑 � WinAmp GUI
Summary(uk):	眺逑怒陸� 鼓緡漑 � WinAmp GUI
Summary(zh_CN):	XMMS - X 똥뜩첵竟꺄렴포
Name:		xmms
Version:	1.2.10
Release:	2
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
BuildRequires:	zlib-devel
%if %{with gtk2}
BuildRequires:	gtk+2-devel >= 2.2.0
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
GUI, it can use WinAmp skins, and play mp3s, mods, s3ms, and other
formats. It now has support for input, output, and general plugins,
and has also been GPL'd.

%description -l es
Editor de sonido con GUI semejante al de WinAmp.

%description -l pl
XMMS jest odtwarzaczem d펧i�ku napisanym od zera. Jako 풽 wykorzystuje
interfejs WinAmpa, mo풽 r�wnie� u퓓wa� jego 'sk�rek'. Odtwarza pliki w
formatach mp3, mod, s3m i wielu innych. Teraz obs퀅guje tak풽 pluginy
do wej턢ia, wyj턢ia oraz og�lne; zosta� tak풽 zGPL-izowany.

%description -l pt_BR
XMMS � um sound player escrito a partir do zero. Como ele utiliza a
interface do WinAmp, ele pode utilizar "skins" do WinAmp, e tocar
arquivos .mp3, .mod, .s3m, e outros formatos. Agora ele suporta
plugins de entrada, sa�da e outros plugins de uso geral, e sua licen�a
se tornou GPL.

%description -l ru
XMMS - 妗鉤할墓죤턍� 鼓粕漑 � 할좟�使沓�� �塊텀팍柬鳩, 适饉苽适잖��
�塊텀팍柬 WinAmp. 停 賈領� �唐驅媒窘죤� "沓�槐" WinAmp, 妗鉤할墓죤�
mp3, mod, s3m � 켠朗�� 팥魯죤�. 闡斤濃 鷗 饉컴텀禮陸텃 饉켄缺些터芼
賈켭俓 켈� 苟怒쫏頓� 利謳�, 吏凜컨, 苟墳하 适剝줏턱�� � 慄泊죈�憫촁�.

%description -l uk
XMMS - 妗逑怒陸� 鼓緡漑 � 할좟╄炚� ┧旽盧탱遝�, 粉 适프켭� ┧旽盧탱�
WinAmp. 憚� 賈領 慄蓋虜戇窘兩죤�" 沓┧�" WinAmp, 妗逑怒陸燉 mp3, mod,
s3m 讀 ┧魃 팥魯죤�. 闡斤� 屢� 揆켬虜鼓� 揆�'ㅔ壞陸過 賈켭迲 苟碌쫀�
利謳�, 慄凜켭, 賈켭迲 憫프景卦하 妗�剝줏턱罫 讀 屢泊죈┾좍├.

%package wm
Summary:	XMMS applet for WindowMaker
Summary(pl):	Aplet XMMS dla WindowMakera
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}

%description wm
XMMS applet for WindowMaker.

%description wm -l pl
Aplet XMMS dla WindowMakera.

%package skins
Summary:	XMMS - Skins
Summary(pl):	XMMS - Sk�rki
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}
Requires:	unzip

%description skins
Additional skins for XMMS.

%description skins -l pl
Dodatkowe 'sk�rki' dla XMMS-a.

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
Summary(es):	Bibliotecas y archivos de inclusi�n, necesarios para compilar plugins de XMMS
Summary(ja):	XMMS - 낙환錮Φⅰⅳλ
Summary(ko):	XMMS - 라이브러리와 헤더 파일들
Summary(pl):	XMMS - biblioteki i pliki nag농wkowe
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o necess�rios para se compilar plugins do XMMS
Summary(uk):	.h-팁奸� 켈� XMMS
Summary(ru):	.h-팁奸� 켈� XMMS
Summary(zh_CN):	XMMS - 역랙욋
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}
# broken/incomplete gtk2 patch? libxmms is still linked with old GTK+
Requires:	gtk+-devel

%description devel
Libraries and header files required for compiling XMMS plugins.

%description devel -l es
Bibliotecas y archivos de inclusi�n, necesarios para compilar plugins
de XMMS.

%description devel -l pl
Biblioteki i pliki nag농wkowe wymagane do budowania wtyczek dla
XMMS-a.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o necess�rios para se compilar
plugins do XMMS.

%description devel -l ru
.h-팁奸� 켈� 饉戇碌턱�� 饉켄缺些터謨 賈켭謙� 켈� XMMS.

%description devel -l uk
.h-팁奸� 켈� 饉쫬켓慄 揆�'ㅔ壞陸炚� 賈켭迲� 켈� XMMS.

%package static
Summary:	XMMS - static libraries
Summary(es):	Static libraries for XMMS development
Summary(pl):	XMMS - biblioteki statyczne
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com XMMS
Summary(ru):	慙죤�使沓�� 쪼쫄�鞫탸� 켈� XMMS
Summary(uk):	慙죤�奢� 짝쫄┩旽漑 켈� XMMS
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static libraries required for compiling XMMS plugins.

%description static -l es
Static libraries for XMMS development.

%description static -l pl
Biblioteki statyczne XMMS-a.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com o XMMS.

%description static -l ru
慙죤�使沓�� 쪼쫄�鞫탸� 켈� 饉戇碌턱�� 饉켄缺些터謨 賈켭謙� 켈� XMMS.

%description static -l uk
慙죤�奢� 짝쫄┩旽漑 켈� 饉쫬켓慄 揆�'ㅔ壞陸炚� 賈켭迲� 켈� XMMS.

%package gnome-mime-info
Summary:	MIME functions for GNOME
Summary(pl):	Funkcje MIME dla GNOME
Group:		X11/Applications
Requires:	gnome-mime-data

%description gnome-mime-info
MIME functions for GNOME.

%description gnome-mime-info -l pl
Funkcje MIME dla GNOME.

%package input-mikmod
Summary:	XMMS - Input plugin to play MODs
Summary(es):	Login de entrada para que XMMS alcance MODs (.MOD,.XM,.S3M, etc)
Summary(ja):	XMMS - MODsㆂ뵈으ㅉㅻㅏㅱㅞ퐁卦ΨιⅠⅳτ
Summary(pl):	XMMS - wtyczka do odtwarzania MOD�w
Summary(pt_BR):	Plugin de entrada para o XMMS tocar MODs (.MOD,.XM,.S3M, etc)
Summary(zh_CN):	XMMS - 꺄렴 M0Ds 匡숭돨渴흙꿨숭
Group:		X11/Applications/Sound
Requires:	%{name}-libs = %{epoch}:%{version}
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
Wtyczka dla XMMS-a do odtwarzania MOD�w (.MOD,.XM,.S3M, etc). B켨�
턻iadom, 풽 ta wtyczka jest bardzo s쿪ba (by� mo풽 z powodu jako턢i
libmikmod) - nie potrafi odtworzy� poprawnie wielu modu농w. Zainstaluj
lepiej xmms-input-modplug.

%description input-mikmod -l pt_BR
Plugin de entrada para o XMMS tocar MODs (.MOD,.XM,.S3M, etc).

%package input-tonegen
Summary:	XMMS - Input plugin to generate sound of given frequency
Summary(pl):	XMMS - wtyczka generuj켧a d펧i�k o zadanej cz�stotliwo턢i
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}
Obsoletes:	xmms-tonegen

%description input-tonegen
Input plugin for XMMS to generate sound of given frequency.

%description input-tonegen -l pl
Wtyczka dla XMMS-a generuj켧a d펧i�k o zadanej cz�stotliwo턢i.

%package input-vorbis
Summary:	XMMS - OGG Vorbis input plugin
Summary(ja):	XMMS - OGGsㆂ뵈으ㅉㅻㅏㅱㅞ퐁卦ΨιⅠⅳτ
Summary(pl):	XMMS - wtyczka do odtwarzania plik�w OGG Vorbis
Summary(zh_CN):	XMMS - 꺄렴 0GGs 긍쯤匡숭돨渴흙꿨숭
Group:		X11/Applications/Sound
Requires:	%{name}-libs >= %{epoch}:%{version}

%description input-vorbis
OGG Vorbis input plugin for XMMS.

%description input-vorbis -l pl
Wtyczka do odtwarzania plik�w w formacie OGG Vorbis.

%package input-cdaudio
Summary:	XMMS - cdaudio input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plyt CD-audio
Group:		X11/Applications/Sound
Requires:	%{name}-libs >= %{epoch}:%{version}

%description input-cdaudio
CD audio input plugin for XMMS.

%description input-cdaudio -l pl
Wtyczka do odtwarzania p퀉t CD-audio.

%package input-mpg123
Summary:	XMMS - mpg123 input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plikow mp3
Group:		X11/Applications/Sound
Requires:	%{name}-libs >= %{epoch}:%{version}

%description input-mpg123
mpg123 input plugin for XMMS.

%description input-mpg123 -l pl
Wtyczka dla XMMS-a do obs퀅gi mpg123.

%package input-wav
Summary:	XMMS - wav input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plikow wav
Group:		X11/Applications/Sound
Requires:	%{name}-libs >= %{epoch}:%{version}

%description input-wav
wav input plugin for XMMS.

%description input-wav -l pl
Wtyczka dla XMMS-a do obs퀅gi plik�w wav.

%package output-OSS
Summary:	XMMS - OSS output plugin
Summary(pl):	XMMS - plugin obs퀅gi sterownik�w OSS
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}
Provides:	xmms-output-plugin

%description output-OSS
OSS output plugin for XMMS.

%description output-OSS -l pl
Obs퀅ga sterownik�w OSS dla XMMS-a.

%package output-ALSA
Summary:	XMMS - ALSA output plugin
Summary(pl):	XMMS - plugin obs퀅gi sterownik�w Alsa
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}
Provides:	xmms-output-plugin
Obsoletes:	xmms-output-alsa

%description output-ALSA
ALSA output plugin for XMMS.

%description output-ALSA -l pl
Obs퀅ga sterownik�w ALSA dla XMMS-a.

%package output-esd
Summary:	XMMS - Output plugin for use with the esound package
Summary(es):	Plugin de salida para XMMS para uso con el paquete eSound
Summary(ja):	XMMS - esoundㆂ貢錮ㅉㅻ싻卦ΨιⅠⅳτ
Summary(pl):	XMMS - wtyczka umo퓄iwiaj켧a korzystanie z esound
Summary(pt_BR):	Plugin de saida para o XMMS para uso com o pacote eSound
Summary(zh_CN):	XMMS - 宅 esound 흡숭관寧폅賈痰돨渴놔꿨숭
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}
Requires:	esound >= 0.2.8
Provides:	xmms-output-plugin
Obsoletes:	xmms-esd

%description output-esd
Output plugin for XMMS for use with the esound package.

%description output-esd -l es
Plugin de salida para XMMS para uso con el paquete eSound.

%description output-esd -l pl
Wtyczka dla XMMS-a umo퓄iwiaj켧a wykorzystanie esound przy odtwarzaniu
d펧i�k�w.

%description output-esd -l pt_BR
Plugin de sa�da para o XMMS trabalhar com o esd.

%package output-disk
Summary:	XMMS - disk-writer output plugin
Summary(pl):	XMMS - wtyczka do zapisywania danych na dysk
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}
Provides:	xmms-output-plugin

%description output-disk
disk-wirter output plugin for XMMS.

%description output-disk -l pl
Wtyczka dla XMMS-a zapisuj켧a dane wyj턢iowe na dysk.

%package visualization-GL
Summary:	XMMS - Visualization plugins that use the OenGL library
Summary(ja):	XMMS - OpenGLㆂ貢錮ㅇㅏⅠιΦⅲ�ゥ琉軻蹂勻쉈婁耀갈ㄵ�
Summary(pl):	XMMS - wtyczki do wizualizacji z u퓓ciem OpenGL
Summary(ru):	XMMS - 饉켄缺些터芼 賈켭俓 慄泊죈�憫촁�, �唐驅媒藍憤� 쪼쫄�鞫탸� OenGL
Summary(uk):	XMMS - 揆�'ㅔ壞陸過 賈켭迲 屢泊죈┾좍├, 麒� 慄蓋虜戇窘藍潼 짝쫄┩旽坑 OpenGL
Summary(zh_CN):	XMMS - 옵柬뺏꿨숭
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}
Requires:	OpenGL
Obsoletes:	xmms-mesa

%description visualization-GL
XMMS - Visualization plugins that use the OpenGL library.

%description visualization-GL -l pl
Wtyczki graficzne wykorzystuj켧e bibliotek� OpenGL.

%description visualization-GL -l ru
XMMS - 饉켄缺些터芼 賈켭俓 慄泊죈�憫촁�, �唐驅媒藍憤� 쪼쫄�鞫탸�
OpenGL.

%description visualization-GL -l uk
XMMS - 揆�'ㅔ壞陸過 賈켭迲 屢泊죈┾좍├, 麒� 慄蓋虜戇窘藍潼 짝쫄┩旽坑
OpenGL.

%prep
%setup -q -a1 -a5
%patch0 -p1
%patch1 -p1

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
echo "Remember to install appropriate xmms-input-* packages for files you want"
echo "to play."

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
%attr(755,root,root) %{_bindir}/xmms-config
%attr(755,root,root) %{_libdir}/libxmms.so.*.*
%dir %{_libdir}/xmms
%dir %{_libdir}/xmms/Input

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a

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
