Summary:	A console player for Last.fm
Summary(pl.UTF-8):	Konsolowy odtwarzacz dla Last.fm
Name:		lastbash
Version:	0.3.2
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/lastbash/%{name}-%{version}.tar.gz
# Source0-md5:	8846371db96932c0b53de8a04f9d5997
URL:		http://lastbash.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LastBASH is a console based Last.fm player.

%description -l pl.UTF-8
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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lastbash.config
%{_mandir}/man1/*.1*
