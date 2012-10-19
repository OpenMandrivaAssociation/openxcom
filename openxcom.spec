%define	git_check 4be8d13

Name:		openxcom
Summary:	Open-source reimplementation of the original X-Com
Version:	0.4.0
Release:	%mkrel 1
#openxcom-0.4.0-4be8d13.tar.bz2
Source0:	https://github.com/SupSuper/OpenXcom/%{name}-%{version}-%{git_check}.tar.bz2
URL:		http://openxcom.org/
Group:		Games/Strategy
License:	GPL
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
%setup -q -n %{name}-%{version}-%{git_check}
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
