%{?_javapackages_macros:%_javapackages_macros}

Name:     yecht
Version:  1.0
Release:  1.1
Summary:  A YAML processor based on Syck
Group:	Development/Java
License:  MIT
URL:            http://github.com/jruby/%{name}
Source0:        %{url}/tarball/%{version}/%{name}-%{name}-%{version}.tar.gz
Patch0:   disable-jruby-dep.patch

BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: maven-local
Requires: java-headless
Requires: jpackage-utils

BuildArch:      noarch

%description
Yecht is a Syck port, a YAML 1.0 processor for Ruby.

%package javadoc
Summary:        Javadocs for %{name}

Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -n %{name}-%{name}-%{version}
%patch0

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May  06 2010  Mohammed Morsi <mmorsi@redhat.com> - 0.0.2-4
- sync'd tarball source w/ upstream
- added my name that was missing from changelog

* Wed May  05 2010  Mohammed Morsi <mmorsi@redhat.com> - 0.0.2-3
- added Alexander Kurtakov's patch to generate javadocs
- added javadoc bits to the spec

* Tue Apr  27 2010  Mohammed Morsi <mmorsi@redhat.com> - 0.0.2-2
- removed deprecated gcj bits
- fixed source uri

* Thu Jan  21 2009  Mohammed Morsi <mmorsi@redhat.com> - 0.0.2-1
- Initial build.
