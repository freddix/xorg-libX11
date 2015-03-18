# based on PLD Linux spec git://git.pld-linux.org/packages/xorg-lib-libX11.git
Summary:	X11 Base library
Name:		xorg-libX11
Version:	1.6.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libX11-%{version}.tar.bz2
# Source0-md5:	2e36b73f8a42143142dda8129f02e4e0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libtool
BuildRequires:	libxcb-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-proto >= 7.7
BuildRequires:	xorg-util-macros
BuildRequires:	xorg-xtrans-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X11 Base library.

%package devel
Summary:	Header files for libX11 library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed to develop programs that
use libX11.

%prep
%setup -qn libX11-%{version}

# support __libmansuffix__ and __filemansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__libmansuffix__/,.so man3/,' \
            -e 's,\.so man__filemansuffix__/,.so man5/,' man/*.man

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-specs=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%dir %{_datadir}/X11
%attr(755,root,root) %ghost %{_libdir}/libX11-xcb.so.?
%attr(755,root,root) %ghost %{_libdir}/libX11.so.?
%attr(755,root,root) %{_libdir}/libX11-xcb.so.*.*.*
%attr(755,root,root) %{_libdir}/libX11.so.*.*.*
%{_datadir}/X11/XErrorDB
%{_datadir}/X11/Xcms.txt

%dir %{_datadir}/X11/locale
%{_datadir}/X11/locale/C
%{_datadir}/X11/locale/compose.dir
%{_datadir}/X11/locale/en_US.UTF-8
%{_datadir}/X11/locale/locale.alias
%{_datadir}/X11/locale/locale.dir

%{_datadir}/X11/locale/armscii-8
%{_datadir}/X11/locale/georgian-academy
%{_datadir}/X11/locale/georgian-ps
%{_datadir}/X11/locale/ibm-cp1133
%{_datadir}/X11/locale/iscii-dev
%{_datadir}/X11/locale/isiri-3342
%{_datadir}/X11/locale/iso8859-1
%{_datadir}/X11/locale/iso8859-10
%{_datadir}/X11/locale/iso8859-11
%{_datadir}/X11/locale/iso8859-13
%{_datadir}/X11/locale/iso8859-14
%{_datadir}/X11/locale/iso8859-15
%{_datadir}/X11/locale/iso8859-2
%{_datadir}/X11/locale/iso8859-3
%{_datadir}/X11/locale/iso8859-4
%{_datadir}/X11/locale/iso8859-5
%{_datadir}/X11/locale/iso8859-6
%{_datadir}/X11/locale/iso8859-7
%{_datadir}/X11/locale/iso8859-8
%{_datadir}/X11/locale/iso8859-9
%{_datadir}/X11/locale/iso8859-9e
%{_datadir}/X11/locale/koi8-c
%{_datadir}/X11/locale/koi8-r
%{_datadir}/X11/locale/koi8-u
%{_datadir}/X11/locale/microsoft-cp1251
%{_datadir}/X11/locale/microsoft-cp1255
%{_datadir}/X11/locale/microsoft-cp1256
%{_datadir}/X11/locale/mulelao-1
%{_datadir}/X11/locale/nokhchi-1
%{_datadir}/X11/locale/tatar-cyr
%{_datadir}/X11/locale/tscii-0

%lang(am) %{_datadir}/X11/locale/am_ET.UTF-8
%lang(el) %{_datadir}/X11/locale/el_GR.UTF-8
%lang(fi) %{_datadir}/X11/locale/fi_FI.UTF-8
%lang(ja) %{_datadir}/X11/locale/ja*
%lang(ko) %{_datadir}/X11/locale/ko
%lang(ko) %{_datadir}/X11/locale/ko_*
%lang(pt_BR) %{_datadir}/X11/locale/pt_BR.UTF-8
%lang(ru) %{_datadir}/X11/locale/ru_RU.UTF-8
%lang(th) %{_datadir}/X11/locale/th_TH*
%lang(vi) %{_datadir}/X11/locale/vi_VN*
%lang(zh_CN) %{_datadir}/X11/locale/zh_CN*
%lang(zh_HK) %{_datadir}/X11/locale/zh_HK*
%lang(zh_TW) %{_datadir}/X11/locale/zh_TW*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libX11-xcb.so
%attr(755,root,root) %{_libdir}/libX11.so
%{_includedir}/X11/*.h
%{_pkgconfigdir}/x11-xcb.pc
%{_pkgconfigdir}/x11.pc
%{_mandir}/man3/*.3x*

