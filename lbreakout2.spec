Summary:	Arkanoid clone
Summary(pl):	Klon Arkanoida
Name:		lbreakout2
Version:	2.5
%define bver	beta-3
%define	brel	%(echo %{bver} | tr -d -)
Release:	1.%{brel}.2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/lgames/%{name}-%{version}%{bver}.tar.gz
# Source0-md5:	eff7e1e961f33e80e2c3a7f04daf69de
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-printf-security.patch
URL:		http://www.lgames.org/
BuildRequires:	SDL-devel >= 1.1.5
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LBreakout is a breakout game with nice graphics, effects and sound.
You can play it either with mouse or keyboard and you can create your
own levels.

%description -l pl
LBreakout to gra breakout z przyjemn± grafik±, efektami i d¼wiêkiem.
Mo¿na graæ mysz± lub klawiatur± oraz tworzyæ w³asne poziomy.

%prep
%setup -q -n %{name}-%{version}%{bver}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-highscore-path=/var/games
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/games,%{_desktopdir},%{_pixmapsdir}}

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
%{_datadir}/games/lbreakout2
%attr(664,root,games) %config(noreplace) %verify(not mtime md5 size) /var/games/lbreakout*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
