Name: hunspell-hy
Summary: Armenian hunspell dictionaries
Version: 0.20.0
Release: 5%{?dist}
Source: http://downloads.sourceforge.net/armspell/myspell-hy-%{version}.tar.gz
Group: Applications/Text
URL: http://sourceforge.net/projects/armspell
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Armenian hunspell dictionaries.

%prep
%setup -q -n myspell-hy-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p hy_AM.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Copyright ChangeLog COPYING
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 06 2010 Caolán McNamara <caolanm@redhat.com> - 0.20.0-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 30 2008 Caolan McNamara <caolanm@redhat.com> - 0.10.1-1
- initial version
