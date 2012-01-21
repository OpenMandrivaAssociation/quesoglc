%define major	0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:           quesoglc
Version:        0.7.2
Release:        %mkrel 1
Summary:        The OpenGL Character Renderer

Group:          System/Libraries
License:        LGPLv2+
URL:            http://quesoglc.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-free.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  pkgconfig(fontconfig) pkgconfig(glut)
BuildRequires:  pkgconfig(fribidi) pkgconfig(glew) pkgconfig(sm) pkgconfig(xmu)
BuildRequires:  pkgconfig(xi) doxygen
BuildRequires:  pkgconfig 

%description
The OpenGL Character Renderer (GLC) is a state machine that provides OpenGL
programs with character rendering services via an application programming
interface (API).

%package -n	%{libname}
Summary:        Libraries for %{name}
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n	%{libname}
The OpenGL Character Renderer (GLC) is a state machine that provides OpenGL
programs with character rendering services via an application programming
interface (API).

%package -n	%{develname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package provides the libraries, include files, and other resources needed
for developing GLC applications.

%prep
%setup -q
rm -f include/GL/{glxew,wglew,glew}.h
ln -s %{_includedir}/GL/{glxew,wglew,glew}.h include/GL/

%build
%configure --disable-static 
%make
cd docs
doxygen
cd ../

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/libGLC.la

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libGLC.so.%{major}*
%doc AUTHORS ChangeLog COPYING README THANKS docs/html

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/GL/glc.h
%{_libdir}/libGLC.so
%{_libdir}/pkgconfig/quesoglc.pc
