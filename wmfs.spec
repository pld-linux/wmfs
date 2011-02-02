Summary:	A lightweight and highly configurable tiling window manager for X
Name:		wmfs
Version:	201011
Release:	0.1
License:	other
Group:		X11/Window Managers
Source0:	http://wmfs.info/attachments/download/15/%{name}-%{version}.tar.gz
# Source0-md5:	cf46782e5404f2cb98242580e5ddcd5e
URL:		http://wmfs.info/projects/wmfs/
BuildRequires:	freetype-devel
BuildRequires:	imlib2-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WMFS (Window Manager From Scratch) is a lightweight and highly
configurable tiling window manager for X. It can be configured with a
configuration file, supports Xft (Freetype) fonts and is compliant
with the Extended Window Manager Hints (EWMH) specifications, Xinerama
and Xrandr. WMFS can be driven with Vi based commands (ViWMFS).
Optional Imlib2 support allow WMFS to draw image instead text
everywhere you want with a simple sequence.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}"
LDFLAGS="%{rpmldflags}"
for lib in freetype2 imlib2 xrandr xinerama; do
	CFLAGS="$CFLAGS $(pkg-config --cflags $lib)"
	LDFLAGS="$LDFLAGS $(pkg-config --libs $lib)"
done
export CFLAGS LDFLAGS

./configure \
	--prefix %{_prefix} \
	--xdg-config-dir %{_sysconfdir}/xdg \
	--man-prefix %{_mandir}


%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_sysconfdir}/xdg/%{name}
%{_mandir}/man1/wmfs*
