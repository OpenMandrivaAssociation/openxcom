%define	git_check ee4d466

Name:		openxcom
Summary:	Open-source reimplementation of the original X-Com
Version:	0.4.5
Release:	%mkrel 1
%if "%git_check" != ""
#openxcom-0.4.0-4be8d13.tar.bz2
Source0:	https://github.com/SupSuper/OpenXcom/SupSuper-OpenXcom-v%{version}-0-g%{git_check}.tar.gz
%else
Source0:	http://openxcom.org/wp-content/uploads/downloads/2012/11/openxcom-0.4.5.tar.gz
%endif
URL:		http://openxcom.org/
Group:		Games/Strategy
License:	GPLv3
BuildRequires:	yaml-devel
BuildRequires:	pkgconfig(SDL_gfx)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(yaml-cpp)
BuildRequires:	TiMidity++ cmake 

%description
OpenXcom is an open-source reimplementation of the popular
UFO: Enemy Unknown (X-Com: UFO Defense in USA) videogame by
Microprose, licensed under the GPL and written in C++ / SDL.
See more info at the website: http://openxcom.org

OpenXcom requires the original X-Com resources (any version).
If you have the Steam version, you can find the X-Com game
folder in "Steam\steamapps\common\xcom ufo defense\XCOM".

When installing manually, copy the X-Com subfolders (GEODATA,
GEOGRAPH, MAPS, ROUTES, SOUND, TERRAIN, UFOGRAPH, UFOINTRO,
UNITS) to OpenXcom's Data folder in one of the following paths:
/usr/share/openxcom

%prep
%if "%git_check" != ""
%setup -q -n SupSuper-OpenXcom-%git_check
%else
%setup -q
%endif
for i in $( find . \( -name '*.cpp' -o -name '*.h' \));do sed -i '/#include "yaml.h"/s/$/\n#include "yaml-cpp\/yaml.h"/' $i;done

%build
%cmake -DDATADIR=%{_datadir}
%make

%install
cd build/
%makeinstall_std DESTDIR=%{buildroot}

%__install -d "%{buildroot}%{_datadir}/%{name}/"

#mv "%{buildroot}/usr/bin/DATA" "%{buildroot}%{_datadir}/%{name}"

%files
%{_bindir}/%name
%{_datadir}/%{name}/
