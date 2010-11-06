%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A freedesktop.org menu implementation
Name:		garcon
Version:	0.1.2
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/libs/garcon/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	glib2-devel
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Garcon is an implementation of the freedesktop.org menu specification
replacing the former Xfce menu library libxfce4menu. It is based on
GLib/GIO only and aims at covering the entire specification except for
legacy menus.

%package -n %{libname}
Summary:	A freedesktop.org menu implementation
Requires:	%{name} = %{version}-%{release}
Group:		System/Libraries

%description -n %{libname}
Garcon is an implementation of the freedesktop.org menu specification
replacing the former Xfce menu library libxfce4menu. It is based on
GLib/GIO only and aims at covering the entire specification except for
legacy menus.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/xdg/menus/xfce-applications.menu
%{_datadir}/desktop-directories/xfce-*.directory

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/*%{name}*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog HACKING NEWS README STATUS TODO
%{_includedir}/%{name}*
%{_libdir}/*%{name}*.la
%{_libdir}/*%{name}*.so
%{_libdir}/*%{name}*.a
%{_libdir}/pkgconfig/%{name}-*.pc
%{_datadir}/gtk-doc/html/%{name}
