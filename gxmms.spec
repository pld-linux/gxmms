Summary:	GNOME panel applet to control XMMS
Summary(pl):	Aplet panelu GNOME do sterowania XMMS-em
Name:		gxmms
Version:	0.1.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://savannah.nongnu.org/download/gxmms/%{name}-%{version}.tar.gz
# Source0-md5:	f03a433107c64a07b077621c5bf1787d
URL:		http://www.nongnu.org/gxmms/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	xmms-devel >= 1.2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gXMMS is a simple GNOME panel applet that lets you control the basic
functions of the X MultiMedia System (XMMS).

%description -l pl
gXMMS jest prostym apletem panelu GNOME, który pozwala kontrolowaæ
podstawowe funkcje XMMS.

%prep
%setup -q

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%{_pixmapsdir}/*.png
