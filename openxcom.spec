Summary:	Open-source reimplementation of the original X-Com
Name:		openxcom
Version:	1.0.0
Release:	1
License:	GPLv3+
Group:		Games/Strategy
Url:		http://openxcom.org/
Source0:	https://github.com/SupSuper/OpenXcom/%{name}-%{version}.tar.gz
# http://www.iconfinder.com/icondetails/1360/128/ufo_icon
Source1:	%{name}.png
BuildRequires:	cmake
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_gfx)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(yaml-cpp)

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
UNITS) to OpenXcom's data folder in the following path:
/usr/share/openxcom/

Important! Please use supported game editions for data files.
Otherwise you may get various messages about missing files or
even segmentation faults.

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%defattr(0644,root,root,0777)
%{_datadir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

# install menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=OpenXcom
Comment=Open-source reimplementation of the original X-Com
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert %{SOURCE1} -resize ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done

