Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Name:		xmms
Version:	0.9.1
Release:	3
Copyright:	GPL
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Vendor:		Peter Alm, Mikael Alm, Olle Hällnäs, Thomas Nilsson and others.
Source0:	http://www.xmms.org/xmms-%{version}.tar.gz
Source1:	xmms.desktop
Source2:	mp3license
Patch0:		xmms-configure.in.patch
Patch1:		xmms-divzero.patch
URL:		http://www.xmms.org/
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	esound-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	mikmod-devel
Requires:	glib >= 1.2.2
Requires:	gtk+ >= 1.2.2
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
XMMS is a sound player written from scratch. Since it uses the WinAmp
GUI, it can use WinAmp skins, and play mp3s, mods, s3ms, and other 
formats. It now has support for input, output, and general plugins, and
has also been GPL'd.

%package mikmod
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
Requires:	libmikmod >= 3.1.5

%description mikmod
Input plugin for XMMS to play MODs (.MOD,.XM,.S3M, etc)

%package esd
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
Requires:	esound >= 0.2.8

%description esd
Output plugin for xmms for use with the esound package

%package gnome
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
Requires:	gnome-libs >= 1.0.0

%description gnome
GNOME applet for controlling xmms from the GNOME panel

%package devel
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and header files required for compiling xmms plugins.

%package static
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries required for compiling xmms plugins.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

cp %{SOURCE2} .

%build
automake; autoconf
(cd libxmms; automake; autoconf)
LDFLAGS="-s"; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/applnk/Multimedia/

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/Multimedia/

gzip -9nf AUTHORS ChangeLog NEWS README mp3license

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
/etc/X11/applnk/Multimedia/xmms.desktop
%attr(755,root,root) %{_bindir}/xmms
%attr(755,root,root) %{_bindir}/wmxmms
%attr(755,root,root) %{_libdir}/libxmms.so.*.*
%{_libdir}/xmms/Input/libcdaudio*
%{_libdir}/xmms/Input/libmpg123*
%{_libdir}/xmms/Input/libwav*
%{_libdir}/xmms/Output/libOSS*
%{_libdir}/xmms/Output/libdisk_writer*
%{_libdir}/xmms/General/*
%{_libdir}/xmms/Effect/*
%{_datadir}/xmms/*

%files mikmod
%defattr(644, root, root, 755)
%{_libdir}/xmms/Input/libmikmod*

%files esd
%defattr(644, root, root, 755)
%{_libdir}/xmms/Output/libesdout*

%files gnome
%defattr(644, root, root, 755)
%{prefix}/bin/gnomexmms
%{prefix}/etc/CORBA/*
%{_datadir}/applets/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644, root, root, 755)
%{_libdir}/lib*.a
