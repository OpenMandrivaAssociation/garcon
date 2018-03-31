%define major 0
%define api 1
%define libname %mklibname %{name}- %{api} %{major}
%define gtklibname %mklibname %{name}-gtk2_ %{api} %{major}
%define gtk3libname %mklibname %{name}-gtk3_ %{api} %{major}
%define develname %mklibname %{name} -d
%define url_ver %(echo %{version} | cut -c 1-3)
%define _disable_rebuild_configure 1

Summary:	A freedesktop.org menu implementation
Name:		garcon
Version:	0.6.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/libs/garcon/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxfce4util-1.0) >= 4.12.0
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.12.0
Requires:	%{libname} = %{version}-%{release}

%description
Garcon is an implementation of the freedesktop.org menu specification
replacing the former Xfce menu library libxfce4menu. It is based on
GLib/GIO only and aims at covering the entire specification except for
legacy menus.

%package -n %{libname}
Summary:	A freedesktop.org menu implementation
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Obsoletes:	%{mklibname xfce4menu 0.1 0} <= 4.6.2
Obsoletes:	%{mklibname garcon 0} < 0.2.1

%description -n %{libname}
Garcon is an implementation of the freedesktop.org menu specification
replacing the former Xfce menu library libxfce4menu. It is based on
GLib/GIO only and aims at covering the entire specification except for
legacy menus.

%package -n %{gtklibname}
Summary:	Common GTK library for Xfce's freedesktop.org menu implementation
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
 	
%description -n %{gtklibname}
Garcon is an implementation of the freedesktop.org menu specification
replacing the former Xfce menu library libxfce4menu. It is based on
GLib/GIO only and aims at covering the entire specification except for
legacy menus.

%package -n %{gtk3libname}
Summary:        Common GTK library for Xfce's freedesktop.org menu implementation
Group:          System/Libraries
Requires:       %{name} = %{EVRD}

%description -n %{gtk3libname}
Garcon is an implementation of the freedesktop.org menu specification
replacing the former Xfce menu library libxfce4menu. It is based on
GLib/GIO only and aims at covering the entire specification except for
legacy menus

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{gtklibname} = %{EVRD}
Requires:	%{gtk3libname} = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%setup -q

%build
%configure \
	--disable-static

%make

%install
%makeinstall_std

# (tpg) this file is in mandriva-xfce-config package
rm -rf %{buildroot}%{_sysconfdir}/xdg/menus/xfce-applications.menu

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%{_datadir}/desktop-directories/xfce-*.directory
#%{_sysconfdir}/xdg/menus/xfce-applications.menu

%files -n %{libname}
%{_libdir}/*%{name}-%{api}.so.%{major}*

%files -n %{gtklibname}
%{_libdir}/lib%{name}-gtk2-%{api}.so.%{major}*

%files -n %{gtk3libname}
%{_libdir}/lib%{name}-gtk3-%{api}.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog HACKING NEWS README STATUS TODO
%{_includedir}/%{name}*
%{_libdir}/*%{name}*.so
%{_libdir}/pkgconfig/%{name}-*.pc
%{_datadir}/gtk-doc/html/%{name}
