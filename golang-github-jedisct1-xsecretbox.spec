# Run tests in check section
%bcond_without check

%global goipath         github.com/jedisct1/xsecretbox
%global commit          7a679c0bcd9a5bbfe097fb7d48497bc06d17be76

%global common_description %{expand:
Go implementation of crypto_secretbox_xchacha20poly1305.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Go implementation of crypto_secretbox_xchacha20poly1305 
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/aead/chacha20/chacha)
BuildRequires: golang(github.com/aead/poly1305)
BuildRequires: golang(golang.org/x/crypto/curve25519)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup

rm -rf vendor


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180518git7a679c0
- Remove vendored packages

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git7a679c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180518git7a679c0
- First package for Fedora

