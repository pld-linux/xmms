#
# Conditional build:
# gnome		- build gnome subpackage
# gtk2		- with gtk+2 (and without gnome :( )
#
%bcond_without gnome
%bcond_with gtk2

%define	pre	pre1
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Summary(es):	Editor de sonido con GUI semejante al de WinAmp
Summary(ja):	XMMS - X Window System���ư���ޥ����ǥ����ץ졼�䡼
Summary(ko):	Unix ���̽� �ý����� ���� winamp ����� ���� ���ֱ�
Summary(pl):	Odtwarzacz d�wi�ku z interfejsem WinAmpa
Summary(pt_BR):	Tocador de som com GUI semelhante ao do WinAmp
Summary(ru):	������������� ������ � WinAmp GUI
Summary(uk):	��������� ������ � WinAmp GUI
Summary(zh_CN):	XMMS - X �˶�ý�岥����
Name:		xmms
Version:	1.2.8
Release:	0.%{pre}.1
Epoch:		2
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://www.xmms.org/files/1.2.x/%{name}-%{version}-%{pre}.tar.bz2
# Source0-md5:	3959cc628f1434d6a444742d42987114
Source1:	%{name}-icons.tar.gz
# Source1-md5:	14fc5a0bb3679daf1c3900e3a30674e9
Source2:	mp3license
Source3:	%{name}.desktop
Source4:	wm%{name}.desktop
Source5:	%{name}-skins.tar.bz2
# Source5-md5:	39d6de4bf2c37c17b868df3596871c59
Source6:	%{name}-gnome-mime-info
Source7:	%{name}.png
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-m4.patch
Patch2:		%{name}-libogg_libvorbis_1.0_ac_fix.patch
Patch3:		%{name}-warn_about_unplayables.patch
Patch4:		%{name}-configure.patch
#Patch5:		%{name}-patch.czech.patch
#Patch6:		%{name}-ass-20020303.patch
Patch7:		%{name}-gtk2.patch
# Original location:
#Patch8		http://members.jcom.home.ne.jp/jacobi/linux/etc/xmms-1.2.7-mmx.patch.gz
#Patch8:		%{name}-1.2.7-mmx.patch
URL:		http://www.xmms.org/
BuildRequires:	OpenGL-devel
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
%if %{without gtk2}
%{?with_gnome:BuildRequires:	gnome-core-devel}
%{?with_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	gtk+-devel >= 1.2.2
Requires:	glib >= 1.2.2
Requires:	gtk+ >= 1.2.2
%endif
Requires:	xmms-output-plugin
Obsoletes:	x11amp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_sysconfdir	/etc/X11/GNOME
%if %{without gtk2}
%{?with_gnome:%define		_appletsdir	%(gnome-config --datadir)/applets}
%endif

%description
XMMS is a sound player written from scratch. Since it uses the WinAmp
GUI, it can use WinAmp skins, and play mp3s, mods, s3ms, and other
formats. It now has support for input, output, and general plugins,
and has also been GPL'd.

%description -l es
Editor de sonido con GUI semejante al de WinAmp.

%description -l pl
XMMS jest odtwarzaczem d�wi�ku napisanym od zera. Jako �e wykorzystuje
interfejs WinAmpa, mo�e r�wnie� u�ywa� jego 'sk�rek'. Odtwarza pliki w
formatach mp3, mod, s3m i wielu innych. Teraz obs�uguje tak�e pluginy
do wej�cia, wyj�cia oraz og�lne; zosta� tak�e zGPL-izowany.

%description -l pt_BR
XMMS � um sound player escrito a partir do zero. Como ele utiliza a
interface do WinAmp, ele pode utilizar "skins" do WinAmp, e tocar
arquivos .mp3, .mod, .s3m, e outros formatos. Agora ele suporta
plugins de entrada, sa�da e outros plugins de uso geral, e sua licen�a
se tornou GPL.

%description -l ru
XMMS - ������������� ������ � ����������� �����������, ������������
��������� WinAmp. �� ����� ������������ "�����" WinAmp, �����������
mp3, mod, s3m � ������ �������. ������ �� ������������ ������������
������ ��� ��������� �����, ������, ������ ���������� � ������������.

%description -l uk
XMMS - ��������� ������ � ���Ʀ���� �����������, �� �����դ ���������
WinAmp. ��� ���� ���������������" �˦��" WinAmp, ���������� mp3, mod,
s3m �� ��ۦ �������. ����� צ� Ц�����դ Ц�'������Φ ����̦ �������
�����, ������, ����̦ ���������� ����������� �� צ���̦��æ�.

%package wm
Summary:	XMMS applet for WindowMaker
Summary(pl):	Aplet XMMS dla WindowMakera
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}

%description wm
XMMS applet for WindowMaker.

%description wm -l pl
Aplet XMMS dla WindowMakera.

%package gnome
Summary:	XMMS - applet for controlling XMMS from the GNOME panel
Summary(ja):	XMMS - GNOME�ѥͥ��Ѥ�XMMS���ץ�å�
Summary(pl):	XMMS - aplet umo�liwiaj�cy sterowanie XMMS-em z panelu GNOME
Summary(ru):	������ ������ GNOME ��� xmms
Summary(uk):	����� ����̦ GNOME ��� xmms
Summary(zh_CN):	XMMS - GNOME ƽ̨�ϵ� XMMS ���Ƴ���
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}
Requires:	gnome-libs >= 1.0.0

%description gnome
GNOME applet for controlling XMMS from the GNOME panel.

%description gnome -l pl
Aplet GNOME umo�liwiaj�cy sterowanie XMMS-em z panelu GNOME.

%description gnome -l ru
����� xmms-gnome �������� ������ ������ GNOME, ������ �����������
��������� xmms.

%description gnome -l uk
����� xmms-gnome ͦ����� ����� ����̦ GNOME, ���� ��� �����צ���
��������� xmms.

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
Summary(ja):	XMMS - ��ȯ�ѥե�����
Summary(ko):	XMMS - ���̺귯���� ��� ���ϵ�
Summary(pl):	XMMS - biblioteki i pliki nag��wkowe
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o necess�rios para se compilar plugins do XMMS
Summary(uk):	.h-����� ��� xmms
Summary(ru):	.h-����� ��� xmms
Summary(zh_CN):	XMMS - ������
Group:		X11/Development/Libraries
%if %{without gtk2}
Requires:	gtk+-devel
%endif
Requires:	%{name}-libs = %{epoch}:%{version}

%description devel
Libraries and header files required for compiling XMMS plugins.

%description devel -l es
Bibliotecas y archivos de inclusi�n, necesarios para compilar plugins
de XMMS.

%description devel -l pl
Biblioteki i pliki nag��wkowe wymagane do budowania wtyczek dla
XMMS-a.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o necess�rios para se compilar
plugins do XMMS.

%description devel -l ru
.h-����� ��� ���������� ������������ ������� ��� xmms.

%description devel -l uk
.h-����� ��� �������� Ц�'��������� ����̦� ��� xmms.

%package static
Summary:	XMMS - static libraries
Summary(es):	Static libraries for XMMS development
Summary(pl):	XMMS - biblioteki statyczne
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com XMMS
Summary(ru):	����������� ���������� ��� xmms
Summary(uk):	������Φ ¦�̦����� ��� xmms
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
����������� ���������� ��� ���������� ������������ ������� ��� xmms.

%description static -l uk
������Φ ¦�̦����� ��� �������� Ц�'��������� ����̦� ��� xmms.

%package input-mikmod
Summary:	XMMS - Input plugin to play MODs
Summary(es):	Login de entrada para que XMMS alcance MODs (.MOD,.XM,.S3M, etc)
Summary(ja):	XMMS - MODs��������뤿������ϥץ饰����
Summary(pl):	XMMS - wtyczka do odtwarzania MOD�w
Summary(pt_BR):	Plugin de entrada para o XMMS tocar MODs (.MOD,.XM,.S3M, etc)
Summary(zh_CN):	XMMS - ���� M0Ds �ļ���������
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}
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
Wtyczka dla XMMS-a do odtwarzania MOD�w (.MOD,.XM,.S3M, etc). B�d�
�wiadom, �e ta wtyczka jest bardzo s�aba (by� mo�e z powodu jako�ci
libmikmod) - nie potrafi odtworzy� poprawnie wielu modu��w. Zainstaluj
lepiej xmms-input-modplug.

%description input-mikmod -l pt_BR
Plugin de entrada para o XMMS tocar MODs (.MOD,.XM,.S3M, etc).

%package input-tonegen
Summary:	XMMS - Input plugin to generate sound of given frequency
Summary(pl):	XMMS - wtyczka generuj�ca d�wi�k o zadanej cz�stotliwo�ci
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}
Obsoletes:	xmms-tonegen

%description input-tonegen
Input plugin for XMMS to generate sound of given frequency.

%description input-tonegen -l pl
Wtyczka dla XMMS-a generuj�ca d�wi�k o zadanej cz�stotliwo�ci.

%package input-vorbis
Summary:	XMMS - OGG Vorbis input plugin
Summary(ja):	XMMS - OGGs��������뤿������ϥץ饰����
Summary(pl):	XMMS - wtyczka do odtwarzania plik�w OGG Vorbis
Summary(zh_CN):	XMMS - ���� 0GGs �����ļ���������
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}

%description input-vorbis
OGG Vorbis input plugin for XMMS.

%description input-vorbis -l pl
Wtyczka do odtwarzania plik�w w formacie OGG Vorbis.

%package input-cdaudio
Summary:	XMMS - cdaudio input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plyt CD-audio
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}

%description input-cdaudio
CD audio input plugin for XMMS.

%description input-cdaudio -l pl
Wtyczka do odtwarzania p�yt CD-audio.

%package input-idcin
Summary:	XMMS - idcin input plugin
Summary(pl):	XMMS - wtyczka do obs�ugi formatu idcin
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}

%description input-idcin
idcin input plugin for XMMS.

%description input-idcin -l pl
Wtyczka dla XMMS-a do obs�ugi formatu idcin.

%package input-mpg123
Summary:	XMMS - mpg123 input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plikow mp3
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}

%description input-mpg123
mpg123 input plugin for XMMS.

%description input-mpg123 -l pl
Wtyczka dla XMMS-a do obs�ugi mpg123.

%package input-wav
Summary:	XMMS - wav input plugin
Summary(pl):	XMMS - wtyczka do odtwarzania plikow wav
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}

%description input-wav
wav input plugin for XMMS.

%description input-wav -l pl
Wtyczka dla XMMS-a do obs�ugi plik�w wav.

%package output-OSS
Summary:	XMMS - OSS output plugin
Summary(pl):	XMMS - plugin obs�ugi sterownik�w OSS
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}
Provides:	xmms-output-plugin

%description output-OSS
OSS output plugin for XMMS.

%description output-OSS -l pl
Obs�uga sterownik�w OSS dla XMMS-a.

%package output-esd
Summary:	XMMS - Output plugin for use with the esound package
Summary(es):	Plugin de salida para XMMS para uso con el paquete eSound
Summary(ja):	XMMS - esound�����Ѥ�����ϥץ饰����
Summary(pl):	XMMS - wtyczka umo�liwiaj�ca korzystanie z esound
Summary(pt_BR):	Plugin de saida para o XMMS para uso com o pacote eSound
Summary(zh_CN):	XMMS - �� esound �����һ��ʹ�õ�������
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}
Requires:	esound >= 0.2.8
Obsoletes:	xmms-esd
Provides:	xmms-output-plugin

%description output-esd
Output plugin for XMMS for use with the esound package.

%description output-esd -l es
Plugin de salida para XMMS para uso con el paquete eSound.

%description output-esd -l pl
Wtyczka dla XMMS-a umo�liwiaj�ca wykorzystanie esound przy odtwarzaniu
d�wi�k�w.

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
Wtyczka dla XMMS-a zapisuj�ca dane wyj�ciowe na dysk.

%package visualization-GL
Summary:	XMMS - Visualization plugins that use the OenGL library
Summary(ja):	XMMS - OpenGL�����Ѥ�������ե�����ʻ�в��ץ饰����
Summary(pl):	XMMS - wtyczki do wizualizacji z u�yciem OpenGL
Summary(ru):	XMMS - ������������ ������ ������������, ������������ ���������� OenGL
Summary(uk):	XMMS - Ц�'������Φ ����̦ צ���̦��æ�, �˦ �������������� ¦�̦����� OpenGL
Summary(zh_CN):	XMMS - ���ӻ����
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}
Requires:	OpenGL
Obsoletes:	xmms-mesa

%description visualization-GL
XMMS - Visualization plugins that use the OpenGL library.

%description visualization-GL -l pl
Wtyczki graficzne wykorzystuj�ce bibliotek� OpenGL.

%description visualization-GL -l ru
XMMS - ������������ ������ ������������, ������������ ����������
OpenGL.

%description visualization-GL -l uk
XMMS - Ц�'������Φ ����̦ צ���̦��æ�, �˦ �������������� ¦�̦�����
OpenGL.

%prep
%setup -q -n %{name}-%{version}-%{pre} -a1 -a5
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
##%patch5 -p1
#%patch6 -p1

cp -f %{SOURCE2} .

%if %{with gtk2}
%patch7 -p1

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
	cat tmp.po | egrep -v '^#\.' | iconv -f $E -t UTF-8 -o $F
    fi
done
%endif
##%patch8 -p1

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

cd libxmms
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd ..

GNOMEOPT=""
%if %{without gtk2}
%{?with_gnome:GNOMEOPT=--with-gnome}
%endif

%configure \
	--disable-vorbistest $GNOMEOPT \
%ifarch %{ix86}
	--enable-simd
%endif

test -z $SED && SED=sed
export SED

%{__make} AS="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/{mime-info,xmms/Skins}

test -z $SED && SED=sed; export SED

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/mime-info/xmms.keys
install icons/*    $RPM_BUILD_ROOT%{_datadir}/xmms
install Skins/*    $RPM_BUILD_ROOT%{_datadir}/xmms/Skins
install %{SOURCE7} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

echo "Remember to install appropriate xmms-input-* packages for files you want"
echo "to play."

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README mp3license FAQ
%{_applnkdir}/Multimedia/xmms.desktop
%attr(755,root,root) %{_bindir}/xmms
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
%dir %{_datadir}/xmms/Skins
%{_datadir}/xmms/*gif
%{_datadir}/xmms/x*xpm
%{_mandir}/*/xmms*
%{_pixmapsdir}/xmms*

%files wm
%defattr(644,root,root,755)
%{_applnkdir}/Multimedia/wmxmms.desktop
%attr(755,root,root) %{_bindir}/wmxmms
%{_datadir}/xmms/wmxmms*xpm
%{_mandir}/*/wmxmms*

%if %{without gtk2}
%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnomexmms
%{_sysconfdir}/CORBA/servers/*
%{_appletsdir}/Multimedia/*
%{_datadir}/mime-info/xmms.keys
%{_mandir}/*/gnomexmms*
%endif
%endif

%files skins
%defattr(644,root,root,755)
%{_datadir}/xmms/Skins/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmms-config
%attr(755,root,root) %{_libdir}/libxmms.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a

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

%files output-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libesdout*

%files output-disk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/libdisk_writer*

%files visualization-GL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Visualization/libogl_spectrum*
