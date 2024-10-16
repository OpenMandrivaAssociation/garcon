%define major 0
%define api 1
%define libname %mklibname %{name}- %{api} %{major}
%define gtklibname %mklibname %{name}-gtk3_ %{api} %{major}
%define develname %mklibname %{name} -d
%define url_ver %(echo %{version} | cut -c 1-3)
%define _disable_rebuild_configure 1

Summary:	A freedesktop.org menu implementation
Name:		garcon
Version:	4.18.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		https://www.xfce.org
Source0:	https://archive.xfce.org/src/xfce/garcon/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	gtk-doc
BuildRequires:	gtk-doc-mkpdf
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:  xfce4-dev-tools

Requires:	%{libname} = %{version}-%{release}

%description
Garcon is an implementation of the freedesktop.org menu specification
replacing the former Xfce menu library libxfce4menu. It is based on
GLib/GIO only and aims at covering the entire specification except for
legacy menus.

%files -f %{name}.lang
%{_datadir}/desktop-directories/xfce-*.directory
%{_sysconfdir}/xdg/menus/xfce-applications.menu
%{_iconsdir}/hicolor/*/apps/org.xfce.garcon.png

#---------------------------------------------------------------------------

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

%files -n %{libname}
%{_libdir}/*%{name}-%{api}.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{gtklibname}
Summary:	Common GTK library for Xfce's freedesktop.org menu implementation
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{gtklibname}
Garcon is an implementation of the freedesktop.org menu specification
replacing the former Xfce menu library libxfce4menu. It is based on
GLib/GIO only and aims at covering the entire specification except for
legacy menus.

%files -n %{gtklibname}
%{_libdir}/lib%{name}-gtk3-%{api}.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{gtklibname} = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}

%description -n %{develname}
Development files and headers for %{name}.

%files -n %{develname}
%doc AUTHORS NEWS README*
%{_includedir}/%{name}*
%{_libdir}/*%{name}*.so
%{_libdir}/pkgconfig/%{name}-*.pc
%{_datadir}/gtk-doc/html/%{name}

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

# (tpg) this file is in mandriva-xfce-config package
#rm -rf %{buildroot}%{_sysconfdir}/xdg/menus/xfce-applications.menu

# locales
%find_lang %{name} %{name}.lang
