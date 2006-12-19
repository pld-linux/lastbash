Summary:	A console player for Last.fm
Summary(pl):	Konsolowy odtwarzacz dla Last.fm
Name:		lastbash
Version:	0.3.1
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/lastbash/%{name}-%{version}.tar.gz
# Source0-md5:	fe4c5af28f3fa7704e8e7ae80ccbbba0
URL:		http://lastbash.sourceforge.net/
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
	prefix=%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/lastbash

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*.1*
