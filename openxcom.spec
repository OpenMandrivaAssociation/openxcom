%define	git_check 372-g666c9c9

Name:		openxcom
Summary:	Curtain is a tool that show a movable and resizable curtain on the desktop screen
Version:	0.3
Release:	%mkrel 1
Source0:	https://github.com/SupSuper/OpenXcom/%{name}-%{version}-%{git_check}.zip
URL:		http://openxcom.org/
Group:		Education
License:	GPL
BuildRequires:	SDL_mixer-devel SDL_gfx-devel yaml-devel
BuildRequires:	yaml-cpp-devel TiMidity++ 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Patch0:		yaml_include.patch

%description
Curtain is a tool that show a movable and resizable curtain
on the desktop screen
You can use this to hide and show objects on the desktop
This program has been implemented for educational purposes

%prep
%setup -q -n %{name}-%{version}-%{git_check}
%patch0 -p1

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
