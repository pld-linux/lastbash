Summary:	A console player for Last.fm
Summary(pl):	Konsolowy odtwarzacz dla Last.fm
Name:		lastbash
Version:	0.3.0
Release:	0.1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/lastbash/%{name}-%{version}.tar.gz
# Source0-md5:	c4c65bbb2d17b10db005e12abea85c00
Patch0:		%{name}-Makefile.patch
URL:		http://lastbash.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LastBASH is a console based Last.fm player.

%description -l pl
LastBASH jest konsolowym odtwarzaczem dla Last.fm.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*.1*
