Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Name:		xmms
Version:	0.9.1
Release:	1
Copyright:	GPL
Group:		X11/Multimedia
Vendor:		Peter Alm, Mikael Alm, Olle Hällnäs, Thomas Nilsson and others.
Url:		http://www.xmms.org/
Source:		http://www.xmms.org/xmms-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
BuildPrereq:	glib-devel
BuildPrereq:	gtk+-devel
BuildPrereq:	esound-devel
BuildPrereq:	gnome-libs-devel
BuildPrereq:	mikmod-devel
Requires:	glib >= 1.2.2
Requires:	gtk+ >= 1.2.2

%define		_prefix		/usr/X11R6

%description
XMMS is a sound player written from scratch. Since it uses the WinAmp
GUI, it can use WinAmp skins, and play mp3s, mods, s3ms, and other 
formats. It now has support for input, output, and general plugins, and
has also been GPL'd.

%package	mikmod
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Group:		X11/Multimedia
Requires:	%{name} = %{version}
Requires:	libmikmod >= 3.1.5

%description mikmod
Input plugin for XMMS to play MODs (.MOD,.XM,.S3M, etc)

%package esd
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Group:		X11/Multimedia
Requires:	%{name} = %{version}
Requires:	esound >= 0.2.8

%description esd
Output plugin for xmms for use with the esound package

%package gnome
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Group:		X11/Multimedia
Requires:	%{name} = %{version}
Requires:	gnome-libs >= 1.0.0

%description gnome
GNOME applet for controlling xmms from the GNOME panel

%package devel
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Group:		X11/Multimedia
Requires:	%{name} = %{version}

%description devel
Libraries and header files required for compiling xmms plugins.

%package static
Summary:	Sound player with the WinAmp GUI, for Unix-based systems
Group:		X11/Multimedia
Requires:	%{name}-devel = %{version}

%description static
Static libraries required for compiling xmms plugins.


%prep
%setup

%build
CFLAGS=$RPM_OPT_FLAGS LDFLAGS="-s" \
./configure \
	--prefix=%{_prefix} \
	--sysconfdir=/etc/X11/GNOME

make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/%{_prefix} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%{_bindir}/xmms
%{_bindir}/wmxmms
%{_libdir}/libxmms.so.*
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
%defattr(644, root, root, 755)
%{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644, root, root, 755)
%{_libdir}/lib*.a

%changelog
* Fri Apr 09 1999 Lyle Kempler <kempler@utdallas.edu>
- initial version
