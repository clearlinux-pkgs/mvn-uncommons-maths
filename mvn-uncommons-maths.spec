#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-uncommons-maths
Version  : 1
Release  : 1
URL      : https://repo.maven.apache.org/maven2/org/uncommons/maths/uncommons-maths/1.2.2a/uncommons-maths-1.2.2a-sources.jar
Source0  : https://repo.maven.apache.org/maven2/org/uncommons/maths/uncommons-maths/1.2.2a/uncommons-maths-1.2.2a-sources.jar
Source1  : https://repo.maven.apache.org/maven2/org/uncommons/maths/uncommons-maths/1.2.2a/uncommons-maths-1.2.2a.jar
Source2  : https://repo.maven.apache.org/maven2/org/uncommons/maths/uncommons-maths/1.2.2a/uncommons-maths-1.2.2a.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-uncommons-maths-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-uncommons-maths package.
Group: Data

%description data
data components for the mvn-uncommons-maths package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/uncommons/maths/uncommons-maths/1.2.2a
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/uncommons/maths/uncommons-maths/1.2.2a/uncommons-maths-1.2.2a-sources.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/uncommons/maths/uncommons-maths/1.2.2a
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/uncommons/maths/uncommons-maths/1.2.2a/uncommons-maths-1.2.2a.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/uncommons/maths/uncommons-maths/1.2.2a
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/uncommons/maths/uncommons-maths/1.2.2a/uncommons-maths-1.2.2a.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/uncommons/maths/uncommons-maths/1.2.2a/uncommons-maths-1.2.2a-sources.jar
/usr/share/java/.m2/repository/org/uncommons/maths/uncommons-maths/1.2.2a/uncommons-maths-1.2.2a.jar
/usr/share/java/.m2/repository/org/uncommons/maths/uncommons-maths/1.2.2a/uncommons-maths-1.2.2a.pom
