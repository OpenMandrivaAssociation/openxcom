%define	git_check 372-g666c9c9

Name:		openxcom
Summary:	Open-source reimplementation of the original X-Com
Version:	0.3
Release:	%mkrel 3
Source0:	https://github.com/SupSuper/OpenXcom/%{name}-%{version}-%{git_check}.zip
URL:		http://openxcom.org/
Group:		Games/Strategy
License:	GPL
BuildRequires:	SDL_mixer-devel SDL_gfx-devel yaml-devel
BuildRequires:	yaml-cpp-devel TiMidity++ cmake 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf $RPM_BUILD_ROOT
cd build/
%makeinstall DESTDIR=%{buildroot}

%__install -d "%{buildroot}%{_datadir}/%{name}/"

mv "%{buildroot}/usr/bin/DATA" "%{buildroot}%{_datadir}/%{name}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%name
%{_datadir}/%{name}/
