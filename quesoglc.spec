%define _disable_lto 1
%define _disable_rebuild_configure 1

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		quesoglc
Version:	0.7.2
Release:	9
Summary:	The OpenGL Character Renderer

Group:		System/Libraries
License:	LGPLv2+
URL:		http://quesoglc.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}-free.tar.bz2
Patch1:		quesoglc-0.7.2-doxyfile.patch
Patch2:		glew-drop-glewContext.patch
Patch3:		fribidi.build.patch
BuildRequires:  pkgconfig(egl)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xi)
BuildRequires:	doxygen

%description
The OpenGL Character Renderer (GLC) is a state machine that provides OpenGL
programs with character rendering services via an application programming
interface (API).

%package -n	%{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
The OpenGL Character Renderer (GLC) is a state machine that provides OpenGL
programs with character rendering services via an application programming
interface (API).

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package provides the libraries, include files, and other resources needed
for developing GLC applications.

%prep
%setup -q
%apply_patches
rm -f include/GL/{glxew,wglew,glew}.h
ln -s %{_includedir}/GL/{glxew,wglew,glew}.h include/GL/
rm -rf src/fribidi

# make autoreconf more happy
sed -i -e 's,\(AM_INIT_AUTOMAKE(\[\),\1foreign subdir-objects ,' configure.in

autoreconf -fiv

%build
%configure2_5x --disable-static
%make
pushd docs
doxygen
popd

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libGLC.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog COPYING README THANKS docs/html
%{_includedir}/GL/glc.h
%{_libdir}/libGLC.so
%{_libdir}/pkgconfig/quesoglc.pc


%changelog
* Tue Jul 28 2009 Emmanuel Andry <eandry@mandriva.org> 0.7.2-1mdv2010.0
+ Revision: 402527
- New version 0.7.2

* Sun Aug 24 2008 Emmanuel Andry <eandry@mandriva.org> 0.7.1-1mdv2009.0
+ Revision: 275476
- import quesoglc


