%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A freedesktop.org menu implementation
Name:		garcon
Version:	0.2.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/libs/garcon/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	glib2-devel
BuildRequires:	libxfce4util-devel >= 4.10.0
Requires:	%{libname} = %{version}

%description
Garcon is an implementation of the freedesktop.org menu specification
replacing the former Xfce menu library libxfce4menu. It is based on
GLib/GIO only and aims at covering the entire specification except for
legacy menus.

%package -n %{libname}
Summary:	A freedesktop.org menu implementation
Group:		System/Libraries
Requires:	%{name} = %{version}
Obsoletes:	%{mklibname xfce4menu 0.1 0} <= 4.6.2

%description -n %{libname}
Garcon is an implementation of the freedesktop.org menu specification
replacing the former Xfce menu library libxfce4menu. It is based on
GLib/GIO only and aims at covering the entire specification except for
legacy menus.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

# (tpg) this file is in mandriva-xfce-config package
#rm -rf %{buildroot}%{_sysconfdir}/xdg/menus/xfce-applications.menu

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%{_datadir}/desktop-directories/xfce-*.directory
%{_sysconfdir}/xdg/menus/xfce-applications.menu

%files -n %{libname}
%{_libdir}/*%{name}*.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog HACKING NEWS README STATUS TODO
%{_includedir}/%{name}*
%{_libdir}/*%{name}*.so
%{_libdir}/pkgconfig/%{name}-*.pc
%{_datadir}/gtk-doc/html/%{name}


%changelog
* Mon Apr 30 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-1
+ Revision: 794641
- update to new version 0.2.0

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.12-1
+ Revision: 791040
- update to new version 0.1.12

* Wed Apr 04 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.11-2
+ Revision: 789104
- bum prequires on libxfce4util-devel to 4.9.0 version
- spec file clean up

* Sat Mar 31 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.11-1
+ Revision: 788505
- update to new version 0.1.11

* Sat Feb 18 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.10-1
+ Revision: 776840
- update to new version 0.1.10

* Fri Jan 06 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.9-2
+ Revision: 757979
- drop la files
- fix find_lang syntax

* Thu Sep 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.9-1
+ Revision: 700795
- add buildrequires on libxfce4util-devel
- update to new version 0.1.9

* Mon Jun 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.8-1
+ Revision: 687563
- update to new version 0.1.8

* Fri Apr 29 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.7-2
+ Revision: 660722
- obsolete old menu library

* Sun Apr 17 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.7-1
+ Revision: 654182
- update to new version 0.1.7

* Sat Apr 09 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.6-1
+ Revision: 652035
- update to new version 0.1.6

* Sat Jan 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.5-1
+ Revision: 632317
- update to new version 0.1.5

* Wed Dec 08 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.4-1mdv2011.0
+ Revision: 616352
- update to new version 0.1.4

* Sun Nov 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.3-1mdv2011.0
+ Revision: 594762
- update to new version 0.1.3

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-3mdv2011.0
+ Revision: 593848
- remove conflicting file with mandriva-xfce-config-common package

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-2mdv2011.0
+ Revision: 593801
- add requires on garcon

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-1mdv2011.0
+ Revision: 593794
- update to new version 0.1.2
- package new menus and new catecory files

* Sat Feb 27 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.1-2mdv2010.1
+ Revision: 512396
- fix requires and provides for devel package
- import garcon


