Summary:	Arkanoid clone
Summary(pl):	Klon Arkanoida
Name:		lbreakout2
Version:	2.3.5
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://ftp1.sourceforge.net/lgames/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-png-conflict.patch
URL:		http://www.lgames.org/
BuildRequires:	SDL-devel >= 1.1.5
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

# temporary - workaround for gcc 3.[12] ICE 
%ifarch athlon
%define		optflags	-O2 -march=athlon -mno-mmx -mno-3dnow
%endif

%description
LBreakout is a breakout game with nice graphics, effects and sound.
You can play it either with mouse or keyboard and you can create your
own levels.

%description -l pl
LBreakout to gra breakout z przyjemn± grafik±, efektami i d¼wiêkiem.
Mo¿na graæ mysz± lub klawiatur± oraz tworzyæ w³asne poziomy.

%prep
%setup -q
%patch -p1

mv -f client/png.h client/pngm.h

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
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
%doc docs/*{html,jpg}
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/games/lbreakout2
%attr(664,root,games) %config(noreplace) %verify(not mtime md5 size) /var/games/lbreakout*
%{_applnkdir}/Games/Arcade/*
%{_pixmapsdir}/*
