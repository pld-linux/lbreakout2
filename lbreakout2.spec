Summary:	Arkanoid clone
Summary(pl):	Klon Arkanoida
Name:		lbreakout2
Version:	2.2.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://ftp1.sourceforge.net/lgames/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.lgames.org/
BuildRequires:	SDL-devel >= 1.1.5
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
LBreakout is a breakout game with nice graphics, effects and sound.
You can play it either with mouse or keyboard and you can create your
own levels.

%description -l pl
LBreakout to gra breakout z przyjemn± grafik±, efektami i d¼wiêkiem.
Mo¿na graæ mysz± lub klawiatur± oraz tworzyæ w³asne poziomy.

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure \
	--with-highscore-path=/var/games
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Arcade,/var/games,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/docs/*{html,jpg}
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/games/lbreakout2
%attr(664,root,games) %config(noreplace) %verify(not mtime md5 size) /var/games/lbreakout*
%{_applnkdir}/Games/Arcade/*
%{_pixmapsdir}/*
