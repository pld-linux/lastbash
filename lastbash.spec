Summary:	A console player for Last.fm
Summary(pl):	Konsolowy odtwarzacz dla Last.fm
Name:		lastbash
Version:	0.3.0
Release:	0.1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/lastbash/%{name}-%{version}.tar.gz
# Source0-md5:	c4c65bbb2d17b10db005e12abea85c00
URL:		http://lastbash.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LastBASH is a console based Last.fm player.

%description -l pl
LastBASH jest konsolowym odtwarzaczem dla Last.fm.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=/usr \
	mandir=$RPM_BUILD_ROOT/usr/share/man \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_datadir}/%{name}/{AUTHORS,ChangeLog,README,TODO,COPYING,INSTALL,VERSION}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*.1*
