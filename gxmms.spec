#
# TODO:
# fix problem with:
# gxmms_applet:12137): GConf-CRITICAL **: 
# file gconf-client.c: line 547 (gconf_client_add_dir):
# assertion `gconf_valid_key (dirname, NULL)' failed

Summary:	GNOME panel applet to control XMMS
Summary(pl.UTF-8):	Aplet panelu GNOME do sterowania XMMS-em
Name:		gxmms
Version:	0.3.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://savannah.nongnu.org/download/gxmms/%{name}-%{version}.tar.gz
# Source0-md5:	fd1faca60413ff3c893535d4a856c5ea
URL:		http://www.nongnu.org/gxmms/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	gnome-panel-devel < 3
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
# also bmp-devel >= 0.9.0 supported
BuildRequires:	xmms-devel >= 1.2.8
Requires:	xmms >= 1.2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gXMMS is a simple GNOME panel applet that lets you control the basic
functions of the X MultiMedia System (XMMS).

%description -l pl.UTF-8
gXMMS jest prostym apletem panelu GNOME, który pozwala kontrolować
podstawowe funkcje XMMS.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-xmms
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT{%{_libexecdir},%{_bindir}}/gxmms_applet

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/gxmms
%{_datadir}/%{name}
%{_libdir}/bonobo/servers/GNOME_gxmmsApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_gxmmsApplet.xml
%{_pixmapsdir}/gxmms.png
%{_pixmapsdir}/gxmms_mini.png
