Summary:	Arkanoid clone
Summary(pl):	Klon Arkanoida
Name:		lbreakout2
Version:	2.5
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	a58ffde70064afbfbb3dfb82ea6ec643
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-printf-security.patch
URL:		http://lgames.sourceforge.net/index.php?project=LBreakout2
BuildRequires:	SDL-devel >= 1.1.5
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/games

%description
LBreakout is a breakout game with nice graphics, effects and sound.
You can play it either with mouse or keyboard and you can create your
own levels.

%description -l pl
LBreakout to gra breakout z przyjemn� grafik�, efektami i d�wi�kiem.
Mo�na gra� mysz� lub klawiatur� oraz tworzy� w�asne poziomy.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*{html,jpg}
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/lbreakout2
%attr(664,root,games) %config(noreplace) %verify(not mtime md5 size) /var/games/lbreakout*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
