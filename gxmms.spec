Summary:	GNOME panel applet to control XMMS
Summary(pl):	Aplet panelu GNOME do sterowania XMMS-em
Name:		gxmms
Version:	0.1.1
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://savannah.nongnu.org/download/gxmms/%{name}-%{version}.tar.gz
# Source0-md5:	9ccd24388604533f12c4c7ee478cc149
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%{_pixmapsdir}/*.png
