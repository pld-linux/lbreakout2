Summary:	Breakout/Arkanoid style arcade game
Summary(pl.UTF-8):	Gra w stylu Breakouta/Arkanoida
Name:		lbreakout2
Version:	2.6.5
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	1a9238b83f9f13f09b7a4d53e00b4e84
Patch0:		%{name}-useless_files.patch
Patch1:		%{name}-desktop.patch
URL:		http://lgames.sourceforge.net/LBreakout2
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libpng-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/games

%description
LBreakout is a breakout game with nice graphics, effects and sound.
You can play it either with mouse or keyboard and you can create your
own levels.

%description -l pl.UTF-8
LBreakout to gra breakout z przyjemną grafiką, efektami i dźwiękiem.
Można grać myszą lub klawiaturą oraz tworzyć własne poziomy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's,\$(datadir)/icons,$(datadir)/pixmaps,' Makefile.am

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO docs/*{html,jpg}
%attr(2755,root,games) %{_bindir}/lbreakout2
%attr(2755,root,games) %{_bindir}/lbreakout2server
%{_datadir}/lbreakout2
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/lbreakout2.hscr
%{_desktopdir}/lbreakout2.desktop
%{_pixmapsdir}/lbreakout48.gif
