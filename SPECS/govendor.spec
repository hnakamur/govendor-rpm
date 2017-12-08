%define debug_package %{nil}

Name:	        govendor
Version:	1.0.8
Release:	1%{?dist}
Summary:	Go vendor tool that works with the standard vendor file

Group:		Development/Tools
License:	BSD-3-Clause License
URL:		https://github.com/kardianos/govendor


# NOTE: govendor.tar.gz was created with the following commands.
# mkdir -p govendor/go
# cd govendor/go
# export GOPATH=$PWD
# go get -u github.com/kardianos/govendor
# cd src/github.com/kardianos/govendor
# git checkout v1.0.8
# cd $GOPATH/../..
# tar cf - govendor | gzip -9 > govendor.tar.gz
Source0:	govendor.tar.gz

BuildRequires:  golang >= 1.8

%description
Go vendor tool that works with the standard vendor file.

%prep
%setup -n %{name}

%build
export GOPATH=%{_builddir}/%{name}/go
cd %{_builddir}/%{name}/go/src/github.com/kardianos/govendor
go install

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}

%{__install} -pD -m 755 %{_builddir}/%{name}/go/bin/govendor %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Fri Dec  8 2017 <hnakamur@gmail.com> - 1.0.8-1
- 1.0.8
