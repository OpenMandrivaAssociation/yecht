%{?_javapackages_macros:%_javapackages_macros}
%global commitversion 157cf13
%global dlversion 0.0.2-0-g157cf13
%global cluster olabini

Name:     yecht
Version:  0.0.2
Release:  9.0%{?dist}
Summary:  A YAML processor based on Syck

License:  MIT
URL:            http://github.com/%{cluster}/%{name}
Source0:        %{url}/tarball/%{version}/%{cluster}-%{name}-%{dlversion}.tar.gz
Patch0:   fix-build-xml-classpaths.path

# https://bugzilla.redhat.com/show_bug.cgi?id=561455
Patch1:   add-javadocs-to-build-xml.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: ant
Requires: java
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
%setup -q -n olabini-%{name}-%{commitversion}
%patch0 -p1
%patch1

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
mkdir lib
ant
ant javadocs

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp lib/yecht-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/yecht-%{version}.jar
ln -s %{_javadir}/yecht-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/yecht.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_javadir}/yecht-%{version}.jar
%{_javadir}/yecht.jar

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}

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
